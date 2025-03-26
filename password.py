import streamlit as st
import re

def check_strenght(password):
    strenght = 0

    if len(password) >= 8:
        strenght += 20
    
    if re.search(r'[A-Z]', password):
        strenght += 20
    
    if re.search(r'[a-z]', password):
        strenght += 20

    if re.search(r'[0-9]', password):
        strenght += 20 

    if re.search(r'[!@#$%^&]', password):
        strenght += 20

    return strenght 

st.title("Password Strength Meter")

password = st.text_input('Enter The Password')

if password:
    strenght = check_strenght(password)

    if strenght == 0:
        st.warning("Your Password is Easy and Weak")
        st.progress(0)

    elif strenght == 20:
        st.warning("Your password is weak")
        st.progress(20)

    elif strenght == 40:
        st.info("Your password is Fair")
        st.progress(40)

    elif strenght == 60:
        st.info("Your password is Good")
        st.progress(60)

    elif strenght == 80:
        st.info("Your password is very Good")
        st.progress(80)

    elif strenght == 100:
        st.info('Your password is Excellent')
        st.progress(100)
