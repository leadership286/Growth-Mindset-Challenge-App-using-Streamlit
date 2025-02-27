import streamlit as st
import random
import datetime

# Theme Toggle
if "theme" not in st.session_state:
    st.session_state.theme = "light"

theme_toggle = st.sidebar.radio("🌗 Theme Mode", ["Light", "Dark"], index=0 if st.session_state.theme == "light" else 1)

if theme_toggle == "Dark":
    st.session_state.theme = "dark"
    st.markdown("""
        <style>
        body { background-color: #1E1E1E; color: white; }
        .stButton>button { background-color: #444; color: white; }
        .stRadio>div { color: white; }
        </style>
    """, unsafe_allow_html=True)
else:
    st.session_state.theme = "light"
    st.markdown("""
        <style>
        body { background-color: white; color: black; }
        .stButton>button { background-color: #ddd; color: black; }
        .stRadio>div { color: black; }
        </style>
    """, unsafe_allow_html=True)

# Growth mindset quotes
QUOTES = [
    "Challenges are what make life interesting. Overcoming them is what makes life meaningful.",
    "Your only limit is your mind.",
    "Mistakes are proof that you are trying.",
    "It does not matter how slowly you go as long as you do not stop.",
    "Dream big and dare to fail."
]

def get_daily_quote():
    return random.choice(QUOTES)

# Mindset Quiz
def mindset_quiz():
    st.subheader("Mindset Quiz: Do You Have a Growth Mindset?")
    score = 0
    questions = [
        ("I enjoy taking on new challenges.", 1),
        ("I believe effort leads to improvement.", 1),
        ("Failure means I should stop trying.", 0),
        ("I seek feedback to grow.", 1)
    ]
    
    for q, correct in questions:
        response = st.radio(q, ("Agree", "Disagree"))
        if (response == "Agree" and correct == 1) or (response == "Disagree" and correct == 0):
            score += 1
    
    if st.button("Submit Quiz"):
        st.success(f"Your growth mindset score: {score}/4")
        if score >= 3:
            st.write("You have a strong growth mindset! Keep it up! 🚀")
        else:
            st.write("You can develop your growth mindset further! Keep learning! 📚")

# Goal Tracker
def goal_tracker():
    st.subheader("📌 Goal Tracker")
    goal = st.text_input("Set a goal you want to achieve:")
    if st.button("Save Goal"):
        st.success(f"Goal saved: {goal}")

# Progress Journal
def progress_journal():
    st.subheader("📝 Progress Journal")
    journal_entry = st.text_area("Write about your progress today:")
    if st.button("Save Entry"):
        st.success("Journal entry saved! Keep going! 🚀")

# Learning Resources
def learning_resources():
    st.subheader("📚 Learning Resources")
    st.markdown("- [Mindset: The New Psychology of Success - Carol Dweck](https://www.amazon.com/dp/0345472322)")
    st.markdown("- [TED Talk: The Power of Believing That You Can Improve](https://www.ted.com/talks/carol_dweck_the_power_of_believing_that_you_can_improve)")

# Streamlit UI
st.title("🚀 Growth Mindset App")
st.write("A simple app to develop and maintain a growth mindset!")

st.subheader("🌟 Today's Quote")
st.info(get_daily_quote())

# Sidebar Menu - Enhanced UI
st.sidebar.title("Navigation")
st.sidebar.markdown("Welcome to the Growth Mindset App by **Rimsha Ansari**! 🌱")


menu = st.sidebar.radio("Menu", ["Mindset Quiz", "Goal Tracker", "Progress Journal", "Learning Resources"], index=0)

if menu == "Mindset Quiz":
    mindset_quiz()
elif menu == "Goal Tracker":
    goal_tracker()
elif menu == "Progress Journal":
    progress_journal()
elif menu == "Learning Resources":
    learning_resources()

st.sidebar.markdown("Created by **Rimsha Ansari** © 2025")

# Footer
st.markdown("---")
st.markdown("### Developed by Rimsha Ansari © 2025")