import sys
import os
import streamlit as st
from streamlit_folium import st_folium

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))


def show(context):
    return ''