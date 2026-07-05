import streamlit as st
import pandas as pd
import numpy as np
import time
from datetime import datetime
st.set_page_config(
    page_title="Hello Streamlit",
    layout="centered"
)

st.title("Hello Streamlit ")

info_text = "If you're reading this text, your app is live!"
st.write(info_text)
st.code(info_text)

st.divider()

st.subheader("What is your name?")
name = st.text_input("Enter your name here:")

if name:
    st.success(f" Nice to meet you, {name}! Welcome to your Streamlit app.")

st.divider()

st.subheader(" How old are you?")
age = st.slider("Select your age:", min_value=1, max_value=100, value=25)
st.write(f"You are **{age}** years old.")

st.subheader(" Favorite color")
color = st.selectbox(
    "Pick your favorite color:",
    ["Red", "Blue", "Green", "Yellow", "Purple", "Black", "White"]
)
st.write(f"Your favorite color is **{color}**.")
st.subheader(" Your hobbies")
hobbies = st.multiselect(
    "Select your hobbies:",
    ["Reading", "Gaming", "Traveling", "Sports", "Coding", "Music", "Cooking"]
)
if hobbies:
    st.write("You selected:", ", ".join(hobbies))

st.subheader(" Try your luck")
if st.button("Click me!"):
    with st.spinner("Rolling the dice..."):
        time.sleep(1)
    number = np.random.randint(1, 7)
    st.balloons()
    st.write(f" You rolled a **{number}**!")

st.subheader(" Current date and time")
st.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

st.subheader(" Random Data Chart")
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=["A", "B", "C"]
)
st.line_chart(chart_data)
st.subheader(" Sample Data Table")
df = pd.DataFrame({
    "Name": ["Ali", "Sara", "Omar", "Lina"],
    "Age": [25, 30, 22, 28],
    "City": ["Cairo", "Riyadh", "Dubai", "Amman"]
})
st.dataframe(df, use_container_width=True)
with st.sidebar:
  
