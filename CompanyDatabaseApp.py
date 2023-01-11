

# main file 

import streamlit as st

st.title("Company Database Platform")


# Company Information
st.header("Company Information")

companyName = st.text_input("Company Name: ") 
address = st.text_input("Address: ")
telephone = st.text_input("Telephone: ")
fax = st.text_input("Fax: ")
email = st.text_input("Email Information: ")
contacts = st.text_input("Name/title of contact(s): ")
contactInfo = st.text_input("Please include telephone and email information of contact(s): ")


# Organization
st.header("Organization Information")

history = st.text_input("Please give a brief history of the company:")
entity = st.text_input("Legal entity type: ")
country = st.text_input("Country of legal registration: ")
dom  = st.text_input("Domicile:")
inceptDate = st.text_input("Inception date: ")
background = st.text_area("Please provide a short background of principals (education, career, background, etc.) ")
size = st.text_input("How large is the firm in terms of full and part-time individuals? ")
struct = st.text_area("Describe the firm’s ownership structure, name of its owners, and their percentage ownership: ")
yoe = st.text_input("What are the average years of professional experience in the firm, both years as a professional as well as years in the firm? ")
turnover = st.text_input("What has been the turnover rate among the firm’s personnel? ")
consult = st.text_area("Are outside representatives or consultants used for any activities? If so, give details. ")
branch = st.text_area("Branch offices or other locations, if any. What functions are performed at these branches and locations? ")
regAuth = st.text_area("What regulatory authority is the company registered with? Include: type, date of registration, and whether all of the employees are registered with the same authority? ")
affil = st.text_area("List any affiliations, directorships and memberships of the company and/or its principals: ")

# Upload 
st.write("Please upload an organizational chart or bio with the names of senior managers in charge of the following areas: \n
Finance \n
Legal/Risk Management \n
Marketing \n
Administration")



