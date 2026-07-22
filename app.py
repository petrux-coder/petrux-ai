import streamlit as st
import requests
import json
import time

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
    st.markdown("✅ Answers ANY question")
    st.markdown("✅ Smart & Fast")
    st.markdown("✅ 100% Free")
    st.markdown("---")
    st.markdown("### 💡 Try asking:")
    st.markdown("• What is the capital of France?")
    st.markdown("• Tell me a story about Nigeria")
    st.markdown("• What is 125 x 37?")
    st.markdown("• Explain AI simply")

# --- USING YOUR TOKEN ---
API_URL = "https://api-inference.huggingface.co/models/microsoft/DialoGPT-medium"
headers = {"Authorization": "Bearer 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"}

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
            try:
                conversation = "\n".join([
                    f"{msg['role']}: {msg['content']}" 
                    for msg in st.session_state.messages[-6:]
                ])
                
                payload = {
                    "inputs": f"{conversation}\nassistant:",
                    "parameters": {
                        "max_new_tokens": 250,
                        "temperature": 0.8,
                        "do_sample": True,
                        "top_p": 0.9,
                        "repetition_penalty": 1.1
                    }
                }
                
                response = requests.post(API_URL, headers=headers, json=payload, timeout=60)
                
                if response.status_code == 200:
                    result = response.json()
                    petru_reply = result[0]['generated_text'].split("assistant:")[-1].strip()
                    
                    if not petru_reply:
                        petru_reply = "I'm PETRU on PETRUX OS. How can I help?"
                    
                    st.markdown(petru_reply)
                    st.session_state.messages.append({"role": "assistant", "content": petru_reply})
                else:
                    st.error(f"API Error: {response.status_code}")
                    st.info("💡 Please wait a moment and try again.")
                    
            except requests.exceptions.Timeout:
                st.error("⏰ PETRU is thinking hard! Please try again.")
            except requests.exceptions.ConnectionError:
                st.error("🌐 Connection error. Please refresh and try again.")
            except Exception as e:
                st.error(f"Error: {e}")

st.markdown("---")
st.markdown('<div class="footer">© 2026 PETRUX AI • Built by Peter Eniola Ayanniyi</div>', unsafe_allow_html=True)
