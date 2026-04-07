import streamlit as st
from modules.preprocess import clean_text
from modules.sentiment import get_sentiment
from modules.emotion import get_emotion
from modules.llm_insight import generate_insight
from modules.database import init_db, insert_entry, fetch_data
from modules.visualization import plot_mood_trend, plot_emotions

# Page config
st.set_page_config(page_title="Mental Health AI", layout="wide")

# Custom CSS (✨ aesthetic)
st.markdown("""
    <style>
    .main {
        background-color: #f7f7fb;
    }
    .stTextArea textarea {
        border-radius: 10px;
    }
    .stButton button {
        background-color: #6c63ff;
        color: white;
        border-radius: 10px;
        height: 3em;
        width: 100%;
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.title("🧠 AI Mental Health Insight Analyzer")
st.caption("A gentle AI tool for emotional reflection 💭")

# Init DB
init_db()

# Layout
col1, col2 = st.columns([2, 1])

with col1:
    user_input = st.text_area("How are you feeling today?", height=150)

    if st.button("Analyze 💫"):
        if user_input.strip() != "":
            clean = clean_text(user_input)
            sentiment, score = get_sentiment(clean)
            emotion = get_emotion(clean)
            insight = generate_insight(user_input, sentiment, emotion)

            insert_entry(user_input, sentiment, score, emotion, insight)

            st.markdown("### 💬 AI Reflection")
            st.success(insight)

            st.markdown("### 📊 Analysis")
            st.write(f"**Sentiment:** {sentiment} ({round(score,2)})")
            st.write(f"**Emotion:** {emotion}")

with col2:
    st.markdown("### 🌿 About")
    st.info(
        "This tool helps you reflect on your emotions using AI.\n\n"
        "⚠️ Not a medical or psychological diagnosis."
    )

# Dashboard
st.markdown("---")
st.markdown("## 📈 Your Mood Journey")

data = fetch_data()

if not data.empty:
    st.plotly_chart(plot_mood_trend(data), use_container_width=True)
    st.plotly_chart(plot_emotions(data), use_container_width=True)
else:
    st.info("No data yet. Start by writing how you feel 💭")