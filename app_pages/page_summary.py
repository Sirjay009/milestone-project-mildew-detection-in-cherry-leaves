import streamlit as st
import matplotlib.pyplot as plt


def page_summary_body():

    st.write("### Quick Project Summary")

    st.info(
        f"**General Information**\n"
        f"* Powdery mildew diseases are caused by many different species of "
        f"ascomycete fungi in the order Erysiphales.\n"
        f"* Infected plants display white powdery spots on the leaves and stems. "
        f"Visual criteria are used to detect infected leaves.\n"
        f"* A 2018 University of Zurich research - "
        f"(https://phys.org/news/2018-01-combination-resistance-genes-wheat-powdery.html) - "
        f"finds that the Pm3 allele is an effective genetic resistance strategy "
        f"that protects host species against powdery mildew fungus.\n\n"
        f"**Project Dataset**\n"
        f"* The available dataset contains 4208 images of equally divided "
        f"healthy cherry leaves and mildew-infected leaves. "
        )

    st.write(
        f"* For additional information, please visit and **read** the "
        f"[Project README file](https://github.com/Sirjay009/milestone-project-mildew-detection-in-cherry-leaves/blob/main/README.md).")
    

    st.success(
        f"The project has 2 business requirements:\n"
        f"* 1 - The client is interested in conducting a study to visually differentiate "
        f"a cherry leaf that is healthy from one that contains powdery mildew.\n"
        f"* 2 - The client is interested in predicting if a cherry leaf is healthy or contains powdery mildew. "
        )