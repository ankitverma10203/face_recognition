import streamlit as st
import face_recognition as fr
import home
import register
import login

homeTab, registerTab, loginTab = st.tabs(["Home", "Register", "Login"])


# with homeTab:

with registerTab:
    register.register()
with loginTab:
    login.login()