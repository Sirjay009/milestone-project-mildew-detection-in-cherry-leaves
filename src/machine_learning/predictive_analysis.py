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
    Plot prediction probability results.
    """

    # Set the correct mapping
    all_classes = ['Healthy', 'Powdery Mildew']
    prob_per_class = pd.DataFrame(columns=['Diagnostic', 'Probability'])

    try:
        for class_name in all_classes:
            prob = pred_proba if class_name == pred_class else 1 - pred_proba
            prob_per_class = prob_per_class._append({
                'Diagnostic': class_name,
                'Probability': round(prob, 3)
            }, ignore_index=True)
    except Exception as e:
        st.warning(f"⚠️ Could not plot prediction: {e}")
        return

    fig = px.bar(
        prob_per_class,
        x='Diagnostic',
        y='Probability',
        range_y=[0, 1],
        width=600,
        height=300,
        template='seaborn'
    )
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

    try:
        # Allocate tensors (safe to re-call)
        interpreter.allocate_tensors()

        input_details = interpreter.get_input_details()
        output_details = interpreter.get_output_details()

        expected_shape = input_details[0]['shape']  # Example: [1, 256, 256, 3]

        # Ensure image is float32
        my_image = my_image.astype(np.float32)

        # ✅ Shape Validation
        if list(my_image.shape) != list(expected_shape):
            st.error(
                f"❌ Input image shape mismatch!\n\n"
                f"Expected: {expected_shape}, Got: {my_image.shape}\n\n"
                f"Please ensure your image has 3 color channels (RGB)."
            )
            return None, None

        # Set input tensor
        interpreter.set_tensor(input_details[0]['index'], my_image)

        # Run inference
        interpreter.invoke()

        # Get prediction
        pred_proba = interpreter.get_tensor(output_details[0]['index'])[0][0]

        # Interpret prediction
        if pred_proba > 0.5:
            pred_class = 'Powdery Mildew'
            confidence = pred_proba
        else:
            pred_class = 'Healthy'
            confidence = 1 - pred_proba

        # Display result
        st.success(
            f"✅ The predictive analysis indicates the sample leaf is "
            f"**{pred_class}** with a confidence of **{confidence * 100:.2f}%**."
        )

        return confidence, pred_class

    except Exception:
        st.error(
            "⚠️ An unexpected error occurred during prediction. "
            "Please try another image or check the input format."
        )
        return None, None
