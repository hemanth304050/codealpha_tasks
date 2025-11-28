# 🎮 CodeAlpha Hangman Game 
## 📌 Project Overview
This is a simple **text-based Hangman game** built using Python.  
The player must guess the hidden word letter-by-letter within **6 incorrect attempts**.

The game uses basic Python concepts like loops, lists, strings, conditional logic, and the `random` module.

---

## 🧠 Features
- 🎲 Randomly selects a word from a predefined list  
- 🔠 Shows blanks for unguessed letters  
- ❌ Only 6 wrong attempts allowed  
- 🔁 Runs until user wins or loses  
- 🖥️ Fully console-based  

---

## 🛠️ Technologies Used
- Python  
- random module  
- Lists & strings  
- Loops (`while`)  
- Conditional statements  

---

## ▶️ How to Run the Game

### 1️⃣ Save the script as:


### 2️⃣ Open Terminal (VS Code, CMD, or any Python environment)

### 3️⃣ Run:
```bash
python hangman.py
📂 Example Gameplay
🎮 Welcome to Hangman!
Word: _ _ _ _ _
Wrong attempts left: 6
Enter a letter: a
Correct!

Word: a _ _ _ _
Wrong attempts left: 6
Enter a letter: p
Correct!

Word: a p p _ _
Wrong attempts left: 6
Enter a letter: e
🎉 You won! The word was: apple
📝 Word List Used

The game randomly chooses from these 5 words:

python

apple

school

program

india
