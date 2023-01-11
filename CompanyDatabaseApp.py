

# main file 

import streamlit as st

st.title("Company Database Platform")

initial = st.sidebar.text_input("Enter company name: ")

if initial is not None:
  st.header(initial)

message = st.text_area("enter stuff: ") 
st.header(message)

