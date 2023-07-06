import streamlit as st
import clipboard

def replace_spaces_with_emoticons(text):
    emoticon = "🤸🏼🤸🏼"  # You can change the emoticon to anything you like
    return text.replace(" ", emoticon)

st.title("My Beshie")

user_input = st.text_input("Enter your text here beshie:")

if user_input:
    result = replace_spaces_with_emoticons(user_input)
    clipboard.copy(result)  # This will copy the result to your clipboard
    st.write(result)
    st.write("Beshie, the result has been copied to your clipboard.")
