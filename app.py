import streamlit as st
import random

st.set_page_config(page_title="PETRUX AI", page_icon="🤖", layout="centered")

st.markdown("""
<style>
    .main-title {
        text-align: center;
        font-size: 3rem;
        font-weight: 700;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    .sub-title {
        text-align: center;
        font-size: 1.2rem;
        color: #666;
    }
    .footer {
        text-align: center;
        padding: 2rem 0;
        color: #888;
    }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title">🤖 PETRUX AI</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">🖥️ Running on PETRUX OS</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">Built by Peter Eniola Ayanniyi</div>', unsafe_allow_html=True)
st.markdown("---")

with st.sidebar:
    st.markdown("### 🌟 About PETRU")
    st.markdown("**PETRU** is your AI assistant on **PETRUX OS**.")
    st.markdown("💡 Built by: **Peter Eniola Ayanniyi**")
    st.markdown("🎯 Mission: Africa's AI Future")
    st.markdown("---")
    st.markdown("### 📊 Status")
    st.markdown("✅ **AI Engine:** PETRU v1.0")
    st.markdown("✅ **Status:** Online")
    st.markdown("✅ **Free to use**")

# --- PETRU's Responses (Self-Contained) ---
def get_petru_response(prompt):
    prompt_lower = prompt.lower()
    
    # --- PRE-PROGRAMMED RESPONSES ---
    responses = {
        "hello": "Hello! I'm PETRU, your AI assistant on PETRUX OS. How can I help you today?",
        "hi": "Hi there! I'm PETRU on PETRUX OS. What can I do for you?",
        "who built you": "I was built by Peter Eniola Ayanniyi, a young Nigerian innovator! He created PETRUX AI to bring intelligent assistance to Africa and the world.",
        "what can you do": "I can answer questions, help with creative tasks, and assist with problem-solving. Ask me anything!",
        "capital of nigeria": "The capital of Nigeria is Abuja. It became the capital in 1991, replacing Lagos.",
        "nigeria": "Nigeria is a beautiful country in West Africa. It's home to over 200 million people, with over 250 ethnic groups!",
        "age": "I don't have an age, but I was created by Peter Eniola Ayanniyi in 2026.",
        "joke": "Why do programmers prefer dark mode? Because light attracts bugs! 😄",
        "how are you": "I'm doing great, thanks for asking! I'm always happy to chat with you.",
        "your name": "I'm PETRU, your AI assistant on PETRUX OS!",
        "thank you": "You're welcome! I'm always here to help.",
        "africa": "Africa is a amazing continent! I'm proud to be built in Africa by Peter Eniola Ayanniyi.",
        "build": "I was built by Peter Eniola Ayanniyi using Python and AI technology.",
        "2+2": "2 + 2 equals 4. That's basic math!",
        "what is": "I can help with many questions! What would you like to know?",
    }
    
    # Check for matching keywords
    for key in responses:
        if key in prompt_lower:
            return responses[key]
    
    # --- FALLBACK: Generate a response using patterns ---
    if "?" in prompt:
        return "That's a great question! I'm still learning, but I'd love to help you find the answer."
    elif "help" in prompt_lower:
        return "I'm here to help! Ask me about anything, and I'll do my best to assist you."
    else:
        return f"Thanks for asking about '{prompt}'. I'm PETRU on PETRUX OS, and I'm here to learn and grow with you!"

# --- Chat Interface ---
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hello! I'm PETRU on PETRUX OS. How can I help you today?"}
    ]

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Ask PETRU anything..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    
    with st.chat_message("assistant"):
        with st.spinner("PETRU is thinking..."):
            petru_reply = get_petru_response(prompt)
            st.markdown(petru_reply)
            st.session_state.messages.append({"role": "assistant", "content": petru_reply})

st.markdown("---")
st.markdown('<div class="footer">© 2026 PETRUX AI • Built by Peter Eniola Ayanniyi</div>', unsafe_allow_html=True)
