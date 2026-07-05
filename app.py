import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Hello Streamlit",
    layout="centered"
)

st.title("Hello Streamlit")

st.divider()

st.subheader("What is your name?")
name = st.text_input("Enter your name here:")

if name:
    st.success(f"Nice to meet you, {name}! Welcome to your Streamlit app.")

st.divider()

st.subheader("How old are you?")
age = st.slider("Select your age:", min_value=1, max_value=100, value=25)
st.write(f"You are **{age}** years old.")

agree = st.checkbox("I accept the terms")

flavor = st.selectbox(
    "Pick one",
    ["Vanilla", "Mango", "Mint"]
)


if "df" not in st.session_state:
    st.session_state.df = pd.DataFrame(
        columns=["Name", "Age", "Agree", "Flavor"]
    )

if st.button("Submit"):
    new_row = pd.DataFrame([{
        "Name": name,
        "Age": age,
        "Agree": agree,
        "Flavor": flavor
    }])

    st.session_state.df = pd.concat(
        [st.session_state.df, new_row],
        ignore_index=True
    )

    st.success(f"Saved! {len(st.session_state.df)} total")

st.dataframe(st.session_state.df, use_container_width=True)
