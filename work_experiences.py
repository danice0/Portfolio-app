import streamlit as st
import base64
import os

def work_experience():
    # Set path to the background image
    background_image_path = r"C:\Users\USER\OneDrive\Desktop\stra\media\image2.jpg"

    # Read and embed the background image using CSS
    with open(background_image_path, "rb") as bg_file:
        bg_image_data = bg_file.read()
        bg_image_url = f"data:image/jpeg;base64,{base64.b64encode(bg_image_data).decode()}"

    # Apply CSS for styling
    st.markdown(f"""
        <style>
        .stApp {{
            background: url("{bg_image_url}");
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        .section-container {{
            background-color: rgba(255, 255, 255, 0.8);
            border-radius: 10px;
            padding: 20px;
            margin-bottom: 20px;
            color: black;
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
        }}
        .job-title {{
            color: #2c3e50;
            font-weight: bold;
        }}
        .job-company {{
            color: #34495e;
            font-style: italic;
        }}
        .certification-tab {{
            margin-bottom: 25px;
            padding: 20px;
            background-color: #f9f9f9;
            border-radius: 10px;
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
            transition: transform 0.3s, box-shadow 0.3s, background-color 0.3s;
            display: flex;
            align-items: center;
        }}
        .certification-tab:hover {{
            transform: translateY(-5px);
            box-shadow: 0 8px 15px rgba(0, 0, 0, 0.2);
            background-color: #f0f8ff;
        }}
        .certification-icon {{
            font-size: 30px;
            margin-right: 15px;
            color: #2196F3;
        }}
        .certification-name {{
            font-size: 18px;
            font-weight: bold;
            color: #333;
        }}
        </style>
    """, unsafe_allow_html=True)

    # Title for Professional Experience
    st.title("💼 Professional Experience")

    # Experience Sections
    experiences = [
        {
            "title": "Trainer for Small and Medium-Scale Enterprises",
            "company": "The University of Ghana in collaboration with IDRC",
            "duration": "Feb 2024 – Dec 2024 | Legon, Ghana",
            "responsibilities": ["Appointed Trainer for SMEs in Digitalization Project"],
            "referees": [
                {"name": "Dr. ASIEDU EDWARD", "role": "Senior Lecturer at UG", "contact": "0550244204"},
                {"name": "MAD. BETTY", "role": "Project Supervisor", "contact": "0545213845"}
            ],
            "key": "referee_1",
        },
        {
            "title": "National Service Personnel - Revenue Department",
            "company": "Ashaiman Municipal Assembly (ASHMA)",
            "duration": "Nov 2022 – Sep 2023 | Ashaiman, Ghana",
            "responsibilities": [
                "Mobilized revenue to support community activities",
                "Gathered data for property rate bills"
            ],
            "referees": [
                {"name": "MRS. JUSTINA AMETEPE", "role": "Former Revenue Officer", "contact": "+233(0)24 500 2905"}
            ],
            "key": "referee_2",
        },
        {
            "title": "Internship - Telecom Technician",
            "company": "Signal Regiment, Burma Camp",
            "duration": "Oct 2021 – Jan 2022 | Ghana",
            "responsibilities": [
                "Trained on PBX systems",
                "Installed and tested telecom equipment",
                "Assisted with communication cables in camp offices"
            ],
            "referees": [
                {"name": "Mr. Ishmael", "role": "Telecom Supervisor", "contact": "+233(0)54 381 9817"},
                {"name": "Sergeant Eric Anloga", "role": "Telecom Specialist", "contact": "+233(0)24 572 2583"}
            ],
            "key": "referee_3",
        }
    ]

    for exp in experiences:
        with st.expander(exp["title"]):
            st.markdown(f"""
                <div class="section-container">
                    <h3 class="job-title">{exp["title"]}</h3>
                    <p class="job-company">{exp["company"]}</p>
                    <p><strong>Duration:</strong> {exp["duration"]}</p>
                    <ul>
                        {''.join(f"<li>{task}</li>" for task in exp["responsibilities"])}
                    </ul>
                </div>
            """, unsafe_allow_html=True)

            if st.button(f"Show Referees for {exp['title']}", key=exp["key"]):
                for referee in exp["referees"]:
                    st.markdown(f"""
                        <p><strong>{referee['name']}:</strong> {referee['role']} - {referee['contact']}</p>
                    """, unsafe_allow_html=True)

    # Certifications Section
    st.markdown("## 🏆 View Certifications")

    certifications = {
        "AWS Badges and Certifications": {"icon": "🛡️", "url": "https://www.credly.com/users/daniel-sallah"},
        "ALX Certificate": {"icon": "📜", "url": "https://drive.google.com/file/d/1rP6z5FPX0M-oxToyoH1ZGrsG3izWBSB3/view?usp=drive_link"},
        "NSS Certificate": {"icon": "📃", "url": "https://drive.google.com/file/d/1_bA0wKLlTw1-Az3YQlhE8Vk0H4EGHWTa/view?usp=drive_link"},
        "Data Science & Analytics Certificate": {"icon": "📊", "url": "https://drive.google.com/file/d/1Wa8YA3o46XsJZtwTRDPyHkV2bYzUMfN_/view?usp=drive_link"},
        "Data & Business Analytics Certificate": {"icon": "📈", "url": "https://drive.google.com/file/d/1eC7zUO-nkKZew-0uraE027dnCB_oyXPq/view?usp=drive_link"},
        "Built Finance Certificate": {"icon": "💼", "url": "https://drive.google.com/file/d/1xBxjYSzAhC46tdcsu29XD8zSWcodXY6x/view?usp=drive_link"},
    }

    cols = st.columns(2)  # Arrange certifications in two columns
    for i, (cert_name, cert_data) in enumerate(certifications.items()):
        with cols[i % 2]:
            st.markdown(f"""
                <a href="{cert_data['url']}" target="_blank" class="certification-tab">
                    <span class="certification-icon">{cert_data['icon']}</span>
                    <span class="certification-name">{cert_name}</span>
                </a>
            """, unsafe_allow_html=True)

    # Skills Section
    st.markdown("## 🛠 Key Skills")
    skills = ["Microsoft Suite", "AWS Cloud", "Graphic Design (Canva)", "Python", "Power BI", "MySQL"]

    cols = st.columns(3)
    for i, skill in enumerate(skills):
        cols[i % 3].markdown(f"- {skill}", unsafe_allow_html=True)

def app():
    work_experience()

if __name__ == "__main__":
    app()
