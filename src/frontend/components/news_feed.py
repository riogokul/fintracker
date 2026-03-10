"""News feed component for the Streamlit dashboard."""
import streamlit as st


def render_news_feed():
    """Render a live news feed panel."""
    st.subheader("Latest News")
    # TODO: Fetch articles from API and display
    st.info("No news articles loaded yet.")
