# 🛠️ CodeAlpha Task Automation with Python Scripts

## 📌 Project Overview
This project automates a simple real-life task using Python:  
**Moving all `.jpg` / `.jpeg` files from one folder to another** automatically.

It demonstrates Python’s ability to interact with the operating system, handle files, and perform repetitive tasks with ease.

---

## 🧠 Features
- 📁 Scans a source folder for image files  
- 🔍 Detects `.jpg` and `.jpeg` files (case-insensitive)  
- 🚚 Moves files to the destination folder using `shutil.move`  
- 🆕 Automatically creates the destination folder if it doesn't exist  
- 📊 Prints a summary of moved files  
- 🖥️ Fully automated and terminal-based  

---

## 🛠️ Technologies Used
- Python  
- `os` module  
- `shutil` module  
- File handling  
- Loops & conditions  

---

## ▶️ How to Run

### 1️⃣ Save the script as:

### 2️⃣ Open the terminal in VS Code or CMD

### 3️⃣ Run:
```bash
python move_jpg_files.py
 4️⃣ Enter:
📂 Source folder path

📂 Destination folder path

Example:
Enter source folder path: C:\Users\User\Pictures\source
Enter destination folder path: C:\Users\User\Pictures\moved
📂 Example Output
Moved: C:\photos\img1.jpg -> C:\moved\img1.jpg
Moved: C:\photos\pic2.jpeg -> C:\moved\pic2.jpeg

Total .jpg/.jpeg files moved: 2
📝 Script Logic (Summary)
Check if source folder exists

Create destination folder (if missing)

Loop through all files

Identify .jpg / .jpeg

Move each file

Count moved files

Display final summary
