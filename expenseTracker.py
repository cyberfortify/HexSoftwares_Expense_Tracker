import csv
import datetime
import os

#Check the csv file and open it
def initialize_file():
    if not os.path.exists('expenses.csv'):
        with open('expenses.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Date', 'Category', 'Amount', 'Description'])  # Headers for the CSV file

#Add expense to csv file
def add_expense(category, amount, description):
    try:
        amount = float(amount)  
        date = datetime.datetime.now().strftime('%Y-%m-%d')  
        expense = [date, category, amount, description]
        
        # Append the expense to the CSV file
        with open('expenses.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(expense)
        print("Expense added successfully!")
    except ValueError:
        print("Invalid amount. Please enter a numeric value.")

#View all expenses
def view_expenses():
    with open('expenses.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)  #Skip the header
        for row in reader:
            print(f"Date: {row[0]}, Category: {row[1]}, Amount: ₹{float(row[2]):,.2f}, Description: {row[3]}")

#Calculate total expenses
def calculate_total():
    total = 0
    with open('expenses.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)  #Skip the header
        for row in reader:
            total += float(row[2])
    return total

#Calculate total expenses by category
def calculate_total_by_category():
    category_totals = {}
    with open('expenses.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)  #Skip the header
        for row in reader:
            category = row[1].strip()
            amount = float(row[2])
            if category in category_totals:
                category_totals[category] += amount
            else:
                category_totals[category] = amount
    for category, total in category_totals.items():
        print(f"{category}: ₹{total:,.2f}")


def main():
    initialize_file()  #call the initialize file method to check the csv file 

    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Calculate Total Expenses")
        print("4. View Total Expenses by Category")
        print("5. Exit")
        
        choice = input("Choose an option (1-7): ")
        
        if choice == '1':
            category = input("Enter category: ")
            amount = input("Enter amount: ")
            description = input("Enter description: ")
            add_expense(category, amount, description)
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            print(f"Total Expenses: ₹{calculate_total():,.2f}")
        elif choice == '4':
            calculate_total_by_category()
        elif choice == '5':
            print("Exiting Expense Tracker.")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()