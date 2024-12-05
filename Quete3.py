import streamlit as st
from streamlit_authenticator import Authenticate
import yaml
from yaml.loader import SafeLoader
import streamlit_authenticator as stauth

with open('config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

# Pre-hashing all plain text passwords once
# stauth.Hasher.hash_passwords(config['credentials'])

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'])





authenticator.login()
if st.session_state['authentication_status']:
    
    menu_option = st.sidebar.selectbox(
        "Sélectionner une option",
        ["Accueil", "Photos"],
        key='menu_selectbox')
    
    if menu_option == "Accueil":
        st.title("Bienvenue sur la page d'accueil")
        st.image("https://www.stylepochoir.fr/medias/images/d3201-logo-football-club-losc-lille-pochoir.jpg")
        authenticator.logout()
    elif menu_option == "Photos":
        st.title("Evolution des 3 derniers Logo du LOSC")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.header("2002")
            st.image("losc1.jpg")

        with col2:
            st.header("2012")
            st.image("losc2.jpg")

        with col3:
            st.header("2018")
            st.image("losc3.jpg")  

elif st.session_state['authentication_status'] is False:
        st.error('Username/password is incorrect')
elif st.session_state['authentication_status'] is None:
        st.warning('Please enter your username and password')
