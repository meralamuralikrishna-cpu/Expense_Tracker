# Expense Tracker

A command-line Expense Tracker application built with Python. It allows users to manage daily expenses using a JSON file for persistent storage. The project demonstrates Python fundamentals, file handling, JSON manipulation, exception handling, and CRUD operations.

---

## Features

* Add expenses
* View all expenses
* View an expense by ID
* Search expenses by:

  * ID
  * Date
  * Category
  * Description
  * Amount
* Update existing expenses
* Delete expenses
* Calculate total expenses
* View category-wise expense summary
* Find the highest expense
* Find the lowest expense
* Calculate the average expense

---

## Technologies Used

* Python 3
* JSON
* datetime
* time

---

## Project Structure

```text
Expense_Tracker/
│
├── main.py
├── expenses.json
└── README.md
```

---

## JSON Format

```json
{
    "expenses": [
        {
            "id": 1,
            "date": "28/12/2005",
            "amount": 500,
            "category": "food",
            "description": "lunch"
        }
    ]
}
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/your-username/Expense_Tracker.git
```

Navigate to the project directory:

```bash
cd Expense_Tracker
```

Run the application:

```bash
python main.py
```

---

## Menu

```text
1. Add Expense
2. View Expense
3. Search Expense
4. Delete Expense
5. Update Expense
6. Calculate Total Expense
7. Category Summary
8. Highest Expense
9. Lowest Expense
10. Average Expense
11. Exit
```

---

## Concepts Used

* Functions
* Loops
* Conditional Statements
* Lists and Dictionaries
* JSON File Handling
* Exception Handling
* Date Handling
* CRUD Operations
