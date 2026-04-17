# Personal Finance Tracker
import json
import matplotlib.pyplot as plt

# Data storage
data = {
    "income": [],
    "expenses": []
}

# Load data from file
def load_data():
    global data
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
    except:
        data = {"income": [], "expenses": []}

# Save data to file
def save_data():
    with open("data.json", "w") as file:
        json.dump(data, file)

# Add income
def add_income():
    try:
        amount = float(input("Enter income amount: "))
        data["income"].append(amount)
        save_data()
        print("Income added!")
    except:
        print("Invalid input")

# Add expense
def add_expense():
    try:
        amount = float(input("Enter expense amount: "))
        category = input("Enter category: ")

        expense = {
            "amount": amount,
            "category": category
        }

        data["expenses"].append(expense)
        save_data()
        print("Expense added!")
    except:
        print("Invalid input")

# View summary
def view_summary():
    total_income = sum(data["income"])
    total_expenses = sum(e["amount"] for e in data["expenses"])

    print("\n--- Summary ---")
    print(f"Income: £{total_income}")
    print(f"Expenses: £{total_expenses}")
    print(f"Savings: £{total_income - total_expenses}")

# Sort expenses
def sort_expenses():
    sorted_list = sorted(data["expenses"], key=lambda x: x["amount"])
    print("\n--- Sorted Expenses ---")
    for e in sorted_list:
        print(f"{e['category']}: £{e['amount']}")

# Show chart
def show_chart():
    categories = {}

    for e in data["expenses"]:
        cat = e["category"]
        categories[cat] = categories.get(cat, 0) + e["amount"]

    plt.bar(categories.keys(), categories.values())
    plt.title("Spending by Category")
    plt.xlabel("Category")
    plt.ylabel("Amount (£)")
    plt.show()

# Main menu
def menu():
    while True:
        print("\n--- Personal Finance Tracker ---")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View Summary")
        print("4. Sort Expenses")
        print("5. Show Chart")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_income()
        elif choice == "2":
            add_expense()
        elif choice == "3":
            view_summary()
        elif choice == "4":
            sort_expenses()
        elif choice == "5":
            show_chart()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice")

# Run program
load_data()
menu()
