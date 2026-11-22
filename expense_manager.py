
import json
import os
from datetime import datetime


class ExpenseManager:

    FILE_NAME = "expenses.json"

    def __init__(self):
        self.expenses = self.load_expenses()

    # Load expenses
    def load_expenses(self):
        if os.path.exists(self.FILE_NAME):
            try:
                with open(self.FILE_NAME, "r") as file:
                    data = json.load(file)

                    if isinstance(data, list):
                        return data

            except (json.JSONDecodeError, OSError):
                print("Error loading expense data.")

        return []

    # Save expenses
    def save_expenses(self):
        try:
            with open(self.FILE_NAME, "w") as file:
                json.dump(self.expenses, file, indent=4)
            return True

        except OSError:
            print("Error saving expenses.")
            return False

    # Generate unique ID
    def generate_id(self):
        return max(
            (e.get("id", 0) for e in self.expenses
             if isinstance(e.get("id"), int)),
            default=0
        ) + 1

    # Add expense
    def add_expense(self):

        print("\n--- ADD NEW EXPENSE ---")

        try:
            amount = float(input("Enter amount: ₹"))

            if amount <= 0:
                print("Amount must be greater than zero.")
                return

            category = input("Enter category: ").strip()
            description = input("Enter description: ").strip()

            if not category or not description:
                print("Category and description cannot be empty.")
                return

            expense = {
                "id": self.generate_id(),
                "amount": amount,
                "category": category.title(),
                "description": description,
                "date": datetime.now().strftime("%Y-%m-%d")
            }

            self.expenses.append(expense)

            if self.save_expenses():
                print("Expense added successfully!")

        except ValueError:
            print("Please enter a valid amount.")

    # View expenses
    def view_expenses(self):

        if not self.expenses:
            print("No expenses found.")
            return

        print("\n--- ALL EXPENSES ---")

        for expense in self.expenses:
            print("-" * 35)
            print("ID:", expense["id"])
            print("Date:", expense["date"])
            print("Category:", expense["category"])
            print("Description:", expense["description"])
            print("Amount: ₹", expense["amount"])

    # Search expenses
    def search_expense(self):

        category = input("Enter category: ").strip().lower()

        found = False

        for expense in self.expenses:

            if expense["category"].lower() == category:
                print("\n", expense)
                found = True

        if not found:
            print("No matching expenses found.")

    # Delete expense
    def delete_expense(self):

        try:
            expense_id = int(input("Enter expense ID: "))

            for expense in self.expenses:

                if expense["id"] == expense_id:

                    self.expenses.remove(expense)

                    if self.save_expenses():
                        print("Expense deleted successfully!")

                    return

            print("Expense not found.")

        except ValueError:
            print("Invalid ID.")

    # Update expense
    def update_expense(self):

        try:
            expense_id = int(input("Enter expense ID: "))

            for expense in self.expenses:

                if expense["id"] == expense_id:

                    print("\n1. Update Amount")
                    print("2. Update Category")
                    print("3. Update Description")

                    choice = input("Choose option: ")

                    if choice == "1":

                        amount = float(input("Enter new amount: ₹"))

                        if amount <= 0:
                            print("Invalid amount.")
                            return

                        expense["amount"] = amount

                    elif choice == "2":

                        category = input("New category: ").strip()

                        if not category:
                            print("Category cannot be empty.")
                            return

                        expense["category"] = category.title()

                    elif choice == "3":

                        description = input("New description: ").strip()

                        if not description:
                            print("Description cannot be empty.")
                            return

                        expense["description"] = description

                    else:
                        print("Invalid choice.")
                        return

                    if self.save_expenses():
                        print("Expense updated successfully!")

                    return

            print("Expense not found.")

        except ValueError:
            print("Invalid input.")

    # Filter expenses by date
    def filter_by_date(self):

        date = input("Enter date (YYYY-MM-DD): ").strip()

        try:
            datetime.strptime(date, "%Y-%m-%d")
        except ValueError:
            print("Invalid date format.")
            return

        found = False

        for expense in self.expenses:

            if expense["date"] == date:
                print(expense)
                found = True

        if not found:
            print("No expenses found on this date.")
