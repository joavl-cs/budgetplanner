#💰 Budget Planner

A simple Python console app to track your income and expenses, calculate your budget, and see stats by category.

🚀 Features:

💵 Add income or expense with categories

📊 View budget: total income, expenses, and balance

📈 See statistics by category (sorted by amount)

🗑️ Delete transactions safely by amount + category

💾 Data saved in transactions.json for persistence

✅ Input validation for clean data

🛠️ Requirements:

Python 3.x

No external libraries required

⚡ Usage:

Run the program:

python budget_planner.py

Follow the menu:

Option	Action
1	Add income
2	Add expense
3	View budget
4	View statistics
5	Delete transaction
6	Exit

Enter amounts (positive numbers) and categories (e.g., Food, Salary).

Deleting transactions requires exact amount + category.

📌 Example
=== Budget Planner ===
1. Add income
2. Add expense
3. View budget
4. View statistics
5. Delete transaction
6. Exit
Choose an option: 1
Enter income amount: 500
Enter income category: Salary

Choose an option: 2
Enter expense amount: 50
Enter expense category: Food

Choose an option: 3
Total Income: 500
Total Expenses: 50
Current Balance: 450

Choose an option: 4
Expense statistics:
Food: 50

Income statistics:
Salary: 500
💡 Tips

Transactions are saved automatically in transactions.json

Stats are sorted by highest amounts for easy review

Keep categories consistent for better tracking

📄 License

This project is free to use, modify, and share.
