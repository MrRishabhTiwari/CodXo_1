import tkinter as tk
from random import randint

class GuessingGame:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Number Guessing Game")
        self.window.geometry("400x350")
        self.window.configure(bg="#f0f0f0")

        self.difficulty = tk.StringVar()
        self.difficulty.set("easy")  
        self.attempts = 0
        self.max_attempts = 0
        self.number_to_guess = 0
        self.range_min = 0
        self.range_max = 0

        tk.Label(self.window, text="Number Guessing Game", font=("Arial", 24), bg="#f0f0f0").pack(pady=20)

        tk.Label(self.window, text="Select difficulty:", font=("Arial", 14), bg="#f0f0f0").pack()
        difficulty_frame = tk.Frame(self.window, bg="#f0f0f0")
        difficulty_frame.pack()
        tk.Radiobutton(difficulty_frame, text="Easy", variable=self.difficulty, value="easy", font=("Arial", 12)).pack(side=tk.LEFT)
        tk.Radiobutton(difficulty_frame, text="Medium", variable=self.difficulty, value="medium", font=("Arial", 12)).pack(side=tk.LEFT)
        tk.Radiobutton(difficulty_frame, text="Hard", variable=self.difficulty, value="hard", font=("Arial", 12)).pack(side=tk.LEFT)

        tk.Button(self.window, text="Set difficulty", command=self.set_difficulty, font=("Arial", 12), bg="#4CAF50", fg="#fff").pack(pady=10)

        tk.Label(self.window, text="Set range (min and max):", font=("Arial", 14), bg="#f0f0f0").pack()
        range_frame = tk.Frame(self.window, bg="#f0f0f0")
        range_frame.pack()
        self.range_min_entry = tk.Entry(range_frame, font=("Arial", 12), width=5)
        self.range_min_entry.pack(side=tk.LEFT)
        tk.Label(range_frame, text="to", font=("Arial", 12), bg="#f0f0f0").pack(side=tk.LEFT)
        self.range_max_entry = tk.Entry(range_frame, font=("Arial", 12), width=5)
        self.range_max_entry.pack(side=tk.LEFT)

        tk.Button(self.window, text="Set range", command=self.set_range, font=("Arial", 12), bg="#4CAF50", fg="#fff").pack(pady=10)

        tk.Label(self.window, text="Guess a number:", font=("Arial", 14), bg="#f0f0f0").pack()
        self.guess_entry = tk.Entry(self.window, font=("Arial", 12), width=10)
        self.guess_entry.pack()
        tk.Button(self.window, text="Guess", command=self.check_guess, font=("Arial", 12), bg="#4CAF50", fg="#fff").pack(pady=10)

        self.result_label = tk.Label(self.window, text="", font=("Arial", 14), bg="#f0f0f0")
        self.result_label.pack()

        self.window.mainloop()

    def set_difficulty(self):
        if self.difficulty.get() == "easy":
            self.max_attempts = 10
        elif self.difficulty.get() == "medium":
            self.max_attempts = 8
        else:
            self.max_attempts = 5
        self.attempts = 0

    def set_range(self):
        self.range_min = int(self.range_min_entry.get())
        self.range_max = int(self.range_max_entry.get())
        self.number_to_guess = randint(self.range_min, self.range_max)

    def check_guess(self):
        try:
            guess = int(self.guess_entry.get())
            if guess < self.range_min or guess > self.range_max:
                self.result_label.config(text=f"Error: Number out of range! Try again.")
            else:
                self.attempts += 1
                if guess == self.number_to_guess:
                    self.result_label.config(text=f"Congratulations! You guessed the number in {self.attempts} attempts.")
                elif self.attempts < self.max_attempts:
                    self.result_label.config(text=f"Try again! You have {self.max_attempts - self.attempts} attempts left.")
                else:
                    self.result_label.config(text=f"Game over! The number was {self.number_to_guess}.")
        except ValueError:
            self.result_label.config(text="Error: Invalid input! Please enter a number.")

if __name__ == "__main__":
    game = GuessingGame()
