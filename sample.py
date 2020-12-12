'''
!/usr/bin/env python
-*-coding:utf-8-*-
@author:shivam_gupta,ayanava_dutta
'''
import streamlit as st
import time
st.title("Sample SignUp UI")


option = st.sidebar.selectbox(
    'Make Your Choice',
     ['Login','StreamLit Documentation'])

if option=='Login':
    name=st.text_input("Enter Your Name",max_chars=20)
    selection = st.radio("Gender",("Male","Female"))
    col1,col2=st.beta_columns(2)
    age=col1.slider("Enter Your Age",max_value=80,min_value=10,value=21)
    dateofbirth=col2.date_input("Date Of Birth")
    password = st.text_input("Enter Your Password",max_chars=18,type='password')

    if len(password)<8:
        st.warning('Password must contain more than 8 characters ')
        st.stop()

    if st.button(label="Submit"):
        st.success("Your form has been submitted Sucessfully")
        st.balloons()
        st.text("You have entered:")
        st.text("Name: "+str(name)+'\n\n'+"Age: "+str(age)+'\n\n'+"Date of Birth: "+str(dateofbirth))
if option=='StreamLit Documentation':
    st.markdown("""<a href="https://docs.streamlit.io/en/stable/">StreamLit Documentation</a>""", unsafe_allow_html=True,)
    
