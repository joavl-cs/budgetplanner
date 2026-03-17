import json

FILENAME = "transactions.json"

class BudgetPlanner:
    def __init__(self):
        self.income = []
        self.expenses = []
        self.load_data()

    def load_data(self):
        try:
            with open(FILENAME, "r") as file:
                data = json.load(file)
                if isinstance(data, dict):
                    self.income = data.get("income", [])
                    self.expenses = data.get("expenses", [])
                else:
                    self.income = []
                    self.expenses = []
        except (FileNotFoundError, json.JSONDecodeError):
            self.income = []
            self.expenses = []

    def save_data(self):
        data = {
            "income": self.income,
            "expenses": self.expenses
        }
        with open(FILENAME, "w") as file:
            json.dump(data, file, indent=4)

    def add_income(self, amount, category):
        if amount <= 0 or not category.strip():
            print("Invalid income entry.")
            return
        self.income.append([amount, category])
        self.save_data()

    def add_expense(self, amount, category):
        if amount <= 0 or not category.strip():
            print("Invalid expense entry.")
            return
        self.expenses.append([amount, category])
        self.save_data()

    def calculate_budget(self):
        total_income = sum(amount for amount, _ in self.income)
        total_expenses = sum(amount for amount, _ in self.expenses)
        return total_income, total_expenses, total_income - total_expenses

    def expense_statistics(self):
        categories = {}
        for amount, category in self.expenses:
            categories[category] = categories.get(category, 0) + amount
        return categories

    def income_statistics(self):
        categories = {}
        for amount, category in self.income:
            categories[category] = categories.get(category, 0) + amount
        return categories

    def delete_transaction(self, transaction_type, amount, category):
        if transaction_type == "expense":
            self.expenses = [e for e in self.expenses if not (e[0] == amount and e[1] == category)]
        elif transaction_type == "income":
            self.income = [i for i in self.income if not (i[0] == amount and i[1] == category)]
        else:
            print("Invalid transaction type.")
            return
        self.save_data()
        print(f"{transaction_type.capitalize()} transaction deleted successfully.")

# Helper function to print stats nicely
def print_statistics(stats):
    if not stats:
        print("No data available.")
        return
    for category, amount in sorted(stats.items(), key=lambda x: x[1], reverse=True):
        print(f"{category}: {amount}")

# Main program
if __name__ == "__main__":
    planner = BudgetPlanner()

    while True:
        print("\n=== Budget Planner ===")
        print("1. Add income")
        print("2. Add expense")
        print("3. View budget")
        print("4. View statistics")
        print("5. Delete transaction")
        print("6. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            try:
                amount = float(input("Enter income amount: "))
                category = input("Enter income category: ")
                planner.add_income(amount, category)
            except ValueError:
                print("Invalid amount entered.")

        elif choice == "2":
            try:
                amount = float(input("Enter expense amount: "))
                category = input("Enter expense category: ")
                planner.add_expense(amount, category)
            except ValueError:
                print("Invalid amount entered.")

        elif choice == "3":
            total_income, total_expenses, balance = planner.calculate_budget()
            print(f"\nTotal Income: {total_income}")
            print(f"Total Expenses: {total_expenses}")
            print(f"Current Balance: {balance}")

        elif choice == "4":
            print("\nExpense statistics:")
            print_statistics(planner.expense_statistics())
            print("\nIncome statistics:")
            print_statistics(planner.income_statistics())

        elif choice == "5":
            t_type = input("Delete income or expense? ").strip().lower()
            try:
                amount = float(input("Enter the amount to delete: "))
                category = input("Enter the category: ")
                planner.delete_transaction(t_type, amount, category)
            except ValueError:
                print("Invalid amount entered.")

        elif choice == "6":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")