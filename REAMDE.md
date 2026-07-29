# Expense Tracker

A simple command-line based Expense Tracker application built using Python.

This program helps users manage their expenses by adding, viewing, searching, updating, deleting, and analyzing expense records.

## Features

- Add new expenses
- View expenses
- Search expenses by:
  - ID
  - Date
  - Category
  - Description
  - Amount
- Update expense details
- Delete expenses
- Calculate total expenses
- Find highest expense
- Find lowest expense
- Store expense data using JSON file

## Technologies Used

- Python
- JSON
- datetime module

## Project Structure

```
Expense-Tracker/
│
├── main.py
├── expenses.json
└── README.md
```

## Requirements

- Python 3.10 or above

## How to Run

1. Download or clone the project.

2. Check Python installation:

```bash
python --version
```

3. Run the program:

```bash
python main.py
```

## Data Storage

Expense details are stored in:

```
expenses.json
```

The data contains:

- ID
- Date
- Amount
- Category
- Description

## Menu Options

```
1. Add Expenses
2. View Expense
3. Search Expense
4. Delete Expense
5. Update Expense
6. Calculate Expense
7. Highest Expense
8. Lowest Expense
9. Exit
```

## Error Handling

The program handles:

- Invalid number inputs
- Missing files
- Empty expense records

## Author

Created by:
Merala Murali Krishna