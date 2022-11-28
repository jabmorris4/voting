import streamlit as st
import pandas as pd
import numpy as np

st.title('To be President')
st.text("Need 269 electoral votes from 538 votes)")
df = pd.read_csv('Dashboard.csv')
primaryColor="#4287f5"
backgroundColor="#4287f5"
secondaryBackgroundColor="#4287f5"
textColor="#4287f5"
font="sans serif"

st.write('Data Source: https://github.com/cs109/content/blob/master/HW2_solutions.ipynb')
if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(df)
    

st.sidebar.header('Vote')

st.subheader('State Voter Facts')
st.write('33 states have early voting')
st.write('3 states conduct all elections by mail')
st.write('20 states require excuse to vote absentee ballot mail')
         
st.sidebar.header('Electoral')
st.sidebar.header('2012 Prediction')
st.sidebar.header('2012 Poll')
st.sidebar.header('Summary')

state=df['State']
state_val = st.sidebar.selectbox('Please select a state', sorted(state))

max_word = st.sidebar.slider("Max States",min_value=1,max_value=51,value=51, step=10)
max_font = st.sidebar.slider("Electoral Votes",min_value=3,max_value=55,value=51, step=10)
img_width = st.sidebar.slider("Party: 1 for voting Democrat, 0 for voting Republican",min_value=0,max_value=1,value=51, step=10)

random = st.sidebar.slider("Gallop Results: 1 for voting Democrat, 0 for voting Republican", min_value=0,max_value=1,value=51)
# Remove whitespace from the top of the page
st.markdown("""
        <style>
               .css-18e3th9 {
                    padding-top: 0rem;
                    padding-bottom: 10rem;
                    padding-left: 5rem;
                    padding-right: 5rem;
                }
               .css-1d391kg {
                    padding-top: 3.5rem;
                    padding-right: 1rem;
                    padding-bottom: 3.5rem;
                    padding-left: 1rem;
                }
        </style>
        """, unsafe_allow_html=True)

DATA_URL = ('https://github.com/cs109/content/blob/master/HW2_solutions.ipynb')

