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

# Function to initialize the session state
def initialize_session_state():
    if "selected_page" not in st.session_state:
        st.session_state.selected_page = "About Me"  # Default page
    if "pages_loaded" not in st.session_state:
        st.session_state.pages_loaded = {}  # Track loaded pages

# Lazy load function for pages
def load_page(page_name):
    # Check if the page is already loaded, if not, load it
    if page_name not in st.session_state.pages_loaded:
        page_module = PAGES.get(page_name)
        if page_module:
            # Only run the page's `app` function if it's not cached yet
            page_module.app()
            st.session_state.pages_loaded[page_name] = True
        else:
            st.error("Page not found. Defaulting to About Me.")
            about_me.app()

def main():
    initialize_session_state()

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
    load_page(st.session_state.selected_page)

if __name__ == "__main__":
    main()
