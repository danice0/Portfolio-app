import streamlit as st
from views import about_me, work_experiences, projects, chatbot # Import all pages/modules

# Set Streamlit page configuration (Move this to the top)
st.set_page_config(
    page_title="Daniel Sallah Portfolio",
    page_icon=":chart_with_upwards_trend:",
    layout="wide",
    initial_sidebar_state="collapsed",  # No sidebar by default
)

# Define a dictionary that links page names to their respective modules
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

    # Check if there's a page parameter in the URL
    query_params = st.query_params
    if "page" in query_params:
        # Convert URL parameter back to original page name
        url_page = query_params["page"][0].replace('_', ' ')
        if url_page in PAGES:
            st.session_state.selected_page = url_page

    # Responsive and Performance-Optimized CSS
    st.markdown("""
        <style>
            /* Global Styles */
            body, .stApp {
                font-family: 'Inter', 'Segoe UI', sans-serif;
                background-color: #121212;
                color: #E0E0E0;
                margin: 0;
                padding: 0;
                overscroll-behavior-x: none;
            }

            /* Responsive Navbar */
            @media screen and (max-width: 768px) {
                .navbar {
                    flex-direction: column;
                    padding: 5px 0;
                }
                .navbar button {
                    width: 100%;
                    margin: 5px 0;
                    padding: 8px 15px;
                    font-size: 16px;
                }
            }

            .navbar {
                display: flex;
                justify-content: center;
                align-items: center;
                background-color: rgba(30, 30, 30, 0.9);
                padding: 10px 0;
                position: sticky;
                top: 0;
                z-index: 1000;
                backdrop-filter: blur(10px);
                box-shadow: 0 2px 5px rgba(0,0,0,0.2);
                width: 100%;
                transition: all 0.3s ease;
            }

            .navbar button {
                background-color: transparent;
                border: none;
                color: #E0E0E0;
                margin: 0 15px;
                padding: 10px 20px;
                font-size: 16px;
                font-weight: 500;
                cursor: pointer;
                border-radius: 5px;
                transition: all 0.3s ease;
                text-transform: uppercase;
                letter-spacing: 1px;
            }

            .navbar button:hover {
                background-color: rgba(64, 224, 208, 0.1);
                color: #40E0D0;
                transform: scale(1.05);
            }

            .navbar button.active {
                background-color: rgba(64, 224, 208, 0.2);
                color: #40E0D0;
                box-shadow: 0 0 10px rgba(64, 224, 208, 0.5);
            }

            /* Performance Optimizations */
            .stMarkdown, .stButton, .stTextInput {
                transition: opacity 0.2s ease;
            }

            /* Hide Streamlit Hamburger Menu and Footer */
            header { visibility: hidden; }
            footer { visibility: hidden; }
            
            /* Responsive Typography */
            @media screen and (max-width: 600px) {
                .stMarkdown h1 { font-size: 24px !important; }
                .stMarkdown h2 { font-size: 20px !important; }
                .stMarkdown p { font-size: 14px !important; }
            }
        </style>
    """, unsafe_allow_html=True)

    # Performance-Enhanced Navbar
    st.markdown('<div class="navbar">', unsafe_allow_html=True)
    cols = st.columns(len(PAGES))
    for i, (page_name, page_module) in enumerate(PAGES.items()):
        with cols[i]:
            # Use st.query_params for page switching
            if st.button(page_name, key=f"nav_{page_name}", 
                         type="primary" if page_name == st.session_state.selected_page else "secondary"):
                st.session_state.selected_page = page_name
                # Add query parameter for shareable links
                st.query_params["page"] = page_name.replace(' ', '_')
    st.markdown('</div>', unsafe_allow_html=True)

    # Dynamic Page Loading with Caching
    @st.cache_resource
    def load_page_module(page_name):
        return PAGES.get(page_name)

    # Dynamically load the selected page with error handling
    try:
        page_module = load_page_module(st.session_state.selected_page)
        if page_module:
            # Performance hint: use st.container for faster rendering
            with st.container():
                page_module.app()
        else:
            st.error("Page not found. Defaulting to About Me.")
            about_me.app()
    except Exception as e:
        st.error(f"An error occurred while loading the page: {e}")
        about_me.app()

# Use st.cache decorators in individual page modules to improve loading speed
if __name__ == "__main__":
    main()