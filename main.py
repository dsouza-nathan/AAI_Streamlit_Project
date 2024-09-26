import streamlit as st

st.title('Hello World')
st.subheader('This is my first website')

#take input from user in streamlit
name = st.text_input('Enter your name')

#display the input
st.write('Hello ',name)

# take math marks as input in slider and display it with name of the student
maths = st.slider('Enter your math marks :',0,100)
st.write(name,'scored',maths,'marks in maths')

#give radio button to choose either from GRE or GMAT
exam = st.radio('Choose an exam :',['GRE','GMAT'])
st.write('You Chose :',exam)

# give checkbox to choose the subjects and display the elected subjects
subjects = st.multiselect(
    'Choose your subject :',['Math','Science','English','History'])
st.write('You Chose :',subjects)

import numpy as np
import pandas as pd
uploaded_file = st.file_uploader('Choose a file :',type = 'xlsx')

if uploaded_file is not None:
    df = pd.read_excel(uploaded_file)
    st.dataframe(df)