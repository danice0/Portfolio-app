import streamlit as st
from views import about_me, work_experiences, projects, chatbot
import time
from functools import lru_cache

# Performance-optimized page configuration
st.set_page_config(
    page_title="Daniel Sallah Portfolio",
    page_icon=":chart_with_upwards_trend:",
    layout="wide",
    initial_sidebar_state="collapsed",
    menu_items=None
)

# Initialize session state
if not hasattr(st.session_state, "page"):
    st.session_state.page: str = "About Me"
if not hasattr(st.session_state, "last_click"):
    st.session_state.last_click: float = time.time()
if not hasattr(st.session_state, "render_id"):
    st.session_state.render_id: int = 0
if not hasattr(st.session_state, "is_loading"):
    st.session_state.is_loading: bool = False

# Cache page components
@lru_cache(maxsize=None)
def get_page_component(page_name: str):
    return PAGES.get(page_name)

# Define pages
PAGES: dict = {
    "About Me": about_me,
    "Work Experiences": work_experiences,
    "Projects": projects,
    "Chatbot/Contact Me": chatbot,
}

# Optimized CSS caching
@st.cache_data
def get_css() -> str:
    return """
    <style>
    /* ... (previous CSS remains the same until here) ... */

    /* Loader Container */
    .loader-container {
        position: fixed;
        top: 0;
        left: 0;
        width: 100vw;
        height: 100vh;
        display: flex;
        justify-content: center;
        align-items: center;
        background: rgba(18, 18, 18, 0.8);
        backdrop-filter: blur(5px);
        -webkit-backdrop-filter: blur(5px);
        z-index: 1000;
        opacity: 0;
        pointer-events: none;
        transition: opacity 0.3s ease;
    }

    .loader-container.show {
        opacity: 1;
        pointer-events: auto;
    }

    /* Loader Animation */
    .loader {
        width: 50px;
        aspect-ratio: 1;
        display: grid;
        border: 4px solid #0000;
        border-radius: 50%;
        border-color: #ccc #0000;
        animation: l16 1s infinite linear;
        will-change: transform;
    }

    .loader::before,
    .loader::after {    
        content: "";
        grid-area: 1/1;
        margin: 2px;
        border: inherit;
        border-radius: 50%;
    }

    .loader::before {
        border-color: #f03355 #0000;
        animation: inherit; 
        animation-duration: .5s;
        animation-direction: reverse;
    }

    .loader::after {
        margin: 8px;
    }

    @keyframes l16 { 
        100% { transform: rotate(1turn) }
    }

    /* Previous CSS remains the same after this point */
    </style>
    """

# Loader HTML
def get_loader_html() -> str:
    return """
    <div class="loader-container" id="loaderContainer">
        <div class="loader"></div>
    </div>
    <script>
        function showLoader() {
            document.getElementById('loaderContainer').classList.add('show');
        }
        function hideLoader() {
            document.getElementById('loaderContainer').classList.remove('show');
        }
    </script>
    """

# Optimized navigation handler with loading state
def handle_navigation(page_name: str) -> None:
    current_time = time.time()
    if current_time - st.session_state.last_click > 0.3:
        st.session_state.is_loading = True
        st.session_state.page = page_name
        st.session_state.last_click = current_time
        st.session_state.render_id += 1

# Image optimization helper
def optimize_image(image_path: str, max_width: int = 800) -> None:
    return st.image(image_path, use_column_width=True, output_format='AUTO')

def main() -> None:
    # Apply optimized CSS and loader
    st.markdown(get_css(), unsafe_allow_html=True)
    st.markdown(get_loader_html(), unsafe_allow_html=True)
    
    # Show/hide loader based on loading state
    if st.session_state.is_loading:
        st.markdown(
            "<script>showLoader();</script>",
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            "<script>hideLoader();</script>",
            unsafe_allow_html=True
        )
    
    # Navigation bar
    with st.container():
        st.markdown('<div class="navbar-container">', unsafe_allow_html=True)
        cols = st.columns(len(PAGES))
        
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
    
    # Content area with loading state management
    with st.container():
        st.markdown('<div class="content-container">', unsafe_allow_html=True)
        try:
            current_page = st.session_state.page
            page_component = get_page_component(current_page)
            
            if page_component:
                page_component.app()
            else:
                st.error("Page not found")
                get_page_component("About Me").app()
                
        except Exception as e:
            st.error(f"Error loading page: {str(e)}")
            get_page_component("About Me").app()
        finally:
            st.session_state.is_loading = False
            st.markdown(
                "<script>hideLoader();</script>",
                unsafe_allow_html=True
            )
            
        st.markdown('</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()