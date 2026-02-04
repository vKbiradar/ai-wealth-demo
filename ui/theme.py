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
            font-family: 'Inter', 'Space Grotesk', -apple-system, BlinkMacSystemFont;
        }

        body {
            background-color: #030712;
            color: #E2F5FF;
        }

        .stApp {
            background-color: #030712;
            background-image:
                radial-gradient(circle at top, rgba(0, 229, 255, 0.22), transparent 55%),
                radial-gradient(circle at 20% 20%, rgba(59, 130, 246, 0.18), transparent 45%),
                linear-gradient(120deg, rgba(0, 229, 255, 0.12), transparent 40%),
                repeating-linear-gradient(90deg, rgba(0, 229, 255, 0.1) 0, rgba(0, 229, 255, 0.1) 1px, transparent 1px, transparent 80px),
                repeating-linear-gradient(0deg, rgba(0, 229, 255, 0.08) 0, rgba(0, 229, 255, 0.08) 1px, transparent 1px, transparent 80px);
            background-attachment: fixed;
            animation: gridPulse 18s ease-in-out infinite;
        }

        @keyframes gridPulse {
            0% {
                background-position: 0 0, 0 0, 0 0, 0 0, 0 0;
            }
            50% {
                background-position: 0 40px, -40px 0, 20px 10px, 0 0, 0 0;
            }
            100% {
                background-position: 0 0, 0 0, 0 0, 0 0, 0 0;
            }
        }

        h1, h2, h3, h4 {
            color: #E6FBFF;
            font-weight: 600;
            letter-spacing: 0.03em;
            text-shadow: 0 0 6px rgba(0, 229, 255, 0.25);
        }

        p, span, label {
            color: #A7C8D9;
        }

        .stButton>button {
            background: linear-gradient(90deg, #00F0FF, #1D8CF8);
            color: #00101A;
            border-radius: 10px;
            padding: 0.6rem 1.4rem;
            border: 1px solid rgba(0, 229, 255, 0.6);
            box-shadow: 0 0 22px rgba(0, 229, 255, 0.6);
        }

        .stButton>button:hover {
            background: linear-gradient(90deg, #7FFBFF, #38BDF8);
            box-shadow: 0 0 30px rgba(0, 229, 255, 0.8);
        }

        .card {
            background: rgba(5, 10, 20, 0.96);
            border-radius: 14px;
            padding: 1.25rem;
            border: 1px solid rgba(0, 229, 255, 0.35);
            box-shadow: 0 0 32px rgba(0, 229, 255, 0.2);
        }

        .muted {
            color: #8BB7CC;
            font-size: 0.9rem;
        }

        hr {
            border: 0;
            height: 1px;
            background: linear-gradient(90deg, transparent, #00F0FF, transparent);
            margin: 1rem 0 1.5rem 0;
        }

        .status-chip {
            display: inline-flex;
            align-items: center;
            gap: 0.35rem;
            padding: 0.25rem 0.75rem;
            border-radius: 999px;
            font-size: 0.85rem;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 0.08em;
            box-shadow: 0 0 12px rgba(0, 229, 255, 0.25);
        }

        .status-ok {
            background: rgba(0, 229, 255, 0.2);
            color: #7FFBFF;
            border: 1px solid rgba(0, 229, 255, 0.6);
        }

        .status-warn {
            background: rgba(56, 189, 248, 0.15);
            color: #60A5FA;
            border: 1px solid rgba(56, 189, 248, 0.5);
        }

        .stSlider [data-baseweb="track"] {
            background: rgba(0, 229, 255, 0.25);
        }

        .stSlider [data-baseweb="thumb"] {
            background-color: #00F0FF;
            box-shadow: 0 0 12px rgba(0, 229, 255, 0.8);
        }

        .live-button {
            display: inline-flex;
            align-items: center;
            justify-content: center;
            width: 100%;
            padding: 0.75rem 1rem;
            border-radius: 12px;
            text-decoration: none;
            color: #00101A;
            font-weight: 600;
            letter-spacing: 0.04em;
            background: linear-gradient(120deg, #00F0FF, #1D8CF8);
            border: 1px solid rgba(0, 229, 255, 0.55);
            box-shadow: 0 0 22px rgba(0, 229, 255, 0.45);
            transition: transform 0.2s ease, box-shadow 0.2s ease;
        }

        .live-button:hover {
            transform: translateY(-2px);
            box-shadow: 0 0 30px rgba(0, 229, 255, 0.7);
        }
        </style>
    """, unsafe_allow_html=True)


def section(title, subtitle=None):
    st.markdown(f"## {title}")
    if subtitle:
        st.markdown(f"<p class='muted'>{subtitle}</p>", unsafe_allow_html=True)
    st.markdown("<hr/>", unsafe_allow_html=True)
