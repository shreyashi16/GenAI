import streamlit as st
import numpy as np
import pandas as pd
st.title("Hello, Streamlit !")
st.write(":streamlit: This is your first streamlit app")
st.text("Lets get started")

name = st.text_input("Enter your name: ")
if st.button("submit"):
    st.success(f"Hello,{name}!")

#Displaying data and charts
df = pd.DataFrame(np.random.rand(10,2), columns = ['A','B'])
st.line_chart(df)
st.bar_chart(df)

#media layout and advance widget
st.sidebar.title("Navigation")
st.image("pythonnn.webp")
st.video("https://www.bing.com/videos/riverview/relatedvideo?q=python+tutorial+vedio&&mid=EC71E119D7AEA4A3E4AEEC71E119D7AEA4A3E4AE&churl=https%3a%2f%2fwww.youtube.com%2fchannel%2fUCWv7vMbMWH4-V0ZXdmDpPBA&FORM=VAMGZC")

#file uploading and catching topics
upload_file = st.file_uploader("upload a csv", type='csv')
if upload_file:
    df = pd.read_csv(upload_file)
    st.dataframe(df)

st.title("text and markdown demo")
st.header("this is header")
st.subheader("this is a subheader")
st.markdown("**Bold**, *Italic*, 'code', [Link](https://streamlit.io)")
st.code("fir i in range(5): print(i)", language="python")
st.text_input("What is your name?")
st.text_area("Write something...")
st.number_input("pick a number", min_value = 0, max_value = 100)
st.slider("Choose a range", 0, 100)
st.selectbox("Select a fruit",["Apple","Banana","Mango"])
st.multiselect("Choose toppings",["cheese","Tomato","Olives"])
st.radio("Pick one",["Option A","Option B"])
st.checkbox("I agree to the terms")

if st.checkbox("show details"):
    st.info("Here are more details...")

option = st.radio("Choose view", ["Show Chart","Show Table"])
if option == "Show Chart":
    st.write("Chart would appear here")
else:
    st.write("Table would appear here")

with st.form("login_form"):
    username = st.text_input("username")
    password = st.text_input("Password", type= "password")
    submitted = st.form_submit_button("Login")

if submitted:
    st.success(f"Welcome, {username}!")