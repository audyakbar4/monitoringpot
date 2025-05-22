import streamlit as st
import json
import os
import bcrypt

USERS_FILE = "users.json"

def load_users():
    if not os.path.exists(USERS_FILE):
        return {}
    with open(USERS_FILE, "r") as f:
        return json.load(f)

def save_users(users):
    with open(USERS_FILE, "w") as f:
        json.dump(users, f)

def hash_password(password: str) -> str:
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode(), salt)
    return hashed.decode()

def check_password(password: str, hashed: str) -> bool:
    return bcrypt.checkpw(password.encode(), hashed.encode())

def login():
    st.markdown("""
    <div class="login-box">
        <h2>Login</h2>
    """, unsafe_allow_html=True)

    users = load_users()
    username = st.text_input("Username", key="login_username")
    password = st.text_input("Password", type="password", key="login_password")

    if st.button("Login", key="login_btn"):
        if username in users and check_password(password, users[username]):
            st.session_state["logged_in"] = True
            st.session_state["user"] = username
            st.success(f"Welcome back, {username}!")
            st.rerun()
        else:
            st.error("Invalid username or password")

    st.markdown("</div>", unsafe_allow_html=True)


def register():
    st.markdown("""
    <div class="login-box">
        <h2>Register New Account</h2>
    """, unsafe_allow_html=True)

    users = load_users()
    username = st.text_input("Choose a username", key="reg_username")
    password = st.text_input("Choose a password", type="password", key="reg_password")
    password_confirm = st.text_input("Confirm password", type="password", key="reg_confirm")

    if st.button("Register", key="register_btn"):
        if not username or not password:
            st.error("Username and password cannot be empty")
        elif username in users:
            st.error("Username already exists")
        elif password != password_confirm:
            st.error("Passwords do not match")
        else:
            users[username] = hash_password(password)
            save_users(users)
            st.success("Registration successful! You can now login.")
            st.rerun()

    st.markdown("</div>", unsafe_allow_html=True)


def logout():
    if st.button("Logout", key="logout_btn", help="Click to logout"):
        st.session_state["logged_in"] = False
        st.session_state.pop("user", None)
        st.rerun()


def auth_menu():
    if "logged_in" not in st.session_state:
        st.session_state["logged_in"] = False

    if st.session_state["logged_in"]:
        st.markdown(f"✅ Logged in sebagai **{st.session_state.get('user')}**")
        logout()
    else:
        action = st.radio("Choose action", ["Login", "Register"], horizontal=True)
        if action == "Login":
            login()
        else:
            register()
