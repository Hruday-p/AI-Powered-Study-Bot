import streamlit as st
import google.generativeai as genai
import time


genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
model = genai.GenerativeModel("gemini-2.5-flash")

st.set_page_config(page_title="AI-Powered Study Bot", page_icon="🤖", layout="centered")


st.markdown("""
<style>
* { font-family: 'Poppins', sans-serif; }
body { background: linear-gradient(135deg, #e9e9ff, #faf8ff, #fdf3ff); }
header, .header { text-align: center; margin-bottom: 25px; }
.header h1 { font-size: 2.5rem; color: #6c63ff; margin-bottom: 5px; }
.header p { color: #555; font-size: 1.1rem; margin-top: 0; }
textarea, .stTextArea textarea {
    border-radius: 12px !important;
    border: 2px solid #ddd !important;
    font-size: 1rem !important;
}
footer { text-align: center; color: #777; margin-top: 40px; font-size: 0.9rem; }
div.stButton > button {
    background: linear-gradient(135deg, #6c63ff, #8f7cff);
    color: white;
    border: none;
    padding: 10px 20px;
    border-radius: 10px;
    font-weight: 600;
    cursor: pointer;
    transition: 0.2s ease;
}
div.stButton > button:hover {
    transform: translateY(-2px);
    background: linear-gradient(135deg, #7b72ff, #a28aff);
}
</style>
""", unsafe_allow_html=True)


st.markdown("""
<div class='header'>
    <h1>🤖 AI-powered  Study Bot</h1>
    <p>Your Intelligent Study Companion</p>
</div>
""", unsafe_allow_html=True)


notes = st.text_area("Enter or paste your study notes:", height=200, placeholder="Type or paste your notes here...")

col1, col2, col3 = st.columns(3)
result_placeholder = st.empty()


def generate_response(action, notes):
    if not notes.strip():
        return "⚠️ Please enter some notes first."

    if action == "Key Points":
        prompt = f"Summarize the following study notes in a few key bullet points:\n\n{notes}"
    elif action == "Summarize":
        prompt = f"Explain the key concepts in the following notes as if I am a complete beginner:\n\n{notes}"
    elif action == "Generate Quiz":
        prompt = f"Create a short 5-question multiple-choice quiz based on these notes. Provide the questions and correct answers:\n\n{notes}"
    else:
        prompt = notes

    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"❌ Error: {str(e)}"
    
with col1:
    if st.button("✨ Key Points", use_container_width=True):
        with st.spinner("Generating Key Points..."):
            time.sleep(1)
            output = generate_response("Key Points", notes)
            result_placeholder.success(output)

with col2:
    if st.button("🧠 Summarize", use_container_width=True):
        with st.spinner("Summarizing..."):
            time.sleep(1)
            output = generate_response("Summarize", notes)
            result_placeholder.info(output)

with col3:
    if st.button("🎯 Generate Quiz", use_container_width=True):
        with st.spinner("Generating Quiz..."):
            time.sleep(1)
            output = generate_response("Generate Quiz", notes)
            result_placeholder.warning(output)

st.markdown("<footer>Study Bot can make mistakes. Re-check the notes again</footer>", unsafe_allow_html=True)
