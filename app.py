import streamlit as st
import pandas as pd
import numpy as np
import time
from datetime import datetime

# ------------------------------------------------------
# إعدادات الصفحة العامة
# ------------------------------------------------------
st.set_page_config(
    page_title="Hello Streamlit",
    page_icon="👋",
    layout="centered"
)

# ------------------------------------------------------
# العنوان الرئيسي
# ------------------------------------------------------
st.title("Hello Streamlit 👋")

# ------------------------------------------------------
# النص المطلوب + عرضه داخل مربع كود
# ------------------------------------------------------
info_text = "If you're reading this text, your app is live!"
st.write(info_text)
st.code(info_text)

st.divider()

# ------------------------------------------------------
# مربع إدخال الاسم
# ------------------------------------------------------
st.subheader("What is your name?")
name = st.text_input("Enter your name here:")

if name:
    st.success(f"🎉 Nice to meet you, {name}! Welcome to your Streamlit app.")

st.divider()

# ------------------------------------------------------
# إضافات إضافية لجعل الموقع أكثر تفاعلاً وتنوعاً
# ------------------------------------------------------

st.header("✨ More Interactive Widgets")

# 1) شريط تمرير (Slider)
st.subheader("🎂 How old are you?")
age = st.slider("Select your age:", min_value=1, max_value=100, value=25)
st.write(f"You are **{age}** years old.")

# 2) قائمة اختيار (Selectbox)
st.subheader("🎨 Favorite color")
color = st.selectbox(
    "Pick your favorite color:",
    ["Red", "Blue", "Green", "Yellow", "Purple", "Black", "White"]
)
st.write(f"Your favorite color is **{color}**.")

# 3) مربعات اختيار متعددة (Checkbox)
st.subheader("🎯 Your hobbies")
hobbies = st.multiselect(
    "Select your hobbies:",
    ["Reading", "Gaming", "Traveling", "Sports", "Coding", "Music", "Cooking"]
)
if hobbies:
    st.write("You selected:", ", ".join(hobbies))

# 4) زر تفاعلي مع تأثير بسيط
st.subheader("🎲 Try your luck")
if st.button("Click me!"):
    with st.spinner("Rolling the dice..."):
        time.sleep(1)
    number = np.random.randint(1, 7)
    st.balloons()
    st.write(f"🎲 You rolled a **{number}**!")

# 5) عرض تاريخ ووقت حالي
st.subheader("🕒 Current date and time")
st.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

# 6) رسم بياني بسيط باستخدام بيانات عشوائية
st.subheader("📊 Random Data Chart")
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=["A", "B", "C"]
)
st.line_chart(chart_data)

# 7) جدول بيانات بسيط
st.subheader("📋 Sample Data Table")
df = pd.DataFrame({
    "Name": ["Ali", "Sara", "Omar", "Lina"],
    "Age": [25, 30, 22, 28],
    "City": ["Cairo", "Riyadh", "Dubai", "Amman"]
})
st.dataframe(df, use_container_width=True)

# 8) شريط جانبي (Sidebar) بمعلومات إضافية
with st.sidebar:
    st.header("ℹ️ About this app")
    st.write("This is a simple demo app built with **Streamlit**.")
    st.write("It includes multiple widgets to demonstrate how easy it is "
             "to build interactive web apps using Python.")
    st.markdown("---")
    st.write("Made with ❤️ using Streamlit")

st.divider()
st.caption("Built with Streamlit 🚀")
