# 🔢 Number Guessing Game (Python)

An interactive Python number guessing game where players try to guess a randomly selected number within a given range and limited attempts.

The game tracks your **best score (fewest attempts)** across multiple rounds.

---

## 🚀 Features

- User-defined number range
- Limited attempts per game
- Best score tracking across sessions
- Input validation
- Replay support
- Testable and modular design

---

## 🛠️ Tech Stack

- Python 3
- Built-in `random` module
- `unittest` for testing

---

## ▶️ How to Run

```bash
git clone https://github.com/<your-username>/number-guessing-game.git
cd number-guessing-game
python guessing_game.py
🧪 Running Tests
python -m unittest discover tests
🎮 Sample Gameplay
Enter the start range number: 1
Enter the end range number: 20

Attempt 1/10 - Enter your guess: 10
Too high!

Attempt 2/10 - Enter your guess: 7
🎉 Correct! You guessed it in 2 attempts.
🏆 New best score!
Best score so far: 2 attempts

💡 Future Enhancements
Difficulty levels
Guess history
Persistent best score (file or DB)
Web or GUI version

📜 License
MIT License
