import streamlit as st
from PIL import Image
from backend.app.multimodal import analyze
st.title("Multimodal AI Research Lab")
st.caption("Research project by Rayyan Anwar")
f=st.file_uploader("Image",type=["png","jpg","jpeg"]); t=st.text_area("Associated text")
if f and st.button("Run Experiment"): st.json(analyze(Image.open(f),t))
