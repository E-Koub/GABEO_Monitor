# public/app.py
import streamlit as st
from pathlib import Path
from visualization.layout import render_layout
from vendor.dataHive.core.context import create_context
from vendor.dataHive.router import ROUTES, DEFAULT_ROUTE
import os


route = st.query_params.get("page", DEFAULT_ROUTE)


def fallback():
    st.error("404 - Page not found")

selected_view = ROUTES.get(route, {}).get("view", fallback)
context = create_context()

render_layout(selected_view,context,ROUTES)