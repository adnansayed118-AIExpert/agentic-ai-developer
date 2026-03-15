#import streamlit
import streamlit as st

# add tiltle to your group using .title()
st.title("My first Streamlit app created by Sayed Adnan")

#Add some text
st.write("Welcome This App calculate the square of a number.")

#create interactive slider
st.header("select a number")
number = st.slider("pick up a number", 0,100,5)

#calculate and display the result
st.subheader("Result")
squared_number= number * number
st.write(f"The square of **{number}** is **{squared_number}**.")