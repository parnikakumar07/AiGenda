import streamlit as st
import os
from PIL import Image
import google.generativeai as genai

genai.configure(api_key="AIzaSyDorXvA2hghyDMM0p7WG8vgTmaXNeuyNTU")

model=genai.GenerativeModel('gemini-1.5-flash')

def get_genai_response(input_text,image_data,promt):
    response = model.generate_content([input_text,image_data[0],promt])
def input_image_details(uploaded_files):
    return response.text

def input_image_details(uploaded_file):
    if uploaded_file is not None:
        bytes_data=uploaded_file.getvalue()
        image_parts=[
            {
                "mime_type":uploaded_file.type,
                "data":bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("no file uploaded")

st.title("Invoice Geneator")
st.sidebar.header("R0boBill")
st.sidebar.write("Made by Pari")
st.sidebar.write("Powered by Google Gemini AI ")
st.header("R0bobill")
st.subheader("Made by Parnika")
st.subheader("Manage your expenses with R0bobill")
input= st.text_input("What do ya want me to do?",key="input")
uploaded_file = st.file_uploader("Choose an image",type=["jpg","jpeg","png"])
image = ""
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image,caption="Uploaded Image",use_column_width=True)

ssubmit=st.button("Lets Go!")

input_promt = """
You are an expert in reading invoices.We are going to upload an image of an invoice and you will have to answer any types of questions that the user asks you.
You have to greet first.
Make sure to keep the fonts uniform and give the items list in point-wise format.
At the end make sure to repeat the name of our app "R0bobill" and ask the user to use it again.
"""
if ssubmit:
    image_data = input_image_details(uploaded_file)
    response = get_genai_response(input_promt,image_data,input)
    st.subheader("Here's what you have to know")
    st.write(response)
    
    
