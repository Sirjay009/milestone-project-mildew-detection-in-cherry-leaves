import streamlit as st
import matplotlib.pyplot as plt


def page_project_hypothesis_body():
    st.write("### Project Hypothesis and Validation")

    st.success(
        f"* We suspect mildew-parasitised cherry leaves have clear signs of fungus infection, "
        f"typically all over the leaf, that can differentiate them from a healthy cherry leaf. \n\n"
        f"* An Image Montage shows that typically a mildew-parasitised cherry leaf has powdery patches across it. "
        f"Average Image, Variability Image and Difference between Averages studies did not reveal "
        f"any clear pattern to differentiate one from another."

    )
