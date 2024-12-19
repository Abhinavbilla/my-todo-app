import streamlit as st
from PIL import Image
with st.expander("Take photo"):
    var = st.camera_input("camera")
if var:
    img = Image.open(var)
    grey_image = img.convert("L")
    st.image(grey_image)