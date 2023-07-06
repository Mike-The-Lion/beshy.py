import streamlit as st

def replace_spaces_with_emoticons(text):
    emoticon = "🤸🏼🤸🏼"  # You can change the emoticon to anything you like
    return text.replace(" ", emoticon)

st.title("Beshie! 🤸🏼")

user_input = st.text_input("Enter your text here:")

if user_input:
    result = replace_spaces_with_emoticons(user_input)
    st.write(result)
