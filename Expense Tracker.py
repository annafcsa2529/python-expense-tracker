
#Python Expense Tracker

expenses = []
monthly_budget = None

#Menu that initially prints
def show_menu():
    print("\n===== Expense Tracker =====")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. Total Spent")
    print("4. Category-wise Totals")
    print("5. Search Expenses")
    print("6. Delete an Expense")
    print("7. Set/View Budget")
    print("8. Exit")

#Function 1
def add_expense():
    try:
        amount = float(input("Enter amount: "))
    except ValueError:
        print("Invalid amount.")
        return

    category = input("Enter category: ").capitalize()
    note = input("Enter note: ")

    expense = {
        "amount": amount,
        "category": category,
        "note": note
    }

    expenses.append(expense)
    print("Expense added successfully!")

#Function 2
def view_expenses():
    if not expenses:#if no elements in main list
        print("No expenses yet.")
        return

    print("\n---- All Expenses ----")
    for i in range(len(expenses)):
        e = expenses[i]
        print(f"{i+1}. ₹{e['amount']} - {e['category']} ({e['note']})")

#Function 3
def total_spent():
    total = 0
    for e in expenses:
        total += e["amount"]

    print(f"\nTotal Spent: ₹{total}")

    # budget check
    if monthly_budget is not None:
        percent = (total / monthly_budget) * 100
        print(f"Budget used: {percent:.1f}%")

        if total > monthly_budget:
            print("⚠️ You exceeded your budget!")
        elif percent > 80:
            print("⚠️ Almost reaching your budget, be careful!")

#Function 4
def category_totals():
    if not expenses:
        print("No expenses to show.")
        return

    totals = {}

    for e in expenses:
        cat = e["category"]
        amt = e["amount"]

        if cat not in totals:
            totals[cat] = 0

        totals[cat] += amt

    print("\n---- Category Totals ----")
    for cat in totals:
        print(f"{cat}: ₹{totals[cat]}")

#Function 5
def search_expenses():
    if not expenses:
        print("No expenses to search.")
        return

    keyword = input("Enter category or note to search: ").lower()

    found = False
    print("\n---- Search Results ----")

    for i in range(len(expenses)):
        e = expenses[i]
        if keyword in e["category"].lower() or keyword in e["note"].lower():
            print(f"{i+1}. ₹{e['amount']} - {e['category']} ({e['note']})")
            found = True

    if not found:
        print("No matching expenses found.")

#Function 6
def delete_expense():
    view_expenses()

    if not expenses:
        return

    try:
        num = int(input("\nEnter expense number to delete: "))
    except ValueError:
        print("Invalid input.")
        return

    if num < 1 or num > len(expenses):
        print("Invalid expense number.")
        return

    removed = expenses.pop(num - 1)
    print(f"Deleted: ₹{removed['amount']} - {removed['category']}")

#Function 7
def set_budget():
    global monthly_budget

    if monthly_budget is None:
        print("No budget set.")
    else:
        print(f"Current budget: ₹{monthly_budget}")

    try:
        b = float(input("Enter new monthly budget (or 0 to remove): "))
    except ValueError:
        print("Invalid amount.")
        return

    if b == 0:
        monthly_budget = None
        print("Budget removed.")
    else:
        monthly_budget = b
        print("Budget updated.")


# MAIN LOOP

while True:#MAINLOOP
    show_menu()
    choice = input("Choose an option: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        total_spent()
    elif choice == "4":
        category_totals()
    elif choice == "5":
        search_expenses()
    elif choice == "6":
        delete_expense()
    elif choice == "7":
        set_budget()
    elif choice == "8":
        print("Exiting... Bye!")
        break
    else:
        print("Invalid choice.")
