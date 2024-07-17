import streamlit as st

st.title("Eduprism")
st.write(

#Quiz data
quiz_data = [
    {"question": "", "choices": ["", "", ""], "answer": ""},
    {"question": "", "choices": [, , , ], "answer": },
]

# Track quiz state
if 'current_question' not in st.session_state:
  st.session_state.current_question = 0
  st.session_state.score = 0

# Get current question data
current_question = quiz_data[st.session_state.current_question]

# Display question and choices
st.write(current_question["question"])
selected_choice = st.radio("Select your answer:", current_question["choices"])

# Check answer on submit button click
if st.button("Submit"):
  # Check if answer is filled in the dictionary
  if "answer" not in current_question:
    st.write("Error: Answer missing for this question!")
  else:
    if selected_choice == current_question["answer"]:
      st.write("Correct! Congratulation")
      st.session_state.score += 1
    else:
      st.write("Incorrect! The correct answer is", current_question["answer"])

  # Move to next question (if any)
  if st.session_state.current_question < len(quiz_data) - 1:
    st.session_state.current_question += 1
  else:
    st.write("Quiz completed! Your score is:", st.session_state.score, "/", len(quiz_data))
)
