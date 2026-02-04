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
            background: radial-gradient(circle at top, #0B1120, #06080F 60%);
            color: #E2E8F0;
        }

        h1, h2, h3, h4 {
            color: #E2E8F0;
            font-weight: 600;
            letter-spacing: 0.02em;
        }

        p, span, label {
            color: #94A3B8;
        }

        .stButton>button {
            background: linear-gradient(90deg, #38BDF8, #818CF8);
            color: #020617;
            border-radius: 10px;
            padding: 0.6rem 1.4rem;
            border: 1px solid rgba(148, 163, 184, 0.2);
            box-shadow: 0 0 16px rgba(56, 189, 248, 0.4);
        }

        .stButton>button:hover {
            background: linear-gradient(90deg, #67E8F9, #A78BFA);
            box-shadow: 0 0 24px rgba(129, 140, 248, 0.6);
        }

        .card {
            background: rgba(15, 23, 42, 0.7);
            border-radius: 14px;
            padding: 1.25rem;
            border: 1px solid rgba(148, 163, 184, 0.2);
            box-shadow: 0 0 24px rgba(15, 23, 42, 0.6);
            backdrop-filter: blur(12px);
        }

        .muted {
            color: #94A3B8;
            font-size: 0.9rem;
        }

        hr {
            border: 0;
            height: 1px;
            background: linear-gradient(90deg, transparent, #38BDF8, transparent);
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
        }

        .status-ok {
            background: rgba(34, 197, 94, 0.2);
            color: #4ADE80;
            border: 1px solid rgba(74, 222, 128, 0.5);
        }

        .status-warn {
            background: rgba(251, 191, 36, 0.2);
            color: #FCD34D;
            border: 1px solid rgba(251, 191, 36, 0.5);
        }
        </style>
    """, unsafe_allow_html=True)


def section(title, subtitle=None):
    st.markdown(f"## {title}")
    if subtitle:
        st.markdown(f"<p class='muted'>{subtitle}</p>", unsafe_allow_html=True)
    st.markdown("<hr/>", unsafe_allow_html=True)
