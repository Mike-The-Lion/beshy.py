import streamlit as st
import emoji

# Create a title
st.title('Space to Emoji Converter')

# Add a text input field to the sidebar
user_input = st.sidebar.text_input("Enter a sentence")

# Add a selectbox to the sidebar
selected_emoji = st.sidebar.selectbox(
    'Select an emoji',
    (':grinning:', ':winking_face:', ':star-struck:', ':thinking_face:', ':face_with_hand_over_mouth:')
)

# Convert the chosen emoji to unicode
unicode_emoji = emoji.emojize(selected_emoji, use_aliases=True)

# Replace spaces with the selected emoji
converted_sentence = user_input.replace(' ', unicode_emoji)

# Write the converted sentence to the main page
st.write(converted_sentence)
