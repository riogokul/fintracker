"""Streamlit frontend application."""
import streamlit as st
from components.news_feed import render_news_feed
from components.summary_viewer import render_summary_viewer

st.set_page_config(page_title="Financial News Summarizer", layout="wide")
st.title("Financial News Summarizer")

# Sidebar filters
st.sidebar.header("Filters")
date_range = st.sidebar.date_input("Date Range")
sectors = st.sidebar.multiselect(
    "Sectors",
    options=["Technology", "Finance", "Energy", "Healthcare", "Consumer"],
)

col1, col2 = st.columns([2, 1])

with col1:
    render_summary_viewer()

with col2:
    st.subheader("Top Movers")
    # TODO: Add sentiment chart

st.subheader("Live News Stream")
render_news_feed()
