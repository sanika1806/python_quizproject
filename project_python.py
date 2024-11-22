import json
import tkinter as tk
from tkinter import messagebox
import random

# Load quiz data from JSON file
with open("quiz_data.json", "r") as file:
    quiz_data = json.load(file)

# Limit to a maximum of 5 questions
quiz_data = random.sample(quiz_data, k=5)

# Rest of the QuizApp code follows
class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Application")
        self.root.geometry("400x300")
        
        self.question_number = 0
        self.score = 0
        
        self.question_label = tk.Label(root, text="", font=("Arial", 14), wraplength=350, justify="center")
        self.question_label.pack(pady=20)
        
        self.option_buttons = []
        for i in range(4):
            button = tk.Button(root, text="", font=("Arial", 12), width=20, command=lambda b=i: self.check_answer(b))
            button.pack(pady=5)
            self.option_buttons.append(button)
        
        self.next_button = tk.Button(root, text="Next", font=("Arial", 12), command=self.next_question)
        self.next_button.pack(pady=10)
        
        self.show_question()

    def show_question(self):
        # Display the current question and options
        if self.question_number < len(quiz_data):
            question_data = quiz_data[self.question_number]
            self.question_label.config(text=question_data["question"])
            for i, option in enumerate(question_data["options"]):
                self.option_buttons[i].config(text=option, state="normal")
        else:
            # End of quiz
            self.end_quiz()

    def check_answer(self, chosen_index):
        # Disable options after choosing an answer
        for button in self.option_buttons:
            button.config(state="disabled")
        
        question_data = quiz_data[self.question_number]
        selected_answer = question_data["options"][chosen_index]
        
        if selected_answer == question_data["answer"]:
            self.score += 1
            messagebox.showinfo("Correct", "You answered correctly!")
        else:
            messagebox.showinfo("Incorrect", f"The correct answer was {question_data['answer']}.")

    def next_question(self):
        # Move to the next question
        self.question_number += 1
        self.show_question()
        
    def end_quiz(self):
        # Show final score
        messagebox.showinfo("Quiz Complete", f"Your final score is {self.score} out of {len(quiz_data)}.")
        self.root.quit()

# Run the application
root = tk.Tk()
app = QuizApp(root)
root.mainloop()
