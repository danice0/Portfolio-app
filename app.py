import streamlit as st
from views import about_me, work_experiences, projects, chatbot  # Import all pages/modules

# Set Streamlit page configuration
st.set_page_config(
    page_title="Daniel Sallah Portfolio",
    page_icon=":chart_with_upwards_trend:",
    layout="wide",
    initial_sidebar_state="collapsed",  # No sidebar by default
)

# Define a dictionary linking page names to modules
PAGES = {
    "About Me": about_me,
    "Work Experiences": work_experiences,
    "Projects": projects,
    "Chatbot/Contact Me": chatbot,
}

def main():
    # Initialize session state for selected page
    if "selected_page" not in st.session_state:
        st.session_state.selected_page = "About Me"  # Default page

    # Responsive Navbar
    st.markdown('<div class="navbar">', unsafe_allow_html=True)
    cols = st.columns(len(PAGES))
    for i, (page_name, page_module) in enumerate(PAGES.items()):
        with cols[i]:
            if st.button(page_name, key=f"nav_{page_name}", 
                         type="primary" if page_name == st.session_state.selected_page else "secondary"):
                st.session_state.selected_page = page_name
    st.markdown('</div>', unsafe_allow_html=True)

    # Load the selected page
    page_module = PAGES.get(st.session_state.selected_page)
    if page_module:
        page_module.app()
    else:
        st.error("Page not found. Defaulting to About Me.")
        about_me.app()

if __name__ == "__main__":
    main()
