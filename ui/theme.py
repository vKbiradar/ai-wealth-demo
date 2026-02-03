import streamlit as st

def set_theme():
    st.set_page_config(
        page_title="AI Wealth",
        layout="wide",
        initial_sidebar_state="collapsed"
    )

    st.markdown("""
        <style>
        html, body, [class*="css"] {
            font-family: 'Inter', -apple-system, BlinkMacSystemFont;
        }

        body {
            background-color: #F8FAFC;
        }

        h1, h2, h3 {
            color: #0F172A;
            font-weight: 600;
        }

        p, span, label {
            color: #475569;
        }

        .stButton>button {
            background-color: #1D4ED8;
            color: white;
            border-radius: 8px;
            padding: 0.6rem 1.2rem;
            border: none;
        }

        .stButton>button:hover {
            background-color: #1E40AF;
        }

        .card {
            background: white;
            border-radius: 12px;
            padding: 1.25rem;
            border: 1px solid #E5E7EB;
        }

        .muted {
            color: #64748B;
            font-size: 0.9rem;
        }
        </style>
    """, unsafe_allow_html=True)


def section(title, subtitle=None):
    st.markdown(f"## {title}")
    if subtitle:
        st.markdown(f"<p class='muted'>{subtitle}</p>", unsafe_allow_html=True)
    st.markdown("<hr/>", unsafe_allow_html=True)

