
from datetime import datetime


class ExpenseReports:

    # Total spending
    def total_expenses(self, expenses):

        total = sum(e["amount"] for e in expenses)

        print("\nTotal Spending: ₹", round(total, 2))

    # Highest expense
    def highest_expense(self, expenses):

        if not expenses:
            print("No expenses available.")
            return

        highest = max(expenses, key=lambda e: e["amount"])

        print("\n--- HIGHEST EXPENSE ---")
        print("Category:", highest["category"])
        print("Description:", highest["description"])
        print("Amount: ₹", highest["amount"])
        print("Date:", highest["date"])

    # Lowest expense
    def lowest_expense(self, expenses):

        if not expenses:
            print("No expenses available.")
            return

        lowest = min(expenses, key=lambda e: e["amount"])

        print("\n--- LOWEST EXPENSE ---")
        print("Category:", lowest["category"])
        print("Description:", lowest["description"])
        print("Amount: ₹", lowest["amount"])

    # Monthly report
    def monthly_report(self, expenses):

        month = input("Enter month (YYYY-MM): ").strip()

        try:
            datetime.strptime(month, "%Y-%m")
        except ValueError:
            print("Invalid month format.")
            return

        monthly = [
            e for e in expenses
            if e["date"].startswith(month)
        ]

        if not monthly:
            print("No expenses found.")
            return

        total = sum(e["amount"] for e in monthly)

        print("\n========== MONTHLY REPORT ==========")
        print("Month:", month)
        print("Transactions:", len(monthly))
        print("Total Spending: ₹", round(total, 2))

        categories = {}

        for expense in monthly:

            category = expense["category"]

            categories[category] = (
                categories.get(category, 0) + expense["amount"]
            )

        print("\nCategory-wise spending:")

        for category, amount in categories.items():

            print(category, ": ₹", round(amount, 2))

        average = total / len(monthly)

        print("\nAverage expense per transaction: ₹",
              round(average, 2))

    # Category-wise analysis
    def category_analysis(self, expenses):

        if not expenses:
            print("No expenses available.")
            return

        categories = {}

        for expense in expenses:

            category = expense["category"]

            categories[category] = (
                categories.get(category, 0) + expense["amount"]
            )

        print("\n--- CATEGORY ANALYSIS ---")

        for category, amount in sorted(
            categories.items(),
            key=lambda item: item[1],
            reverse=True
        ):

            print(category, ": ₹", round(amount, 2))

    # Average daily spending for a month
    def average_daily_spending(self, expenses):

        month = input("Enter month (YYYY-MM): ").strip()

        try:
            datetime.strptime(month, "%Y-%m")
        except ValueError:
            print("Invalid month format.")
            return

        monthly = [
            e for e in expenses
            if e["date"].startswith(month)
        ]

        if not monthly:
            print("No expenses found.")
            return

        total = sum(e["amount"] for e in monthly)

        active_days = len(set(e["date"] for e in monthly))

        average = total / active_days

        print("\nAverage spending per active day: ₹",
              round(average, 2))
