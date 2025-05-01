from data import question_data

# Class to represent each question
class Question:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer

# Class to manage the quiz logic
class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.score = 0
        self.question_list = question_list

    # Check if there are more questions left
    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    # Ask the next question to the user
    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
        self.check_answer(user_answer, current_question.answer)

    # Check the user's answer and give feedback
    def check_answer(self, user_answer, correct_answer):
        if user_answer.strip().lower() == correct_answer.lower():
            self.score += 1
            print("✅ Correct!")
        else:
            print(f"❌ Wrong! The correct answer was: {correct_answer}.")
        print(f"Current Score: {self.score}/{self.question_number}\n")

# Create a list of Question objects from the question data
question_bank = []
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    question_bank.append(Question(question_text, question_answer))

# Start the quiz
quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

# Final result
print("🎉 You've completed the quiz!")
print(f"Your final score is: {quiz.score}/{quiz.question_number}")
