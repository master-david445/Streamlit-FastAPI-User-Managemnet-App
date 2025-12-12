import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"

st.title("Streamlit FastAPI User Management Demo")
st.subheader("Manage users with FastAPI backend")

#---Function to send data to the API---
def create_user(name: str):
    """Send a POST request to the FastAPI /users endpoint to create a new user."""
    st.info(f"Creating user with name: {name}")

    # 1. Define the data payload (most matched the Pydantric model)
    payload = {"name": name}

    try: 
        # 2. Make the POST request to the API
        response = requests.post(f"{API_URL}/users", json=payload)

        if response.status_code == 200:
            st.success("User created successfully!")
            st.json(response.json())
        else:
            st.error(f"Failed to create user. Status code: {response.status_code}")
            st.json(response.json())

    except requests.exceptions.RequestException as e:   
        st.error(f"An error occurred: Is the server running? {e}")


#--- Streamlit Form ---
st.header("Create a new user")

with st.form("user_form"):
    new_user_name = st.text_input("Name")
    submitted = st.form_submit_button("Create User")

    if submitted and new_user_name:
        create_user(new_user_name)


#--- Display Existing Users ---
st.header("Existing Users from FastAPI")
if st.button("Refresh User List"):
  with st.spinner("Fetching users..."):
    try:
        response = requests.get(f"{API_URL}/users")
        if response.status_code == 200:
            users = response.json()
            st.success("Fetched users successfully!")
            st.json(users)
        else:
            st.error(f"Failed to fetch users. Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        st.error(f"An error occurred: Is the server running? {e}")