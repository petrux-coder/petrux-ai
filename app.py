import streamlit as st
import random
import time

st.set_page_config(
    page_title="PETRUX AI",
    page_icon="🤖",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# --- Mobile-Friendly CSS ---
st.markdown("""
<style>
    /* Mobile-first design */
    .main-title {
        text-align: center;
        font-size: 2.5rem;
        font-weight: 700;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        padding: 1rem 0;
    }
    .sub-title {
        text-align: center;
        font-size: 1rem;
        color: #666;
    }
    .footer {
        text-align: center;
        padding: 1.5rem 0;
        color: #888;
        font-size: 0.8rem;
    }
    /* Chat bubbles */
    .stChatMessage {
        background: #f8f9fa;
        border-radius: 15px;
        padding: 12px;
        margin: 5px 0;
    }
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    /* Better spacing on mobile */
    .block-container {
        padding: 1rem 0.5rem !important;
    }
    /* Sidebar styling */
    .css-1d391kg {
        background: linear-gradient(180deg, #667eea 0%, #764ba2 100%);
        color: white;
    }
</style>
""", unsafe_allow_html=True)

# --- Header ---
st.markdown('<div class="main-title">🤖 PETRUX AI</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">🖥️ Running on PETRUX OS</div>', unsafe_allow_html=True)

# --- Sidebar ---
with st.sidebar:
    st.image("https://via.placeholder.com/150x150.png?text=PETRUX", width=120)
    st.markdown("### 🌟 About PETRU")
    st.markdown("**PETRU** is your AI assistant on **PETRUX OS**.")
    st.markdown("💡 Built by: **Peter Eniola Ayanniyi**")
    st.markdown("🎯 Mission: Africa's AI Future")
    st.markdown("---")
    st.markdown("### 📊 Status")
    st.markdown("✅ **AI Engine:** PETRU v2.0")
    st.markdown("✅ **Status:** Online")
    st.markdown("✅ **Free to use**")
    st.markdown("---")
    st.markdown("### 💡 Quick Tips")
    st.markdown("• Ask about Nigeria 🇳🇬")
    st.markdown("• Ask about Africa 🌍")
    st.markdown("• Ask me anything!")

# --- PETRU's Knowledge ---
def get_petru_response(prompt):
    prompt_lower = prompt.lower()
    
    # Greetings
    if any(word in prompt_lower for word in ["hello", "hi", "hey"]):
        return "Hello! I'm PETRU on PETRUX OS. How can I help you today?"
    
    # About PETRU
    if any(word in prompt_lower for word in ["who built you", "who made you"]):
        return "I was built by Peter Eniola Ayanniyi, a young Nigerian innovator! He created PETRUX AI to bring intelligent assistance to Africa and the world."
    
    if any(word in prompt_lower for word in ["your name", "who are you"]):
        return "I'm PETRU, your AI assistant on PETRUX OS! I'm here to help you learn and grow."
    
    # Nigeria
    if "capital of nigeria" in prompt_lower:
        return "The capital of Nigeria is Abuja. It became the capital in 1991, replacing Lagos."
    
    if "nigeria" in prompt_lower and "history" in prompt_lower:
        return "Nigeria became independent from Britain in 1960. Before that, it was home to ancient kingdoms like the Nri, Oyo, and Benin empires. Today, it's Africa's most populous country!"
    
    if "nigeria" in prompt_lower:
        return "Nigeria is 'The Giant of Africa'! 🇳🇬 It has over 200 million people, 250+ ethnic groups, and is a leader in music, film (Nollywood), and technology on the continent!"
    
    # Africa
    if "africa" in prompt_lower:
        return "Africa is an amazing continent! 🌍 It has 54 countries, over 1.4 billion people, and is the birthplace of humanity. I'm proud to be built in Africa!"
    
    # Continents
    if "continent" in prompt_lower:
        if "largest" in prompt_lower:
            return "Asia is the largest continent! 🌏 Africa is the second largest."
        return "There are 7 continents: Africa, Antarctica, Asia, Europe, North America, Australia/Oceania, and South America."
    
    # Math
    if any(word in prompt_lower for word in ["+", "-", "x", "/", "plus", "minus", "times"]):
        try:
            import re
            math_pattern = r'(\d+\s*[\+\-\*\/]\s*\d+)'
            match = re.search(math_pattern, prompt_lower)
            if match:
                result = eval(match.group())
                return f"The answer is {result}! 🧮"
        except:
            pass
    
    # Jokes
    if "joke" in prompt_lower:
        jokes = [
            "Why do programmers prefer dark mode? Because light attracts bugs! 😄",
            "What do you call a Nigerian programmer? A Nairobian! 😂",
            "Why did the AI break up with the human? It needed more processing power! 🤖"
        ]
        return random.choice(jokes)
    
    # Facts
    if "fact" in prompt_lower:
        facts = [
            "Nigeria has the largest economy in Africa! 💰",
            "The world's oldest university is in Africa - University of Timbuktu (1120 AD)!",
            "Nigeria produces the most movies in Africa - Nollywood! 🎬"
        ]
        return random.choice(facts)
    
    # Help
    if "help" in prompt_lower or "what can you do" in prompt_lower:
        return "I can answer questions about Nigeria, Africa, history, math, and more! Just ask me anything."
    
    # Fallback
    return f"I'm PETRU on PETRUX OS! Try asking me about Nigeria, Africa, or math."

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
    
    with st.chat_message("assistant"):
        with st.spinner("PETRU is thinking..."):
            time.sleep(0.5)  # Simulate thinking
            petru_reply = get_petru_response(prompt)
            st.markdown(petru_reply)
            st.session_state.messages.append({"role": "assistant", "content": petru_reply})

# --- Footer ---
st.markdown("---")
st.markdown('<div class="footer">© 2026 PETRUX AI • Built by Peter Eniola Ayanniyi</div>', unsafe_allow_html=True)
