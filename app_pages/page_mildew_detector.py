import streamlit as st
from PIL import Image
import numpy as np
import pandas as pd

from src.data_management import download_dataframe_as_csv
from src.machine_learning.predictive_analysis import (
                                                    load_model_and_predict,
                                                    resize_input_image,
                                                    plot_predictions_probabilities,
                                                    load_tflite_model
                                                    )


# Cache the TFLite model per version to save memory and load time
@st.cache_resource
def load_model_cached(version):
    return load_tflite_model(version)


def page_mildew_detector_body():
    st.info(
        "* The client is interested in telling whether a given cherry leaf contains mildew or not."
    )

    st.write(
        "* You can download a set of mildew-contained and healthy cherry leaves for live prediction. "
        "You can download the images from [here](https://www.kaggle.com/datasets/codeinstitute/cherry-leaves)."
    )

    st.write("---")

    images_buffer = st.file_uploader(
        "Upload samples. You may select more than one.",
        type="png",
        accept_multiple_files=True,
    )

    if images_buffer is not None:
        version = "v1"
        model = load_model_cached(version)  # ✅ load once with cache

        df_report = pd.DataFrame([])
        for image in images_buffer:
            img_pil = Image.open(image)
            st.info(f"Sample: **{image.name}**")
            img_array = np.array(img_pil)
            st.image(
                img_pil,
                caption=f"Image Size: {img_array.shape[1]}px width x {img_array.shape[0]}px height",
            )

            resized_img = resize_input_image(img=img_pil, version=version)

            # ✅ Pass the cached model to the prediction function
            pred_proba, pred_class = load_model_and_predict(
                model, resized_img
            )

            plot_predictions_probabilities(pred_proba, pred_class)

            df_report = df_report._append(
                {"Name": image.name, "Result": pred_class}, ignore_index=True
            )

        if not df_report.empty:
            st.success("Analysis Report")
            st.table(df_report)
            st.markdown(download_dataframe_as_csv(df_report), unsafe_allow_html=True)
