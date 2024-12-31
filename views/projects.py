import streamlit as st
import base64
from pathlib import Path

def app():
    """Main function for the projects page."""

    # Use a relative path for the background image
    background_path = Path("media/EEE.jpg")  # Place your image in a "media" folder within your app's directory
    
    if background_path.exists():  # Check if the file exists
        with open(background_path, "rb") as image_file:
            encoded_image = base64.b64encode(image_file.read()).decode()

        # Embed the image as base64 in CSS
        st.markdown(f"""
        <style>
            .stApp {{
                background-image: url("data:image/jpg;base64,{encoded_image}"); 
                background-size: cover;
                background-position: center;
                background-repeat: no-repeat;
                background-attachment: fixed;
            }}

            /* Title Styling */
            h1 {{
                font-family: 'Helvetica Neue', sans-serif;
                color: #ffffff;
                text-align: center;
                text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
                padding: 20px;
                background: rgba(0,0,0,0.6);
                border-radius: 10px;
                margin-bottom: 40px;
            }}
            
            /* Project Card Styling */
            .project-card {{
                background: rgba(255, 255, 255, 0.9);
                padding: 30px;
                border-radius: 20px;
                box-shadow: 0 4px 6px rgba(0,0,0,0.1);
                margin: 20px;
                transition: all 0.3s ease;
                height: 100%;
            }}
            
            .project-card:hover {{
                transform: translateY(-5px);
                box-shadow: 0 8px 12px rgba(0,0,0,0.2);
                background: rgba(255, 255, 255, 0.95);
            }}
            
            /* Project Title Styling */
            .project-title {{
                font-family: 'Georgia', serif;
                font-size: 1.6rem;
                color: #2c3e50;
                margin-bottom: 10px;
                font-weight: bold;
                text-align: center;
            }}
            
            /* Button Styling */
            .view-project-btn {{
                display: block;
                width: 100%;
                padding: 15px;
                font-size: 1.2rem;
                background: linear-gradient(45deg, #2196F3, #1976D2);
                color: white;
                text-align: center;
                text-decoration: none;
                border-radius: 10px;
                font-family: 'Roboto', sans-serif;
                font-weight: 600;
                transition: all 0.3s ease;
            }}
            
            .view-project-btn:hover {{
                background: linear-gradient(45deg, #1976D2, #1565C0);
                transform: scale(1.05);
            }}

            /* Icon Styling */
            .project-icon {{
                font-size: 2.5rem;
                color: #2196F3;
                text-align: center;
                margin-bottom: 10px;
            }}
        </style>
        """, unsafe_allow_html=True)
    else:
        st.error("Background image not found. Please check the file path.")

    # Title
    st.title("💼 Data Analysis Projects")
    
    # Project Configuration with Icons
    PROJECT_FILES = {
        "BILIV AUGMENTA": {
            "url": "https://drive.google.com/file/d/1euQw8uKXsrbgIdl9GM-GmK7lPVLQywAa/view?usp=drive_link",
            "icon": "📊"
        },
        "CD Project": {
            "url": "https://drive.google.com/file/d/1fJYQDPXla9uzKolth_ADB0c6NjRckwD6/view?usp=drive_link",
            "icon": "📈"
        },
        "EXPRESS MART": {
            "url": "https://drive.google.com/file/d/1wAie7_D--809e0AZycbkjKmj2xI6wvIN/view?usp=drive_link",
            "icon": "📉"
        },
        "NEBULON FIN DATA": {
            "url": "https://drive.google.com/file/d/17tMe5Bh9tHpbt3qdEKN6ztdiRb7ZbiFL/view?usp=drive_link",
            "icon": "📋"
        },
        "QUANTIUM DATA ANALYTICS": {
            "url": "https://drive.google.com/file/d/1Vr1ttZ3keOSS6H_f7UP8iyN6Q8MkwNjK/view?usp=drive_link",
            "icon": "📚"
        },
        "VEXTEX MOBILE NET DATA": {
            "url": "https://drive.google.com/file/d/1-pZ0YU4V4qzOcW4zPuXY0JPGZg5nhvps/view?usp=drive_link",
            "icon": "🖥️"
        }
    }
    
    # Display projects in a grid
    cols = st.columns(3)
    for idx, (project_name, project_data) in enumerate(PROJECT_FILES.items()):
        with cols[idx % 3]:
            st.markdown(f"""
            <div class="project-card">
                <div class="project-icon">{project_data["icon"]}</div>
                <div class="project-title">{project_name}</div>
                <a href="{project_data["url"]}" target="_blank" class="view-project-btn">
                    View Project
                </a>
            </div>
            """, unsafe_allow_html=True)

if __name__ == "__main__":
    app()
