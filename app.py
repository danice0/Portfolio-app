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
    menu_items=None  # Disable menu for better performance
)

# Initialize session state with type hints for better performance
if not hasattr(st.session_state, "page"):
    st.session_state.page: str = "About Me"
if not hasattr(st.session_state, "last_click"):
    st.session_state.last_click: float = time.time()
if not hasattr(st.session_state, "render_id"):
    st.session_state.render_id: int = 0

# Cache page components for better performance
@lru_cache(maxsize=None)
def get_page_component(page_name: str):
    return PAGES.get(page_name)

# Define pages with type hints
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
    /* Performance optimizations */
    * {
        text-rendering: optimizeLegibility;
        -webkit-font-smoothing: antialiased;
        -moz-osx-font-smoothing: grayscale;
        box-sizing: border-box;
    }

    /* Root variables with mobile-first approach */
    :root {
        --navbar-height: min(4rem, 10vh);
        --content-padding: clamp(0.5rem, 2vw, 2rem);
        --max-width: min(1200px, 95vw);
        --font-size-base: clamp(14px, 1vw + 8px, 16px);
        --font-size-h1: clamp(24px, 3vw + 16px, 40px);
        --font-size-h2: clamp(20px, 2vw + 14px, 32px);
        --font-size-h3: clamp(16px, 1.5vw + 12px, 24px);
    }

    /* Global performance optimizations */
    .stApp {
        background-color: #121212 !important;
        max-width: 100vw;
        overflow-x: hidden;
        will-change: transform;
        contain: content;
    }

    /* Optimized navbar */
    .navbar-container {
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        z-index: 999;
        background-color: rgba(18, 18, 18, 0.95);
        padding: clamp(0.25rem, 1vw, 0.5rem) var(--content-padding);
        backdrop-filter: blur(8px);
        -webkit-backdrop-filter: blur(8px);
        box-shadow: 0 2px 10px rgba(0, 0, 0, 0.3);
        transform: translateZ(0);
        will-change: transform;
        contain: layout style paint;
    }

    /* Performance-optimized content container */
    .content-container {
        margin: calc(var(--navbar-height) + 1rem) auto 2rem;
        padding: 0 var(--content-padding);
        max-width: var(--max-width);
        width: 100%;
        contain: content;
    }

    /* Optimized button styles */
    .stButton button {
        width: 100%;
        padding: clamp(0.3rem, 1vw, 0.5rem) !important;
        background-color: transparent !important;
        color: white !important;
        font-size: var(--font-size-base) !important;
        white-space: nowrap !important;
        overflow: hidden !important;
        text-overflow: ellipsis !important;
        transform: translateZ(0);
        will-change: transform, background-color;
        transition: transform 0.2s ease, background-color 0.2s ease !important;
    }

    /* Image optimizations */
    img {
        max-width: 100%;
        height: auto;
        contain: content;
        transform: translateZ(0);
    }

    /* Responsive typography */
    .stText, .stMarkdown {
        font-size: var(--font-size-base);
        line-height: 1.5;
    }

    h1 { font-size: var(--font-size-h1) !important; }
    h2 { font-size: var(--font-size-h2) !important; }
    h3 { font-size: var(--font-size-h3) !important; }

    /* Mobile optimizations */
    @media screen and (max-width: 768px) {
        .navbar-container {
            position: sticky;
            padding: 0.25rem;
            height: auto;
            contain: layout style;
        }
        
        .content-container {
            margin-top: 0.5rem;
            padding: 0 0.5rem;
        }
        
        .row-widget.stHorizontal {
            flex-direction: column;
            gap: 0.25rem;
        }
        
        img {
            max-height: 50vh;
            object-fit: contain;
        }
    }

    /* Hide Streamlit components */
    #MainMenu, header, footer { display: none !important; }

    /* Performance optimization for animations */
    @media (prefers-reduced-motion: reduce) {
        * {
            animation: none !important;
            transition: none !important;
        }
    }
    </style>
    """

# Optimized navigation handler with debouncing
def handle_navigation(page_name: str) -> None:
    current_time = time.time()
    if current_time - st.session_state.last_click > 0.3:  # 300ms debounce
        st.session_state.page = page_name
        st.session_state.last_click = current_time
        st.session_state.render_id += 1

# Image optimization helper
def optimize_image(image_path: str, max_width: int = 800) -> None:
    return st.image(image_path, use_column_width=True, output_format='AUTO')

def main() -> None:
    # Apply optimized CSS
    st.markdown(get_css(), unsafe_allow_html=True)
    
    # Optimized navigation bar
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
    
    # Optimized content area with error handling
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
            
        st.markdown('</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()