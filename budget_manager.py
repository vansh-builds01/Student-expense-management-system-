
import json
import os
from datetime import datetime


class BudgetManager:

    FILE_NAME = "budget.json"

    def __init__(self):
        self.budgets = self.load_budgets()

    # Load budgets
    def load_budgets(self):

        if os.path.exists(self.FILE_NAME):
            try:
                with open(self.FILE_NAME, "r") as file:
                    data = json.load(file)

                    if isinstance(data, dict):
                        return data

            except (json.JSONDecodeError, OSError):
                print("Error loading budget data.")

        return {}

    # Save budgets
    def save_budgets(self):

        try:
            with open(self.FILE_NAME, "w") as file:
                json.dump(self.budgets, file, indent=4)

        except OSError:
            print("Error saving budget.")

    # Set monthly budget
    def set_budget(self):

        month = input("Enter month (YYYY-MM): ").strip()

        try:
            datetime.strptime(month, "%Y-%m")

            amount = float(input("Enter monthly budget: ₹"))

            if amount <= 0:
                print("Budget must be greater than zero.")
                return

            self.budgets[month] = amount
            self.save_budgets()

            print("Monthly budget saved successfully!")

        except ValueError:
            print("Invalid month or budget amount.")

    # Calculate monthly spending
    def calculate_spending(self, expenses, month):

        return sum(
            expense["amount"]
            for expense in expenses
            if expense["date"].startswith(month)
        )

    # Check budget
    def check_budget(self, expenses):

        month = input("Enter month (YYYY-MM): ").strip()

        try:
            datetime.strptime(month, "%Y-%m")
        except ValueError:
            print("Invalid month format.")
            return

        if month not in self.budgets:
            print("No budget set for this month.")
            return

        budget = self.budgets[month]
        spent = self.calculate_spending(expenses, month)
        remaining = budget - spent

        print("\n--- BUDGET STATUS ---")
        print("Monthly Budget: ₹", budget)
        print("Total Spent: ₹", round(spent, 2))
        print("Remaining: ₹", round(remaining, 2))

        if remaining < 0:
            print("WARNING: Monthly budget exceeded!")

        elif spent >= budget * 0.8:
            print("WARNING: You have used at least 80% of your budget!")

        else:
            print("You are within your budget.")

    # Display all budgets
    def view_budgets(self):

        if not self.budgets:
            print("No budgets available.")
            return

        print("\n--- ALL MONTHLY BUDGETS ---")

        for month, amount in self.budgets.items():
            print(month, ": ₹", amount)
