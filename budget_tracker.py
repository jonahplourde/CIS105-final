"""
Budget Tracker Application
A comprehensive tool for tracking and managing personal expenses by category.
"""

import json
import os
from datetime import datetime


class BudgetTracker:
    """Class to manage budget and expenses."""
    
    def __init__(self, filename="budget_data.json"):
        """Initialize the budget tracker with data file."""
        self.filename = filename
        self.expenses = []
        self.categories = ["Food", "Transportation", "Entertainment", "Utilities", "Other"]
        self.load_data()
    
    def load_data(self):
        """Load expenses from file if it exists."""
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r') as file:
                    self.expenses = json.load(file)
            except json.JSONDecodeError:
                print("Warning: Could not read data file. Starting fresh.")
                self.expenses = []
        else:
            self.expenses = []
    
    def save_data(self):
        """Save expenses to file."""
        try:
            with open(self.filename, 'w') as file:
                json.dump(self.expenses, file, indent=2)
        except IOError as e:
            print(f"Error saving data: {e}")
    
    def add_expense(self, category, amount, description):
        """
        Add a new expense to the tracker.
        
        Args:
            category (str): Expense category
            amount (float): Expense amount
            description (str): Expense description
        
        Returns:
            bool: True if successful, False otherwise
        """
        if category not in self.categories:
            print(f"Invalid category. Available categories: {', '.join(self.categories)}")
            return False
        
        if amount <= 0:
            print("Amount must be greater than 0.")
            return False
        
        expense = {
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "category": category,
            "amount": amount,
            "description": description
        }
        
        self.expenses.append(expense)
        self.save_data()
        print(f"✓ Expense added successfully!")
        return True
    
    def get_category_total(self, category):
        """
        Calculate total expenses for a specific category.
        
        Args:
            category (str): Expense category
        
        Returns:
            float: Total amount spent in category
        """
        return sum(expense["amount"] for expense in self.expenses 
                   if expense["category"] == category)
    
    def get_total_expenses(self):
        """
        Calculate total expenses across all categories.
        
        Returns:
            float: Total amount spent
        """
        return sum(expense["amount"] for expense in self.expenses)
    
    def display_summary(self):
        """Display a summary report of expenses by category."""
        if not self.expenses:
            print("\nNo expenses recorded yet.")
            return
        
        print("\nExpense Summary:")
        total = self.get_total_expenses()
        
        for category in self.categories:
            category_total = self.get_category_total(category)
            if category_total > 0:
                percentage = (category_total / total * 100) if total > 0 else 0
                print(f"  {category}: ${category_total:.2f} ({percentage:.1f}%)")
        
        print(f"  Total: ${total:.2f}")
    
    def display_all_expenses(self):
        """Display all recorded expenses in a list format."""
        if not self.expenses:
            print("\nNo expenses recorded yet.")
            return
        
        print("\nAll Expenses:")
        for expense in self.expenses:
            print(f"  {expense['date']} | {expense['category']}: ${expense['amount']:.2f} - {expense['description']}")
    
    def display_category_expenses(self, category):
        """Display all expenses for a specific category."""
        category_expenses = [e for e in self.expenses if e["category"] == category]
        
        if not category_expenses:
            print(f"\nNo expenses recorded for {category}.")
            return
        
        print(f"\n{category} Expenses:")
        total = 0
        for expense in category_expenses:
            print(f"  {expense['date']} | ${expense['amount']:.2f} - {expense['description']}")
            total += expense['amount']
        
        print(f"Category Total: ${total:.2f}")


def display_menu():
    """Display the main menu options."""
    print("\n--- Budget Tracker Menu ---")
    print("1. Add expense")
    print("2. View all expenses")
    print("3. View summary")
    print("4. View by category")
    print("5. Exit")


def get_valid_amount():
    """
    Get and validate a monetary amount from user.
    
    Returns:
        float: Validated amount
    """
    while True:
        try:
            amount = float(input("Enter amount ($): "))
            if amount <= 0:
                print("Amount must be greater than 0. Try again.")
                continue
            return amount
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def add_expense_menu(tracker):
    """Handle the add expense menu option."""
    print("\nAdd New Expense")
    
    # Display available categories
    print("Categories:")
    for i, category in enumerate(tracker.categories, 1):
        print(f"  {i}. {category}")
    
    # Get category selection
    while True:
        try:
            choice = int(input("Select category: "))
            if 1 <= choice <= len(tracker.categories):
                category = tracker.categories[choice - 1]
                break
            else:
                print("Invalid selection.")
        except ValueError:
            print("Enter a valid number.")
    
    # Get amount
    amount = get_valid_amount()
    
    # Get description
    description = input("Description (optional): ").strip() or category
    
    tracker.add_expense(category, amount, description)


def view_category_menu(tracker):
    """Handle the view by category menu option."""
    print("\nView by Category")
    
    print("Categories:")
    for i, category in enumerate(tracker.categories, 1):
        total = tracker.get_category_total(category)
        print(f"  {i}. {category} (${total:.2f})")
    
    while True:
        try:
            choice = int(input("Select category: "))
            if 1 <= choice <= len(tracker.categories):
                category = tracker.categories[choice - 1]
                tracker.display_category_expenses(category)
                break
            else:
                print("Invalid selection.")
        except ValueError:
            print("Enter a valid number.")


def main():
    """Main program loop."""
    print("Welcome to Budget Tracker")
    
    tracker = BudgetTracker()
    
    while True:
        display_menu()
        
        try:
            choice = input("Select option: ").strip()
            
            if choice == "1":
                add_expense_menu(tracker)
            elif choice == "2":
                tracker.display_all_expenses()
            elif choice == "3":
                tracker.display_summary()
            elif choice == "4":
                view_category_menu(tracker)
            elif choice == "5":
                print("Goodbye!")
                break
            else:
                print("Invalid option.")
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break
        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
