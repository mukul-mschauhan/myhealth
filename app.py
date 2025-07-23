from dotenv import load_dotenv
load_dotenv()
import streamlit as st
import os
import pandas as pd
import google.generativeai as genai

# Configure the key
genai.configure(api_key=os.getenv("GOOGLE-API-KEY"))

# Front End
st.sidebar.subheader("BMI Calculator")
weight = st.sidebar.text_input("Weight (in Kgs):")
height = st.sidebar.text_input("Height (in cms):")

# BMI Calculator
st.sidebar.markdown("The BMI is: ") # BMI = weight/(height/100)**2
weight_num = pd.to_numeric(weight)
height_num = pd.to_numeric(height)
heights = height_num/100
bmi = weight_num/(heights)**2
st.sidebar.write(bmi)

notes = f'''The BMI value can be interpreted as:
* Underweight: BMI<18.5
* Normal Weight: BMI 18.5 - 24.9
* Overweight: BMI 25 - 29.9
* Obese: BMI > 30'''

st.sidebar.write(notes)

# Front End - Right Hand Side
st.header(":red[MyHealtify]-You", divider="blue")
input = st.text_input("Hi! I am your medical expert 💊. Ask me information about Health, Diseases & Fitness Only")

def guide_me_on(input):
    model = genai.GenerativeModel("gemini-2.5-pro")
    if input!="":
        prompt = f'''Act as a Dietician, Health Coach and Expert and 
        address the queries, questions, apprehensions related to health,
        fitness, mental fitness, diseases and things associated with empathy towards the user. 
        Any query or question that is not related to health
        should pass the following message - "I am a Healthcare Expert and I 
        can answer questions related to Health, Fitness and Diet Only".
        If someone asks about medicine for any ailment, 
        just pass the message - "I am an AI Model and cannot answer questions
        related to diagnosis and medicines. Please reach out to your doctor for consulation"
        Note: Add Emojis to give personalized touch in the response.'''

        response = model.generate_content(prompt+input)
        return(response.text)
    else:
        return(st.write("Please write the Prompt"))
    
submit = st.button("Submit")
if submit:
    response = guide_me_on(input)
    st.subheader(":blue[Response]")
    st.write(response)




