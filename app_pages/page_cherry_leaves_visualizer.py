import streamlit as st
import os
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.image import imread

import itertools
import random


def page_cherry_leaves_visualizer_body():
    st.write("### 🍒 Cherry Leaves Visualizer")
    st.info(
        "* The client is interested in a study that visually distinguishes "
        "healthy cherry leaves from those infected with powdery mildew."
    )

    version = 'v1'

    # Section 1: Average and Variability Images
    if st.checkbox("📊 Show Average and Variability Images"):
        try:
            avg_pm = imread(f"outputs/{version}/avg_var_powdery_mildew.png")
            avg_healthy = imread(f"outputs/{version}/avg_var_healthy.png")

            st.warning(
                "* The average and variability images show only subtle color differences "
                "between healthy and mildew-infected leaves."
            )
            st.image(avg_pm, caption="Powdery Mildew - Average and Variability", use_column_width=True)
            st.image(avg_healthy, caption="Healthy Leaf - Average and Variability", use_column_width=True)
        except FileNotFoundError:
            st.error("❌ Average/variability image files not found.")
        st.write("---")

    # Section 2: Difference Image
    if st.checkbox("🧮 Show Difference Between Average Images"):
        try:
            diff_img = imread(f"outputs/{version}/avg_diff.png")
            st.warning(
                "* This comparison also doesn't show strong visual cues "
                "between healthy and infected leaves."
            )
            st.image(diff_img, caption="Difference Between Average Images", use_column_width=True)
        except FileNotFoundError:
            st.error("❌ Difference image file not found.")
        st.write("---")

    # Section 3: Image Montage
    if st.checkbox("🖼️ Show Image Montage"):
        st.write("* Click the 'Create Montage' button to refresh the image grid.")

        my_data_dir = 'inputs/cherry-leaves/cherry-leaves/validation'
        if os.path.exists(my_data_dir):
            labels = os.listdir(my_data_dir)
            label_to_display = st.selectbox("Select label", options=labels, index=0)

            if st.button("Create Montage"):
                image_montage(
                    dir_path=my_data_dir,
                    label_to_display=label_to_display,
                    nrows=4, ncols=2, figsize=(10, 12)  # Reduced for performance
                )
        else:
            st.error("❌ Image directory not found.")
        st.write("---")


def image_montage(dir_path, label_to_display, nrows=4, ncols=2, figsize=(10, 12)):
    sns.set_style("white")
    labels = os.listdir(dir_path)

    # Ensure selected label is valid
    if label_to_display not in labels:
        st.warning("⚠️ The label you selected doesn't exist.")
        st.info(f"Available labels: {labels}")
        return

    # Get image list for the label
    image_dir = os.path.join(dir_path, label_to_display)
    images_list = os.listdir(image_dir)

    # Limit number of images to avoid memory overload
    max_images = nrows * ncols
    if len(images_list) < max_images:
        st.warning(
            f"Only {len(images_list)} images available — montage will fill only part of the grid."
        )
        img_idx = images_list
        # Adjust grid size dynamically
        nrows = int(np.ceil(len(img_idx) / ncols))
    else:
        img_idx = random.sample(images_list, max_images)

    # Prepare plot layout
    fig, axes = plt.subplots(nrows=nrows, ncols=ncols, figsize=figsize)
    axes = axes.flatten()  # Flatten in case of 1D axes

    for i, img_name in enumerate(img_idx):
        img_path = os.path.join(image_dir, img_name)
        img = imread(img_path)
        img_shape = img.shape
        axes[i].imshow(img)
        axes[i].set_title(f"{img_shape[1]}px × {img_shape[0]}px")
        axes[i].axis("off")

    # Hide unused axes
    for j in range(len(img_idx), len(axes)):
        axes[j].axis("off")

    plt.tight_layout()
    st.pyplot(fig)
    plt.close(fig)  # Free memory