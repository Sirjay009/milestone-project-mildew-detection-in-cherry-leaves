import streamlit as st
import matplotlib.pyplot as plt


def page_project_hypothesis_body():
    st.write("### Project Hypothesis and Validation")

    st.success(
        f"* We opine that mildew-infected cherry leaves have clear signs of fungus infection, "
        f"characterized typically by discolouration and white powedry spots all over the leaf,"
        f"that differentiate them from a healthy cherry leaf. \n\n"
        f"* An Image Montage shows that typically a mildew-infected cherry is mostly discoloured and "
        f"has white powdery patches across it's surface."
        f"Average Image, Variability Image and Difference between Averages studies did not reveal "
        f"any clear pattern to differentiate one from another."

    )
