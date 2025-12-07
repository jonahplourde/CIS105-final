BUDGET TRACKER - README
======================

OVERVIEW
Budget Tracker is a command-line Python application that helps users track and 
manage personal expenses by category.

HOW TO RUN
python budget_tracker.py

FEATURES
- Add expenses with category, amount, and description
- View all recorded expenses
- View summary by category with percentages
- Filter expenses by category
- Persistent data storage (JSON)
- Error handling and input validation

CATEGORIES
Food, Transportation, Entertainment, Utilities, Other

REQUIREMENTS
Python 3.6+
No external libraries needed

DATA STORAGE
Expenses saved to budget_data.json

RUBRIC COVERAGE
- User Interaction: Menu-driven interface with input validation
- Data Handling: Lists, dictionaries, JSON persistence (load_data, save_data, 
  get_category_total, get_total_expenses functions)
- Control Structures: While loops, for loops, if/else statements
- Functions: 12 custom functions handling specific tasks
- Error Handling: Try/except blocks for file I/O, JSON, numeric input, KeyboardInterrupt
- Output: Clear formatted output with summaries and reports
