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
    st.markdown("✅ **AI Engine:** PETRU v2.0")
    st.markdown("✅ **Status:** Online & Smart")
    st.markdown("✅ **Free to use**")
    st.markdown("---")
    st.markdown("### 💡 Tips")
    st.markdown("Ask me about:")
    st.markdown("• Nigeria 🇳🇬")
    st.markdown("• Africa 🌍")
    st.markdown("• Math ➕")
    st.markdown("• History 📚")

# --- PETRU's RESPONSES (EXPANDED) ---
def get_petru_response(prompt):
    prompt_lower = prompt.lower()
    
    # --- GREETINGS ---
    if any(word in prompt_lower for word in ["hello", "hi", "hey", "good morning", "good afternoon"]):
        return "Hello! I'm PETRU on PETRUX OS. How can I help you today?"
    
    # --- ABOUT PETRU ---
    if any(word in prompt_lower for word in ["who built you", "your creator", "who made you"]):
        return "I was built by Peter Eniola Ayanniyi, a young Nigerian innovator! He created PETRUX AI to bring intelligent assistance to Africa and the world."
    
    if any(word in prompt_lower for word in ["your name", "who are you"]):
        return "I'm PETRU, your AI assistant running on PETRUX OS! I was built to help you learn and grow."
    
    # --- NIGERIA ---
    if "capital of nigeria" in prompt_lower:
        return "The capital of Nigeria is Abuja. It became the capital in 1991, replacing Lagos."
    
    if "nigeria" in prompt_lower and "history" in prompt_lower:
        return "Nigeria's history is rich and complex! It became independent from Britain in 1960. Before that, it was home to ancient kingdoms like the Nri, Oyo, and Benin empires. Today, Nigeria is Africa's most populous country with over 200 million people!"
    
    if "nigeria" in prompt_lower and ("ethnic" in prompt_lower or "group" in prompt_lower):
        return "Nigeria has over 250 ethnic groups! The three largest are Hausa, Igbo, and Yoruba. Each has its own unique language, culture, and traditions."
    
    if "nigeria" in prompt_lower:
        return "Nigeria is a beautiful country in West Africa. It's home to over 200 million people, over 250 ethnic groups, and is known as 'The Giant of Africa'. The country has a rich history, diverse cultures, and is a leader in music, film, and technology on the continent!"
    
    # --- AFRICA ---
    if "africa" in prompt_lower:
        return "Africa is an amazing continent! It's home to 54 countries, over 1.4 billion people, and is the birthplace of humanity. I'm proud to be built in Africa by Peter Eniola Ayanniyi!"
    
    # --- CONTINENTS ---
    if "continent" in prompt_lower:
        return "There are 7 continents in the world: Africa, Antarctica, Asia, Europe, North America, Australia/Oceania, and South America. Africa is the second largest!"
    
    # --- MATH ---
    if any(word in prompt_lower for word in ["math", "add", "subtract", "multiply", "divide"]):
        return "I can help with basic math! Just ask me something like: What is 5 + 5? or 10 x 5?"
    
    if "+" in prompt_lower or "-" in prompt_lower or "x" in prompt_lower or "/" in prompt_lower:
        try:
            # Simple math calculation
            result = eval(prompt_lower.replace("x", "*").replace("is", "").strip())
            return f"The answer is {result}! Let me know if you need more math help."
        except:
            return "I can do basic math! Try something like: 5 + 5 or 10 x 5."
    
    # --- JOKES ---
    if "joke" in prompt_lower:
        jokes = [
            "Why do programmers prefer dark mode? Because light attracts bugs! 😄",
            "What do you call a Nigerian programmer? A Nairobian! 😂",
            "Why did the AI break up with the human? It needed more processing power! 🤖",
            "What's a programmer's favorite song? 'Hello World' by Adele! 🎵"
        ]
        return random.choice(jokes)
    
    # --- FACTS ---
    if "fact" in prompt_lower:
        facts = [
            "Nigeria has the largest economy in Africa! 💰",
            "The first African country to gain independence was Ghana in 1957.",
            "Africa is the continent with the most countries (54)!",
            "The world's oldest university is in Africa - University of Timbuktu (1120 AD)!",
            "Nigeria produces the most movies in Africa - Nollywood! 🎬"
        ]
        return random.choice(facts)
    
    # --- HELP ---
    if "help" in prompt_lower or "what can you do" in prompt_lower:
        return "I can answer questions about Nigeria, Africa, history, math, and more! Just ask me anything. Try: 'Tell me about Nigeria' or 'What is 5 + 5?'"
    
    # --- FALLBACK (For any other question) ---
    if "?" in prompt_lower:
        return f"That's a great question! I'm still learning, but I'd love to help. Could you ask me about Nigeria, Africa, math, or history?"
    else:
        return f"Thanks for your message! I'm PETRU on PETRUX OS. Try asking me: 'Tell me about Nigeria' or 'What is 5 + 5?'"

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
