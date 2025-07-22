import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
import tensorflow as tf
from PIL import Image
from src.data_management import load_pkl_file


# Load TFLite model only once at the global level
@st.cache_resource
def load_tflite_model(version):
    interpreter = tf.lite.Interpreter(
        model_path=f"outputs/{version}/mildew_detector_model.tflite")
    interpreter.allocate_tensors()
    return interpreter


# Load image shape only once
@st.cache_data
def get_image_shape(version):
    return load_pkl_file(file_path=f"outputs/{version}/image_shape.pkl")


def plot_predictions_probabilities(pred_proba, pred_class):
    """
    Plot prediction probability results
    """

    prob_per_class = pd.DataFrame(
        data=[0, 0],
        index={'Parasitised': 0, 'Healthy': 1}.keys(),
        columns=['Probability']
    )
    prob_per_class.loc[pred_class] = pred_proba
    for x in prob_per_class.index.to_list():
        if x not in pred_class:
            prob_per_class.loc[x] = 1 - pred_proba
    prob_per_class = prob_per_class.round(3)
    prob_per_class['Diagnostic'] = prob_per_class.index

    fig = px.bar(
        prob_per_class,
        x='Diagnostic',
        y=prob_per_class['Probability'],
        range_y=[0, 1],
        width=600, height=300, template='seaborn')
    st.plotly_chart(fig)


def resize_input_image(img, version):
    """
    Reshape image to average image size
    """
    image_shape = get_image_shape(version)
    img_resized = img.resize((image_shape[1], image_shape[0]), Image.LANCZOS)
    my_image = np.array(img_resized) / 255.0
    my_image = np.expand_dims(my_image, axis=0).astype(np.float32)

    return my_image


def load_model_and_predict(interpreter, my_image):
    """
    Perform prediction using a pre-loaded TFLite model interpreter.
    """
    # Allocate tensors (safe to call again; no overhead if already done)
    interpreter.allocate_tensors()

    input_details = interpreter.get_input_details()
    output_details = interpreter.get_output_details()

    # Ensure data is float32
    my_image = my_image.astype(np.float32)

    # Set input tensor
    interpreter.set_tensor(input_details[0]['index'], my_image)

    # Run inference
    interpreter.invoke()

    # Get prediction
    pred_proba = interpreter.get_tensor(output_details[0]['index'])[0][0]

    target_map = {v: k for k, v in {'Parasitised': 0, 'Uninfected': 1}.items()}
    pred_class = target_map[pred_proba > 0.5]
    if pred_class == target_map[0]:
        pred_proba = 1 - pred_proba

    st.write(
        f"The predictive analysis indicates the sample cell is "
        f"**{pred_class.lower()}** with mildew.")

    return pred_proba, pred_class
