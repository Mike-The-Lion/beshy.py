import streamlit as st
from streamlit import cli as stcli
import streamlit.components.v1 as components
import argparse
import sys

def main():
    st.title('Beshie! 🤸🏼🤸🏼🤸🏼')
    
    user_input = st.text_input("Input your text here:")

    # Define the emoticon you want to replace spaces with
    emoticon = "🤸🏼"

    # Replace spaces in the input string with the emoticon
    output_text = user_input.replace(" ", emoticon)

    st.write(output_text)

    # Create a button for the user to copy the output text
    copy_button = components.html("""
        <button class="copy-button" data-clipboard-text="{}">
            Copy to clipboard
        </button>
        <script>
        new ClipboardJS('.copy-button');
        </script>
        """.format(output_text))

    if copy_button:
        st.write('Text copied to clipboard!')

if __name__ == "__main__":
    if st._is_running_with_streamlit:
        main()
    else:
        sys.argv = ["streamlit", "run", sys.argv[0]]
        sys.exit(stcli.main())
