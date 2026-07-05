import streamlit as st
import pandas as pd
import os

st.set_page_config(
    page_title="Hello Streamlit",
    layout="centered"
)

st.title("Hello Streamlit")

st.divider()

st.subheader("What is your name?")
name = st.text_input("Enter your name here:")

st.subheader("How old are you?")
age = st.slider("Select your age:", min_value=1, max_value=100, value=25)

agree = st.checkbox("I accept the terms")

flavor = st.selectbox(
    "Pick one",
    ["Vanilla", "Mango", "Mint"]
)

if os.path.exists("data.csv"):
    df = pd.read_csv("data.csv")
else:
    df = pd.DataFrame(columns=["Name", "Age", "Agree", "Flavor"])

if st.button("Submit"):
    if name.strip():
        new_row = pd.DataFrame([{
            "Name": name,
            "Age": age,
            "Agree": agree,
            "Flavor": flavor
        }])

        df = pd.concat([df, new_row], ignore_index=True)
        df.to_csv("data.csv", index=False)

        st.success(f"Saved! {len(df)} total")
    else:
        st.warning("Please enter your name.")

st.dataframe(df, use_container_width=True)
