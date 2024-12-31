import streamlit as st
import base64
import os

def app():
    # Use relative paths for deployment compatibility
    profile_image_path = os.path.join("media", "profile.jpg")
    background_image_path = os.path.join("media", "image1.jpg")

    # Check if files exist and handle errors
    try:
        # Read the background image
        with open(background_image_path, "rb") as bg_file:
            bg_image_data = bg_file.read()
            bg_image_url = f"data:image/jpeg;base64,{base64.b64encode(bg_image_data).decode()}"
    except FileNotFoundError:
        bg_image_url = None
        st.warning("Background image not found. Using a default background.")

    try:
        # Read the profile image
        with open(profile_image_path, "rb") as profile_file:
            profile_image_data = profile_file.read()
            profile_image_url = f"data:image/jpeg;base64,{base64.b64encode(profile_image_data).decode()}"
    except FileNotFoundError:
        profile_image_url = None
        st.warning("Profile image not found. Please upload a profile image.")

    # Display background image using CSS
    if bg_image_url:
        st.markdown(f"""
            <style>
            .stApp {{
                background: url("{bg_image_url}");
                background-size: cover;
                background-repeat: no-repeat;
                background-attachment: fixed;
                height: 100vh;
                color: #FFFFFF;
            }}
            </style>
        """, unsafe_allow_html=True)

    # About section with text and profile image
    st.markdown(f"""
        <div style="display: flex; align-items: center; justify-content: space-between;">
            <div style="max-width: 600px;">
                <h1 style="color: gold;">ABOUT ME</h1>
                <h2>Hi, I'm SALLAH KWAKU DANIEL 👋</h2>
                <p>
                    Daniel Sallah is a highly skilled Data Analyst, Network Engineer, and AWS Cloud Practitioner based in Accra, GH. With a strong foundation in signal processing and wireless communication, he excels in transforming complex data into actionable insights using Python.
                </p>
                <h3>Fun Facts About Me:</h3>
                <ul>
                    <li>🌍 Based in Accra-Tema, GH</li>
                    <li>💻 Languages: Python, MATLAB, and more</li>
                    <li>🎯 Hobbies: Coding, traveling, gaming, and graphic design</li>
                </ul>
                <a href="https://drive.google.com/file/d/1g0J-oM-s3lgOaFpiKTn2klII9fEXjL1s/view?usp=drive_link" target="_blank" class="download-btn">Download CV</a>
            </div>
            <div>
                {f'<img src="{profile_image_url}" alt="Profile Image" style="max-width: 300px; border-radius: 10px; box-shadow: 0 0 30px gold;" />' if profile_image_url else ''}
            </div>
        </div>
    """, unsafe_allow_html=True)
