BUDGET TRACKER - README
======================

WHAT YOUR PROGRAM DOES
Budget Tracker is a command-line Python application that helps users track and 
manage personal expenses by category. Users can add expenses, view all recorded 
expenses, see a summary report with spending by category and percentages, and 
filter expenses by specific categories. All data is automatically saved to a 
JSON file for persistence between sessions.

HOW TO RUN IT
1. Open a terminal/command prompt
2. Navigate to the project directory
3. Run: python budget_tracker.py
4. Follow the menu prompts to:
   - Add an expense (option 1)
   - View all expenses (option 2)
   - View spending summary (option 3)
   - View expenses by category (option 4)
   - Exit (option 5)

REQUIREMENTS
Python 3.6 or higher
No external libraries needed (uses only standard library: json, os, datetime)

RESOURCES USED
- Python Official Documentation: https://docs.python.org/3/
- Python json module: https://docs.python.org/3/library/json.html
- Python datetime module: https://docs.python.org/3/library/datetime.html
- Python os module: https://docs.python.org/3/library/os.html
- PEP 8 Style Guide: https://www.python.org/dev/peps/pep-0008/

FEATURES
- Add expenses with category, amount, and description
- View all recorded expenses
- View summary by category with percentages
- Filter expenses by category
- Persistent data storage (JSON file)
- Input validation and error handling
- Menu-driven interface
