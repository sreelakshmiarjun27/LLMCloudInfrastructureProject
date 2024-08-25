import streamlit as st
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

# User input for chatbot
user_question = st.text_input("What would you like to know about cloud computing?")

# Ask button for chatbot
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

# Cloud Cost Calculator
st.markdown("### Cloud Cost Estimator")
service_type = st.selectbox("Select the cloud service type:", ["Compute", "Storage", "Data Transfer"])
usage_hours = st.number_input("Enter usage hours (per month):", min_value=0)
data_transfer_gb = st.number_input("Enter data transfer (GB per month):", min_value=0)

# Adjusted Pricing (Example prices in pounds)
pricing = {
    "Compute": 0.04,  # Price per hour in pounds
    "Storage": 0.014,  # Price per GB in pounds
    "Data Transfer": 0.018  # Price per GB in pounds
}

# Calculate button
if st.button("Calculate Cost"):
    if usage_hours or data_transfer_gb:
        total_cost = 0
        if service_type == "Compute":
            total_cost = usage_hours * pricing["Compute"]
        elif service_type == "Storage":
            total_cost = data_transfer_gb * pricing["Storage"]
        elif service_type == "Data Transfer":
            total_cost = data_transfer_gb * pricing["Data Transfer"]
        
        st.success(f"Estimated Cost for {service_type} service: £{total_cost:.2f} per month")
    else:
        st.warning("Please enter usage hours or data transfer amount.")

# Rating button
rating = st.slider("Rate your experience:", 1, 5, 3)
if st.button("Submit Rating"):
    st.success(f"Thank you for your rating of {rating} stars!")

# Animated elements (using st.balloons() as an example)
if st.button("Feeling happy? Click for a surprise!"):
    st.balloons()