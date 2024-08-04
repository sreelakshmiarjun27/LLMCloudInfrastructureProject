import streamlit as st
from PIL import Image
import io
from app import get_answer, preprocess_text

# Streamlit app
st.set_page_config(page_title="Cloud Chatbot", page_icon="☁️", layout="wide")

# Custom CSS for better styling
st.markdown("""
    <style>
    .main {
        background-color: #f0f8ff;
    }
    .stTextInput > div > div > input {
        background-color: #ffffff;
    }
    .stButton > button {
        background-color: #4682b4;
        color: white;
    }
    .answer-box {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    </style>
    """, unsafe_allow_html=True)

# Title and welcome message
st.title("☁️ Cloud Chatbot")
st.markdown("### Welcome! I'm your friendly cloud chatbot, here to assist you with cloud infrastructure details.")

# User input
user_question = st.text_input("What would you like to know about cloud computing?")

# Ask button
if st.button("Ask"):
    if user_question:
        answer, relevant_chunk = get_answer(user_question)
        
        st.markdown("### Answer:")
        st.markdown(f'<div class="answer-box">{answer}</div>', unsafe_allow_html=True)
        
        if relevant_chunk:
            st.write("### Most Relevant Context:")
            st.info(relevant_chunk[:500] + "..." if len(relevant_chunk) > 500 else relevant_chunk)
        
        # Show NLP analysis
        st.write("### NLP Analysis:")
        preprocessed_question = preprocess_text(user_question)
        st.write(f"Preprocessed question: {preprocessed_question}")
    else:
        st.warning("Please enter a question before clicking Ask.")

# File uploader for images and PDFs
uploaded_file = st.file_uploader("Upload an image or PDF related to your question", type=["jpg", "jpeg", "png", "pdf"])

if uploaded_file is not None:
    if uploaded_file.type.startswith('image'):
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Image', use_column_width=True)
    elif uploaded_file.type == 'application/pdf':
        st.success(f"PDF file '{uploaded_file.name}' uploaded successfully!")

# Rating button
rating = st.slider("Rate your experience:", 1, 5, 3)
if st.button("Submit Rating"):
    st.success(f"Thank you for your rating of {rating} stars!")

# Animated elements (using st.balloons() as an example)
if st.button("Feeling happy? Click for a surprise!"):
    st.balloons()