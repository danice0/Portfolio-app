import streamlit as st
from views import about_me, work_experiences, projects, chatbot
import time

# Set Streamlit page configuration
st.set_page_config(
    page_title="Daniel Sallah Portfolio",
    page_icon=":chart_with_upwards_trend:",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Initialize session state first thing
if "page" not in st.session_state:
    st.session_state.page = "About Me"
if "last_click" not in st.session_state:
    st.session_state.last_click = time.time()
if "render_id" not in st.session_state:
    st.session_state.render_id = 0

# Define pages
PAGES = {
    "About Me": about_me,
    "Work Experiences": work_experiences,
    "Projects": projects,
    "Chatbot/Contact Me": chatbot,
}

# Cache the CSS
@st.cache_data
def get_css():
    return """
        <style>
            /* Performance optimized styles */
            .stApp {
                background-color: #121212 !important;
            }
            
            .navbar-container {
                position: fixed;
                top: 0;
                left: 0;
                right: 0;
                z-index: 999;
                background-color: rgba(18, 18, 18, 0.95);
                padding: 0.5rem;
                backdrop-filter: blur(8px);
                -webkit-backdrop-filter: blur(8px);
            }
            
            .content-container {
                margin-top: 4rem;
                padding: 1rem;
            }
            
            .stButton button {
                width: 100%;
                padding: 0.5rem !important;
                transition: background-color 0.2s ease, transform 0.2s ease !important;
                border: none !important;
                background-color: transparent !important;
                color: white !important;
            }
            
            .stButton button:hover {
                background-color: rgba(255, 255, 255, 0.1) !important;
                transform: translateY(-1px);
            }
            
            .stButton button:active {
                transform: translateY(1px);
            }
            
            /* Hide Streamlit components */
            #MainMenu, header, footer {display: none !important;}
            
            /* Responsive design */
            @media (max-width: 768px) {
                .navbar-container {
                    position: sticky;
                }
                .content-container {
                    margin-top: 1rem;
                }
            }
        </style>
    """

def handle_navigation(page_name):
    current_time = time.time()
    if current_time - st.session_state.last_click > 0.3:  # 300ms debounce
        st.session_state.page = page_name
        st.session_state.last_click = current_time
        st.session_state.render_id += 1

@st.cache_data
def get_page_component(_page_name, _render_id):
    """Cache page components with render ID to handle updates"""
    return PAGES.get(_page_name)

def main():
    # Apply CSS
    st.markdown(get_css(), unsafe_allow_html=True)
    
    # Navigation bar
    st.markdown('<div class="navbar-container">', unsafe_allow_html=True)
    cols = st.columns(len(PAGES))
    
    # Handle navigation buttons
    for i, page_name in enumerate(PAGES.keys()):
        with cols[i]:
            is_current = st.session_state.page == page_name
            button_style = "primary" if is_current else "secondary"
            
            if st.button(
                page_name,
                key=f"nav_{page_name}_{st.session_state.render_id}",
                type=button_style,
                use_container_width=True
            ):
                handle_navigation(page_name)
                st.rerun()
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Content area
    st.markdown('<div class="content-container">', unsafe_allow_html=True)
    try:
        # Get current page component
        current_page = st.session_state.page
        page_component = PAGES.get(current_page)
        
        if page_component:
            with st.container():
                page_component.app()
        else:
            st.error("Page not found")
            PAGES["About Me"].app()
            
    except Exception as e:
        st.error(f"Error loading page: {str(e)}")
        PAGES["About Me"].app()
        
    st.markdown('</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()