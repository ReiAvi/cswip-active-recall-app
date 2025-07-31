import streamlit as st
from agents.active_recall_agent import generate_active_recall

st.title("CSWIP 3.1 Active Recall Agent (Mock Prototype)")

topic = st.text_input("Enter Topic (e.g., Weld Defects: Porosity):", "Weld Defects: Porosity")
question_count = st.slider("Number of Questions", min_value=1, max_value=20, value=5)
difficulty = st.selectbox("Difficulty Level", ["Beginner", "Intermediate", "Advanced"])

if st.button("Generate Q&A"):
    qas = generate_active_recall(topic, question_count, difficulty)
    for idx, qa in enumerate(qas, 1):
        st.markdown(f"**{qa['question']}**")
        st.markdown(f"<span style='color:green'>{qa['answer']}</span>", unsafe_allow_html=True)
        st.markdown("---")
