from datetime import datetime
import matplotlib.pyplot as plt
categories = [
    "Food", "Travel", "Shopping", "Bills",
    "Gym", "College", "Medical",
    "Entertainment", "Recharge", "Extra"
]
limits = {
    "Food": 3000,
    "Travel": 2000,
    "Shopping": 4000,
    "Bills": 5000,
    "Gym": 1500,
    "College": 3000,
    "Medical": 2500,
    "Entertainment": 2000,
    "Recharge": 1000,
    "Extra": 2000
}
all_expense = []
try:
    with open("expense.txt", "r") as file:
        for line in file:
            data = line.strip().split(",")
            expense = {
                "date": data[0],
                "amount": float(data[1]),
                "category": data[2]
            }
            all_expense.append(expense)
except FileNotFoundError:
    pass

print("=" * 50)
print("         PERSONAL EXPENSE TRACKER")
print("=" * 50)

while True:
    current_date = datetime.now().strftime("%d-%m-%Y")
    print("\nCurrent Date :", current_date)
    try:
        amount = float(input("Enter amount : Rs "))
    except ValueError:
        print("Invalid amount entered")
        continue

    category = input("Enter category : ").title()
    if category in categories:
        expense = {
            "date": current_date,
            "amount": amount,
            "category": category
        }
        all_expense.append(expense)
        with open("expense.txt", "a") as file:
            file.write(f"{current_date},{amount},{category}\n")
        print("Expense added successfully")

        choice = input("Do you want to add another expense? (yes/no) : ")
        if choice.lower() != "yes":
            break
    else:
        print("Invalid category")
        print("Available categories :", categories)

print("\n" + "=" * 50)
print("               ALL EXPENSES")

for expense in all_expense:

    print("Date      :", expense["date"])
    print("Amount    : Rs", expense["amount"])
    print("Category  :", expense["category"])
    print("-" * 40)

total = 0
for expense in all_expense:
    total += expense["amount"]
print("\nTotal Expense = Rs", total)

search = input("\nEnter category to search : ").title()

category_total = 0
print("\n" + "=" * 50)
print(f"         {search.upper()} EXPENSES")
print("=" * 50)

for expense in all_expense:
    if expense["category"] == search:
        print("Date      :", expense["date"])
        print("Amount    : Rs", expense["amount"])
        print("Category  :", expense["category"])
        print("-" * 40)

        category_total += expense["amount"]

print("Total", search, "Expense = Rs", category_total)

if search in limits:

    if category_total > limits[search]:

        extra = category_total - limits[search]

        print("Alert :", search,
              "expense limit exceeded by Rs", extra)

    else:
        print(search, "expense is within budget")

else:
    print("Category not found in limits")

try:
    budget = float(input("\nEnter monthly budget : Rs "))

except ValueError:
    print("Invalid budget amount")
    budget = 0

amount_left = budget - total

print("\nRemaining Amount = Rs", amount_left)

if amount_left < 0:
    print("Status : Out of budget")

else:
    print("Status : Within budget")

print("\n" + "=" * 50)
print("           CATEGORY SUMMARY")

category_names = []
category_values = []

for cat in categories:

    cat_total = 0

    for expense in all_expense:

        if expense["category"] == cat:
            cat_total += expense["amount"]

    print(cat, "= Rs", cat_total)
    category_names.append(cat)
    category_values.append(cat_total)

if len(all_expense) > 0:
    highest = all_expense[0]
    for expense in all_expense:

        if expense["amount"] > highest["amount"]:
            highest = expense

    print("\n" + "=" * 50)
    print("            HIGHEST EXPENSE")

    print("Date      :", highest["date"])
    print("Amount    : Rs", highest["amount"])
    print("Category  :", highest["category"])
else:
    print("No expenses entered")

plt.figure(figsize=(10, 6))
plt.bar(category_names, category_values)
plt.xlabel("Categories")
plt.ylabel("Amount Spent")
plt.title("Expense Analysis by Category")
plt.xticks(rotation=30)
plt.show()