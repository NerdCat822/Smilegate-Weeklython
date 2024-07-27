import streamlit as st
from st_pages import show_pages_from_config
from utils import load_page_config, set_sidebar_width
from PIL import Image

if __name__ == "__main__":
    # Display the pages based on configuration
    show_pages_from_config()
    
    # Load page configuration
    load_page_config()
    set_sidebar_width()

    # Add content on top of the image
    st.markdown(
        """
        <div class="content">
            <h1>Beyond The Language Barrier 👀</h1>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Load the local image
    image_path = "imgs/img.png"
    image = Image.open(image_path)

    st.markdown(
        """
        <style>
        .full-screen-image {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            object-fit: cover;
            z-index: -1;
        }
        .content {
            position: relative;
            z-index: 1;
            color: white;
            padding: 20px;
            text-align: center;
        }
        .stImage > img {
            width: 100%;
            height: 100vh;
            object-fit: cover;
        }
        .stImage > div:nth-child(2) {
            position: absolute;
            bottom: 0;
            left: 0;
            right: 0;
            background-color: rgba(0, 0, 0, 0.5);
            color: white;
            padding: 10px;
            text-align: center;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Display the image as a full-screen background with caption
    st.image(image, use_column_width=True, output_format="png", caption="© 2024 언어유희. All rights reserved.")