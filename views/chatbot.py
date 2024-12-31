import streamlit as st
import base64
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(to_email, subject, body):
    """Send an email using SMTP."""
    from_email = "sallahdaniel0@gmail.com"  # Your Gmail address
    app_password = "qtid tmbi qmod tgam"  # Your Gmail app password

    try:
        # Create the email
        msg = MIMEMultipart()
        msg['From'] = from_email
        msg['To'] = to_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        # Send the email
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(from_email, app_password)
        server.send_message(msg)
        server.quit()
        return True
    except Exception as e:
        st.error(f"Failed to send email: {e}")
        return False

def app():
    # Set up the background image
    background_image_path = r"C:\Users\USER\OneDrive\Desktop\stra\media\CONTACT.jpg"
    with open(background_image_path, "rb") as bg_file:
        bg_image_data = bg_file.read()
        bg_image_url = f"data:image/jpeg;base64,{base64.b64encode(bg_image_data).decode()}"

    # Apply CSS styles
    st.markdown(f"""
        <style>
            .stApp {{
                background: url("{bg_image_url}");
                background-size: cover;
                background-position: center;
                background-repeat: no-repeat;
                background-attachment: fixed;
            }}
            .header {{
                text-align: center;
                color: white;
                margin-top: 50px;
                padding: 20px;
                background: rgba(0, 0, 0, 0.6);
                border-radius: 10px;
            }}
            .header h1 {{
                font-size: 3rem;
                margin-bottom: 10px;
            }}
            .header p {{
                font-size: 1.5rem;
            }}
            .contact-form {{
                background-color: white;
                padding: 2rem;
                border-radius: 10px;
                box-shadow: 0 2px 15px rgba(0,0,0,0.2);
                margin: 2rem auto;
                max-width: 700px;
            }}
            .contact-form h2 {{
                text-align: center;
                color: #0056b3;
                margin-bottom: 20px;
            }}
            .footer {{
                text-align: center;
                color: white;
                margin-top: 50px;
                padding: 10px;
            }}
            .footer a {{
                color: #40E0D0;
                text-decoration: none;
            }}
        </style>
    """, unsafe_allow_html=True)

    # Header Section
    st.markdown("""
        <div class="header">
            <h1>CUSTOMER SERVICE</h1>
            <p>Feel free to reach out for any inquiries or support. I am here to help!</p>
        </div>
    """, unsafe_allow_html=True)

    # Initialize session state for input fields
    if "form_submitted" not in st.session_state:
        st.session_state.form_submitted = False

    # Contact Form
    st.markdown('<div class="contact-form">', unsafe_allow_html=True)
    st.markdown('<h2>Get in Touch</h2>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        first_name = st.text_input("First Name", key="first_name" if not st.session_state.form_submitted else "")
    with col2:
        last_name = st.text_input("Last Name", key="last_name" if not st.session_state.form_submitted else "")

    email = st.text_input("Email Address", key="email" if not st.session_state.form_submitted else "")
    phone = st.text_input("Phone Number", key="phone" if not st.session_state.form_submitted else "")
    message = st.text_area("Message", height=150, key="message" if not st.session_state.form_submitted else "")

    if st.button("Submit"):
        if first_name and last_name and email and phone and message:
            with st.spinner("Sending your message..."):
                # Send the email to yourself
                to_admin = "sallahdaniel0@gmail.com"  # Your email address
                subject_admin = f"New Message from {first_name} {last_name}"
                body_admin = f"""
                You have received a new message via the Customer Service page:

                Name: {first_name} {last_name}
                Email: {email}
                Phone: {phone}

                Message:
                {message}
                """
                admin_email_sent = send_email(to_admin, subject_admin, body_admin)

                # Send acknowledgment email to the user
                subject_user = "Acknowledgment: Message Received"
                body_user = f"""
                Dear {first_name},

                Thank you for reaching out! I have received your message and will get back to you shortly.

                Best regards,
                Daniel Sallah
                """
                user_email_sent = send_email(email, subject_user, body_user)

                if admin_email_sent and user_email_sent:
                    st.success("Your message has been sent successfully! Check your email for acknowledgment.")
                    st.session_state.form_submitted = True
                else:
                    st.error("There was an issue sending your message. Please try again.")
        else:
            st.warning("Please fill in all fields before submitting.")

    st.markdown('</div>', unsafe_allow_html=True)

    # Footer
    st.markdown("""
        <div class="footer">
            <p>📧 Email: <a href="mailto:sallahdaniel0@gmail.com">sallahdaniel0@gmail.com</a></p>
            <p>📞 Phone: +233 559 093 797</p>
            <a href="https://linkedin.com/in/daniel-sallah-7b2475169" target="_blank">🔗 LinkedIn Profile</a>
        </div>
    """, unsafe_allow_html=True)

# Run the app
if __name__ == "__main__":
    app()
