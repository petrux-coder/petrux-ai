import streamlit as st
import requests
import json

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
    st.markdown("### ✨ Features")
    st.markdown("✅ Intelligent Conversations")
    st.markdown("✅ Smart Responses")
    st.markdown("✅ 100% Free")

# Get token from Streamlit Secrets
HF_TOKEN = st.secrets.get("HF_TOKEN")

if not HF_TOKEN:
    st.error("⚠️ API token not configured. Please contact the app administrator.")
    st.stop()

# Use a simpler, more reliable model
API_URL = "https://api-inference.huggingface.co/models/microsoft/DialoGPT-medium"

def get_petru_response(user_input, chat_history):
    try:
        # Build conversation history
        conversation = "\n".join(chat_history[-4:])
        
        payload = {
            "inputs": f"{conversation}\nUser: {user_input}\nPETRU:",
            "parameters": {
                "max_new_tokens": 80,
                "temperature": 0.7,
                "do_sample": True,
                "pad_token_id": 50256,
                "repetition_penalty": 1.1
            }
        }
        
        headers = {
            "Authorization": f"Bearer {HF_TOKEN}",
            "Content-Type": "application/json"
        }
        
        response = requests.post(API_URL, headers=headers, json=payload, timeout=30)
        
        if response.status_code == 200:
            result = response.json()
            if isinstance(result, list) and len(result) > 0:
                generated_text = result[0].get('generated_text', '')
                reply = generated_text.split("PETRU:")[-1].strip()
                return reply if reply else "I'm PETRU on PETRUX OS. How can I help?"
            else:
                return "I'm PETRU on PETRUX OS. How can I help?"
        else:
            return f"I'm having trouble connecting. Please try again."
            
    except requests.exceptions.Timeout:
        return "The request timed out. Please try again."
    except Exception as e:
        return "I'm having trouble connecting. Please try again."

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hello! I'm PETRU on PETRUX OS. How can I help you today?"}
    ]
    st.session_state.chat_history = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Ask PETRU anything..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Add to chat history
    st.session_state.chat_history.append(f"User: {prompt}")
    
    with st.chat_message("assistant"):
        with st.spinner("PETRU is thinking..."):
            petru_reply = get_petru_response(prompt, st.session_state.chat_history)
            st.markdown(petru_reply)
            st.session_state.messages.append({"role": "assistant", "content": petru_reply})
            st.session_state.chat_history.append(f"PETRU: {petru_reply}")

st.markdown("---")
st.markdown('<div class="footer">© 2026 PETRUX AI • Built by Peter Eniola Ayanniyi</div>', unsafe_allow_html=True)
