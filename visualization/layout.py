# visualization/layout.py
import streamlit as st

def render_layout(content_function, context,ROUTES):
    with st.sidebar:
        st.title("🧭 Navigation")

        for key, info in ROUTES.items():
            label = info.get("label", key)
            if st.button(label):
                st.query_params.update(page=key)
                st.rerun()

    content_function(context)
