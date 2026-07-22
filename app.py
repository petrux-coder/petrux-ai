
import streamlit as st
from transformers import AutoTokenizer, AutoModelForCausalLM
import warnings
warnings.filterwarnings('ignore')

# --- Better Page Configuration ---
st.set_page_config(
    page_title="PETRUX AI",
    page_icon="🤖",
    layout="centered"
)

# --- Professional Styling ---
st.markdown('''
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
    .stChatMessage {
        background: #f8f9fa;
        border-radius: 10px;
        padding: 10px;
    }
</style>
''', unsafe_allow_html=True)

# --- Header ---
st.markdown('<div class="main-title">🤖 PETRUX AI</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">🖥️ Running on PETRUX OS</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">Built by Peter Eniola Ayanniyi</div>', unsafe_allow_html=True)
st.markdown("---")

# --- Sidebar with Info ---
with st.sidebar:
    st.markdown("### 🌟 About PETRU")
    st.markdown("**PETRU** is your AI assistant on **PETRUX OS**.")
    st.markdown("💡 Built by: **Peter Eniola Ayanniyi**")
    st.markdown("🎯 Mission: Africa's AI Future")
    st.markdown("---")
    st.markdown("### ✨ Features")
    st.markdown("✅ Intelligent Conversations")
    st.markdown("✅ Context Memory")
    st.markdown("✅ Fast Responses")
    st.markdown("✅ 100% Free")
    st.markdown("---")
    st.markdown("### 🔗 Quick Links")
    st.markdown("[📂 GitHub Repository](https://github.com/petrux-coder/petrux-ai)")
    st.markdown("[❓ Report Issue](https://github.com/petrux-coder/petrux-ai/issues)")

# --- Load Model ---
@st.cache_resource
def load_model():
    tokenizer = AutoTokenizer.from_pretrained("TinyLlama/TinyLlama-1.1B-Chat-v1.0")
    model = AutoModelForCausalLM.from_pretrained(
        "TinyLlama/TinyLlama-1.1B-Chat-v1.0",
        device_map="auto",
        torch_dtype="auto"
    )
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token
    return tokenizer, model

try:
    tokenizer, model = load_model()
    model_loaded = True
except:
    model_loaded = False

# --- Chat Interface ---
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hello! I'm PETRU on PETRUX OS. How can I help you today?"}
    ]

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
if prompt := st.chat_input("Ask PETRU anything..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    
    if model_loaded:
        with st.chat_message("assistant"):
            with st.spinner("PETRU is thinking..."):
                try:
                    formatted_messages = [
                        {"role": "system", "content": "You are PETRU, a helpful AI assistant on PETRUX OS."}
                    ] + st.session_state.messages
                    
                    prompt_text = tokenizer.apply_chat_template(
                        formatted_messages,
                        tokenize=False,
                        add_generation_prompt=True
                    )
                    
                    inputs = tokenizer(prompt_text, return_tensors="pt", truncation=True, max_length=2048)
                    
                    outputs = model.generate(
                        **inputs,
                        max_new_tokens=200,
                        temperature=0.7,
                        do_sample=True,
                        pad_token_id=tokenizer.pad_token_id
                    )
                    
                    response = tokenizer.decode(outputs[0][inputs.input_ids.shape[1]:], skip_special_tokens=True)
                    petru_reply = response.strip()
                    
                    if not petru_reply:
                        petru_reply = "I'm PETRU on PETRUX OS. How can I help?"
                    
                    st.markdown(petru_reply)
                    st.session_state.messages.append({"role": "assistant", "content": petru_reply})
                    
                except Exception as e:
                    st.error(f"Error: {e}")
    else:
        st.error("PETRU is not ready. Please try again later.")

# --- Footer ---
st.markdown("---")
st.markdown('<div class="footer">© 2026 PETRUX AI • Built by Peter Eniola Ayanniyi</div>', unsafe_allow_html=True)
