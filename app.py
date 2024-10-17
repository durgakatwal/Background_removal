
import streamlit as st
from rembg import remove
from PIL import Image
import io

st.title('Background Remover')

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    input_image = uploaded_file.read()
    output_image = remove(input_image)

    st.image(output_image, caption='Output Image', use_column_width=True)

    st.download_button(label="Download Image", data=output_image, file_name="output.png")
