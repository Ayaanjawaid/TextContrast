import streamlit as st
from difflib import Differ


st.set_page_config(
    page_title="TextContrast", 
    page_icon="🔍",  
)

def compare_texts(text1, text2):
    d = Differ()
    diff = list(d.compare(text1.splitlines(), text2.splitlines()))
    return '\n'.join(diff)

st.title("TextContrast: Text Comparison Tool")
st.write("This tool compares two texts and highlights the differences.")

text1 = st.text_area("Enter the first text:", height=200)
text2 = st.text_area("Enter the second text:", height=200)

if st.button("Compare"):
    if text1 and text2:
        differences = compare_texts(text1, text2)
        st.subheader("Differences:")
        st.code(differences, language="diff")
    else:
        st.warning("Please enter text in both fields to compare.")
