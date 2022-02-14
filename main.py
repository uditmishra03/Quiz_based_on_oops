from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


question_bank = []
for each in question_data:
    each_text = each["question"]
    each_answer = each["correct_answer"]
    question = Question(each_text, each_answer)
    question_bank.append(question)

quiz_brain = QuizBrain(question_bank)

while quiz_brain.still_has_question():
    quiz_brain.next_question()

print("You've completed the quiz.")
print(f"Your final score was: {quiz_brain.score}/{len(question_bank)}.")