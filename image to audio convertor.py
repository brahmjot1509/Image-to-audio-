import easyocr as ocr  #OCR
import streamlit as st  #Web App
from PIL import Image #Image Processing
import numpy as np #Image Processing 
from gtts import gTTS
import pytesseract 
import os
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
st. markdown("<h1 style='text-align: center;'>IMAGE TO AUDIO CONVERTOR</h1>", unsafe_allow_html=True)
st.markdown("")

#image uploader
image = st.file_uploader(label = "Upload your image here",type=['png','jpg','jpeg'])

@st.cache
def load_model(): 
    reader = ocr.Reader(['en'],model_storage_directory='.')
    return reader 

reader = load_model() #load model

if image is not None:

    input_image = Image.open(image) #read image
    st.image(input_image) #display image
    st.success("Here you go!")
    st.header("The text is: ")
    

    with st.spinner(" Processing the Image "):
        result =pytesseract.image_to_string(input_image)
        st.write(result)
 
    st.header(f" Press the button to convert into audio File: ")
 
    tts= gTTS(text=result,slow=False)
    tts.save("audio1.mp3")
           
    if st.button("convert"):
        audio_file = open("audio1.mp3", "rb")
        audio_bytes = audio_file.read()
        st.markdown(f"Your audio:")
        st.audio(audio_bytes, format="audio/mp3", start_time=0)
        # output_text = text_to_speech(text)
        
        st.balloons()
    else:
        st.write("Upload an Image")
#audio 
    