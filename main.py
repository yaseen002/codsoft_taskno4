import tkinter as tk
from tkinter import PhotoImage, Label
import random

def play_game(user_choice):
    global score
    computer_choice = random.choice(["rock", "paper", "scissors"])
    result = determine_winner(user_choice, computer_choice)
    display_result(user_choice, computer_choice, result)
    
    # Update score and display
    if result == "You win!":
        score += 1
        score_label.config(text=f"Score: {score}")

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "scissors" and computer_choice == "paper") or
        (user_choice == "paper" and computer_choice == "rock")
    ):
        return "You win!"
    else:
        return "Computer wins!"

def display_result(user_choice, computer_choice, result):
    result_label.config(text=f"You chose {user_choice}\nComputer chose {computer_choice}\nResult: {result}", fg="green" if result == "You win!" else "red")

def save_score():
    with open("score.txt", "w") as file:
        file.write(str(score))

# Create the main window
root = tk.Tk()
root.title("Rock-Paper-Scissors Game")

# Load and resize images with adjusted subsample values
rock_img = PhotoImage(file="rockk.png").subsample(6, 6)
paper_img = PhotoImage(file="paper.png").subsample(2, 2)
scissors_img = PhotoImage(file="scissors.png").subsample(2, 2)

# Create and pack image buttons
rock_button = tk.Button(root, image=rock_img, command=lambda: play_game("rock"))
rock_button.pack(side=tk.LEFT, padx=10)

paper_button = tk.Button(root, image=paper_img, command=lambda: play_game("paper"))
paper_button.pack(side=tk.LEFT, padx=10)

scissors_button = tk.Button(root, image=scissors_img, command=lambda: play_game("scissors"))
scissors_button.pack(side=tk.LEFT, padx=10)

# Create and pack result label
result_label = tk.Label(root, text="Select one", fg="black")
result_label.pack(pady=20)

# Create and pack score label
score = 0
score_label = tk.Label(root, text="Score: 0")
score_label.pack(anchor=tk.W, padx=10, pady=10)

# Create and pack exit button
exit_button = tk.Button(root, text="Exit", command=lambda: [save_score(), root.destroy()])
exit_button.pack(side=tk.BOTTOM, pady=10)

# Run the Tkinter main loop
root.mainloop()
