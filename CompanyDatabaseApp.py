

# main file 

import streamlit as st
from PIL import Image

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
st.write("Please upload an organizational chart or bio with the names of senior managers in charge of the following areas: Finance, Legal/Risk Management, Marketing, Administration")

def load_image(image_file):
	img = Image.open(image_file)
	return img

image_file = st.file_uploader("Upload Image", type=["png","jpg","jpeg"])

if image_file is not None:

   # To See details
   filename = image_file.name
   filetype = image_file.type
   filesize = image_file.size
   st.write(filename)

   # To View Uploaded Image
   st.image(load_image(image_file),width=250)


# Complicane
st.header("Compliance Information")

comp = st.text_input("Who is responsible for compliance? ")
coi = st.text_area("Please describe any current or potential conflict of interest: ")
relationAffect = st.text_area("Does the firm or directors have any relationship which may affect its business activities? ")
accountant = st.text_input("Please list your accountant and attorney of the company: ")
accountLoc = st.text_input("Where are the accounts maintained? ")
problems = st.text_area("Is there any material, criminal, civil or administrative proceedings pending or threatened against the firm or any of its principals, or have there ever been any such matters? If yes, please provide full details: ")
otherInv = st.text_area("Do any of the firm’s principles have other business involvement? If yes, describe and quantify how much of their professional time is dedicated to each. ")
CRF = st.selectbox("Is your company looking to be included in the Caribbean Resilience Fund (CRF)? ", ['Yes','No'])
													 
if CRF is 'Yes':
	st.write(CRF)
													 




