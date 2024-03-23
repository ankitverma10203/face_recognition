import streamlit as st

import image
from db import Database


def login():
    picture = st.camera_input("picture", key="loginPic")

    if picture:
        unknown_user_dir = "./unknown_user/"
        unknown_user_name = "unknown_user"
        image.save_image(picture, unknown_user_dir, unknown_user_name)

        is_match, user_id = image.compare_faces_in_directory("./known_user/", unknown_user_dir)

        if is_match:
            db = Database()
            st.write(user_id)
            user_detail = db.get_user_detail(user_id)
            st.write(user_detail)
        else:
            st.error("No Match Found")

        image.delete_image(unknown_user_dir + unknown_user_name)
