import streamlit as st
import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

st.title("Generative AI Web App")

tab1, tab2 = st.tabs(["Text Generation","Image Generation"])

with tab1:
    prompt = st.text_input("Enter text prompt")
    if st.button("Generate Text"):
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role":"user","content":prompt}]
        )
        st.write(response.choices[0].message.content)

with tab2:
    img_prompt = st.text_input("Enter image prompt")
    if st.button("Generate Image"):
        image = client.images.generate(prompt=img_prompt,n=1,size="512x512")
        st.image(image.data[0].url)
