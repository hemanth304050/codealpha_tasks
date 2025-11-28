# 📊 CodeAlpha Stock Portfolio Tracker

## 📌 Project Overview
The **Stock Portfolio Tracker** is a Python script that calculates the **total investment value** based on user inputs and a predefined dictionary of stock prices.  
It also saves the results to **.txt** and **.csv** files for easy documentation.

This project demonstrates Python basics such as dictionaries, loops, file handling, and arithmetic operations.

---

## 🧠 Features
- 📝 User inputs stock symbol and quantity  
- 💹 Uses a hardcoded dictionary for stock prices  
- ➗ Calculates value = price × quantity  
- 📦 Saves output to:
  - `portfolio.txt`  
  - `portfolio.csv`  
- 📉 Displays total investment value in the console  
- 🖥️ Fully terminal-based program  

---

## 🛠️ Technologies Used
- Python  
- Dictionary  
- Input/Output  
- File Handling  
- Basic Arithmetic  

---

## ▶️ How to Run

### 1️⃣ Save the script as:


### 2️⃣ Open terminal (VS Code or CMD)

### 3️⃣ Run:
```bash
python portfolio_tracker.py
4️⃣ Enter stock names and quantities

Example:

AAPL
10
TSLA
3
done
📂 Example Console Output
AAPL added. Value = 1800
TSLA added. Value = 750

Total Investment Value: 2550

📝 Files Generated
📄 portfolio.txt
Stock   Qty   Price   Value
AAPL    10    180     1800
TSLA     3    250     750

Total Investment: 2550
📑 portfolio.csv
Stock,Quantity,Price,Value
AAPL,10,180,1800
TSLA,3,250,750
Total,2550

📊 Hardcoded Stock Prices Used
AAPL  → 180
TSLA  → 250
GOOGL → 140
AMZN  → 135
MSFT  → 400
