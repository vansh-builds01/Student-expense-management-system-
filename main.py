
from expense_manager import ExpenseManager
from budget_manager import BudgetManager
from reports import ExpenseReports


def main():

    expense_manager = ExpenseManager()
    budget_manager = BudgetManager()
    reports = ExpenseReports()

    while True:

        print("\n" + "=" * 45)
        print("       SMART PERSONAL EXPENSE TRACKER")
        print("=" * 45)

        print("\n--- EXPENSE MANAGEMENT ---")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Search Expense")
        print("4. Update Expense")
        print("5. Delete Expense")
        print("6. Filter Expenses By Date")

        print("\n--- BUDGET MANAGEMENT ---")
        print("7. Set Monthly Budget")
        print("8. Check Budget Status")
        print("9. View All Budgets")

        print("\n--- REPORTS & ANALYSIS ---")
        print("10. Total Expenses")
        print("11. Highest Expense")
        print("12. Lowest Expense")
        print("13. Monthly Report")
        print("14. Category Analysis")
        print("15. Average Daily Spending")

        print("\n16. Exit")

        choice = input("\nEnter your choice: ").strip()

        # Expense management

        if choice == "1":
            expense_manager.add_expense()

        elif choice == "2":
            expense_manager.view_expenses()

        elif choice == "3":
            expense_manager.search_expense()

        elif choice == "4":
            expense_manager.update_expense()

        elif choice == "5":
            expense_manager.delete_expense()

        elif choice == "6":
            expense_manager.filter_by_date()

        # Budget management

        elif choice == "7":
            budget_manager.set_budget()

        elif choice == "8":
            budget_manager.check_budget(
                expense_manager.expenses
            )

        elif choice == "9":
            budget_manager.view_budgets()

        # Reports

        elif choice == "10":
            reports.total_expenses(
                expense_manager.expenses
            )

        elif choice == "11":
            reports.highest_expense(
                expense_manager.expenses
            )

        elif choice == "12":
            reports.lowest_expense(
                expense_manager.expenses
            )

        elif choice == "13":
            reports.monthly_report(
                expense_manager.expenses
            )

        elif choice == "14":
            reports.category_analysis(
                expense_manager.expenses
            )

        elif choice == "15":
            reports.average_daily_spending(
                expense_manager.expenses
            )

        elif choice == "16":
            print("\nThank you for using Smart Expense Tracker!")
            break

        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()
