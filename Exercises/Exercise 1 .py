import tkinter as tk
from tkinter import messagebox
import random

class MathsQuiz:
    def __init__(self, root):
        self.root = root
        self.root.title("Maths Quiz")
        self.root.geometry("800x400")
        
        self.score = 0
        self.question_count = 0
        self.current_answer = 0
        self.difficulty_level = 1

        self.create_menu()

    def create_menu(self):
        # Clear  screen and  background color
        self.clear_window()
        self.root.config(bg="Thistle")

        # Title label for the difficulty menu
        label = tk.Label(self.root, text="DIFFICULTY LEVEL", font=("Helvetica", 16), bg="Thistle")
        label.pack(pady=50)

        # Difficulty options as buttons: Easy, Moderate, Advanced
        easy_button = tk.Button(self.root, text="Easy", command=lambda: self.start_quiz(1), bg="LightPink", font=("Helvetica", 12))
        easy_button.pack(pady=5)

        moderate_button = tk.Button(self.root, text="Moderate", command=lambda: self.start_quiz(2), bg="PeachPuff", font=("Helvetica", 12))
        moderate_button.pack(pady=5)

        advanced_button = tk.Button(self.root, text="Advanced", command=lambda: self.start_quiz(3), bg="PaleGoldenrod", font=("Helvetica", 12))
        advanced_button.pack(pady=5)

    def start_quiz(self, level):
        # Reset score and question count for a new quiz
        self.score = 0
        self.question_count = 0
        self.difficulty_level = level

        # Start with the first question
        self.next_question()

    def next_question(self):
        # If less than 10 questions, generate a new one; otherwise, show results
        if self.question_count < 10:
            self.question_count += 1
            self.num1 = self.random_int(self.difficulty_level)
            self.num2 = self.random_int(self.difficulty_level)
            operation = self.decide_operation()

            # Decide if it's an addition or subtraction and create the question text
            if operation == '+':
                self.current_answer = self.num1 + self.num2
                question_text = f"{self.num1} + {self.num2} ="
            else:
                self.current_answer = self.num1 - self.num2
                question_text = f"{self.num1} - {self.num2} ="

            # Display the question on screen
            self.display_question(question_text)
        else:
            # All questions answered, show the final score
            self.display_results()

    def random_int(self, level):
        # Generate a random number based on difficulty level
        if level == 1:
            return random.randint(1, 9)  # Single digit for Easy level
        elif level == 2:
            return random.randint(10, 99)  # Two digits for Moderate level
        elif level == 3:
            return random.randint(1000, 9999)  # Four digits for Advanced level

    def decide_operation(self):
        # Randomly choose between addition and subtraction
        return random.choice(['+', '-'])

    def display_question(self, question_text):
        # Clear the screen and set background color for the question screen
        self.clear_window()
        self.root.config(bg="DarkSeaGreen")

        # Show the question number
        question_number_label = tk.Label(self.root, text=f"Question {self.question_count}", font=("Helvetica", 14, "bold"), bg="lightyellow")
        question_number_label.pack(pady=5)

        # Show the question text
        question_label = tk.Label(self.root, text=question_text, font=("Helvetica", 16), bg="DarkSeaGreen")
        question_label.pack(pady=10)

        # Input field for the user's answer
        self.answer_entry = tk.Entry(self.root, font=("Helvetica", 14))
        self.answer_entry.pack(pady=5)
        self.answer_entry.bind("<Return>", self.check_answer)

        # Submit button to check the answer
        submit_button = tk.Button(self.root, text="Submit", command=self.check_answer, bg="lightblue")
        submit_button.pack(pady=5)

        # Back button to return to the menu
        back_button = tk.Button(self.root, text="Back", command=self.create_menu, bg="lightgray")
        back_button.pack(pady=5)

    def check_answer(self, event=None):
        try:
            # Get the user's answer from the input field
            user_answer = int(self.answer_entry.get())
        except ValueError:
            # Show a warning if input is not a number
            messagebox.showwarning("Invalid input", "Please enter a valid number.")
            return

        if user_answer == self.current_answer:
            # If correct on first try, award 10 points
            self.score += 10
            messagebox.showinfo("Correct!", "That's correct!")
            self.next_question()
        else:
            # Allow one more attempt if incorrect
            messagebox.showinfo("Try Again", "Incorrect. Try one more time.")
            self.answer_entry.delete(0, tk.END)
            self.answer_entry.bind("<Return>", self.check_second_attempt)

    def check_second_attempt(self, event=None):
        try:
            user_answer = int(self.answer_entry.get())
        except ValueError:
            messagebox.showwarning("Invalid input", "Please enter a valid number.")
            return

        if user_answer == self.current_answer:
            # Award 5 points for a correct answer on the second attempt
            self.score += 5
            messagebox.showinfo("Correct!", "That's correct!")
        else:
            # Inform user of the correct answer if they miss it twice
            messagebox.showinfo("Incorrect", f"The correct answer was {self.current_answer}.")

        # Move to the next question after the second attempt
        self.next_question()

    def display_results(self):
        # Clear the screen and set background color for the results screen
        self.clear_window()
        self.root.config(bg="lightgray")

        # Show final score
        result_text = f"Your final score is {self.score} out of 100."
        rank_text = self.get_rank_text()

        result_label = tk.Label(self.root, text=result_text, font=("Helvetica", 16), bg="lightgray")
        result_label.pack(pady=10)

        rank_label = tk.Label(self.root, text=rank_text, font=("Helvetica", 16), bg="lightgray")
        rank_label.pack(pady=5)

        # Buttons to play again, go back to menu, or quit
        play_again_button = tk.Button(self.root, text="Play Again", command=self.create_menu, bg="lightblue")
        play_again_button.pack(pady=5)

        back_button = tk.Button(self.root, text="Back to Menu", command=self.create_menu, bg="lightgray")
        back_button.pack(pady=5)

        quit_button = tk.Button(self.root, text="Quit", command=self.root.quit, bg="pink")
        quit_button.pack(pady=5)

    def get_rank_text(self):
        # Determine rank based on score
        if self.score > 90:
            return "Rank: A+"
        elif self.score > 80:
            return "Rank: A"
        elif self.score > 70:
            return "Rank: B"
        elif self.score > 60:
            return "Rank: C"
        else:
            return "Rank: D"

    def clear_window(self):
        # Remove all widgets from the window to start fresh for each screen
        for widget in self.root.winfo_children():
            widget.destroy()

# Main application code
if __name__ == "__main__":
    root = tk.Tk()
    app = MathsQuiz(root)
    root.mainloop()
