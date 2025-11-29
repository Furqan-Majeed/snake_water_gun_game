Markdown

# 🐍 Snake-Water-Gun Game

![Python](https://img.shields.io/badge/Language-Python-blue?style=for-the-badge&logo=python) ![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge) ![Status](https://img.shields.io/badge/Status-Completed-orange?style=for-the-badge)

A simple and fun command-line game built using Python. This is a variation of the classic **Rock-Paper-Scissors** game, where the user plays against the computer.

## 📌 Game Rules

The logic is simple and follows a cyclical winning pattern:

| Your Choice | Computer Choice | Result | Reason |
| :--- | :--- | :--- | :--- |
| **Snake 🐍** | Water 💧 | **You Win** | Snake drinks Water |
| **Water 💧** | Gun 🔫 | **You Win** | Water damages Gun |
| **Gun 🔫** | Snake 🐍 | **You Win** | Gun shoots Snake |
| **Same** | Same | **Tie** | Choices matched |

*(The reverse applies if the Computer makes the winning move!)*

## 🚀 Features

* **Human vs Computer:** Play against a randomized AI logic.
* **Input Validation:** Handles user input gracefully.
* **Randomized Outcomes:** Uses Python’s `random` module for unpredictable gameplay.
* **Clean Logic:** Easy-to-read `if-elif-else` conditional structures.
* **Replayability:** Play as many rounds as you like.

## 📂 Project Structure

```text
snake_water_gun_game/
│
│── main.py             # The source code for the game
│── README.md           # Project documentation
💻 Sample Output
Here is what the game looks like when you run it in the terminal:

Plaintext

Computer Turn: Snake(s) Water(w) or Gun(g)?
Your Turn: s

You chose: Snake
Computer chose: Water

🐍 Snake drinks Water! You Win!
🛠️ Tech Stack
Language: Python 3.x

Modules: random (Standard Library)

▶️ How to Run the Game
Clone the repository:

Bash

git clone https://github.com/Furqan-Majeed/snake_water_gun_game.git
Navigate to the project folder:

Bash

cd snake_water_gun_game
Run the game:

Bash

python main.py
(Note: Ensure your python file is named main.py or game.py inside the folder)

📈 What I Learned
By building this project, I practiced:

Implementing core game logic and algorithms.

Using Python conditional statements (if, elif, else).

Handling user inputs and edge cases.

Working with the random module to generate computer choices.

Structuring a beginner-friendly Python project.

🤝 Contributions
Contributions are welcome! If you have ideas for new features (like a scoreboard or a GUI), feel free to fork the repo and submit a pull request.

📜 License
This project is licensed under the MIT License.
