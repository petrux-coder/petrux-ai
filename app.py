
import streamlit as st
from transformers import AutoTokenizer, AutoModelForCausalLM
import warnings
warnings.filterwarnings('ignore')

st.set_page_config(page_title="PETRUX OS", page_icon="🤖", layout="centered")

st.title("🤖 PETRUX AI")
st.subheader("🖥️ Running on PETRUX OS")
st.caption("Built by Peter Eniola Ayanniyi")

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
