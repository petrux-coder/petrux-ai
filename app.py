import streamlit as st
from transformers import pipeline
import warnings
warnings.filterwarnings('ignore')

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
    st.markdown("✅ Fast Responses")
    st.markdown("✅ 100% Free")

@st.cache_resource
def load_model():
    # Using a MUCH smaller and faster model
    return pipeline('text-generation', model='distilgpt2', device=-1)

try:
    generator = load_model()
    model_loaded = True
except:
    model_loaded = False

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
    
    if model_loaded:
        with st.chat_message("assistant"):
            with st.spinner("PETRU is thinking..."):
                try:
                    response = generator(
                        f"You are PETRU, a helpful AI assistant. Answer briefly: {prompt}\nPETRU:",
                        max_new_tokens=60,
                        do_sample=True,
                        temperature=0.7,
                        pad_token_id=50256
                    )
                    
                    petru_reply = response[0]['generated_text'].split("PETRU:")[-1].strip()
                    
                    if not petru_reply:
                        petru_reply = "I'm PETRU on PETRUX OS. How can I help?"
                    
                    st.markdown(petru_reply)
                    st.session_state.messages.append({"role": "assistant", "content": petru_reply})
                    
                except Exception as e:
                    st.error(f"Error: {e}")
    else:
        st.error("PETRU is not ready. Please try again later.")

st.markdown("---")
st.markdown('<div class="footer">© 2026 PETRUX AI • Built by Peter Eniola Ayanniyi</div>', unsafe_allow_html=True)
