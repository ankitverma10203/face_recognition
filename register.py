import streamlit as st
import face_recognition as fr
from UserDetail import UserDetail
from db import Database

import image


def register():
    picture = st.camera_input("picture")

    if picture:
        form = st.form("Register")
        name = form.text_input("Username")
        dob = form.date_input("DOB")
        city = form.text_input("City")
        submit = form.form_submit_button("submit")
        if submit:
            if not name or not dob or not city:
                st.error("Please enter your name, DOB and city")
            else:
                st.success("registered successfully")
                user_id = insert_user_detail(city, dob, name)
                know_user_dir = "./known_user/"
                image.save_image(picture, know_user_dir, str(user_id))


def insert_user_detail(city, dob, name):
    user_detail = UserDetail(name, dob, city)
    db = Database()
    user_id = db.insert_user_detail(user_detail)
    return user_id




