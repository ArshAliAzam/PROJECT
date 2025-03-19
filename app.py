import streamlit as st
# st.markdown("### <h3 style='color:blue;'>CONVERTER♾️</h3>", unsafe_allow_html=True)
st.markdown("""
    <h2 style="background: linear-gradient(to right, red, orange, yellow, green, blue, indigo, violet);
               -webkit-background-clip: text;
               color: transparent;
               font-weight: bold;">
        This is CONVERTOR!
    </h2>
    """, unsafe_allow_html=True)

import streamlit as st

st.markdown("""
    <style>
    .stApp {
        background-image: url("https://images.unsplash.com/photo-1507525428034-b723cf961d3e");
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🗺️Unit Convertor App♾️!!")
st.markdown("### convert lenght, weight And time Instantly")
st.write("welcome select a category, enter a value and get the converted result in real_time")

category = st.selectbox("Select a Category", ["length", "weight", "time"])

def convert_units(category, value, unit):
  if category == "length":
    if unit == "kilometer to miles":
      return value * 0.621371
    elif unit == "miles to kilometer":
      return value / 1.60934

  elif category == "weight":
    if unit == "kilogram to pound":
      return value * 2.20462
    elif unit == "pound to kilogram":
      return value / 2.20462

  elif category == "time":
    if unit == "seconds to minutes":
      return value /60
    elif unit == "minutes to seconds":
      return value * 60
    elif unit == "hours to minutes":
      return value * 60
    elif unit == "minutes to hours":
      return value / 60
    elif unit == "days to hours":
      return value * 24
    elif unit == "hours to days":
      return value / 24

if category == "length":
  unit = st.selectbox("📏Select a Conversation", ["kilometer to miles", "miles to kilometer"])

elif category == "weight":
  unit = st.selectbox("⚖️Select a Conversation", ["kilogram to pound", "pound to kilogram"])

elif category == "time":
  unit = st.selectbox("⏳Select a Conversation", ["seconds to minutes", "minutes to seconds", "hours to minutes", "minutes to hours", "days to hours", "hours to days"])

value = st.number_input("Enter the value to convert")

if st.button("Convert"):
  result = convert_units(category, value, unit)
  st.success(f"The result is {result:.2f}")
  st.balloons()
