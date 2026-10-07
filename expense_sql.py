from calendar import month
from unicodedata import category

import mysql.connector

con=mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="expense"
)
cursor=con.cursor()
print("Connected successfully!")

def add_expense():
    amount = float(input("Amount: "))
    date = input("Date (YYYY-MM-DD): ")
    category = int(input("Category ID: "))
    payment = input("Payment method: ")

    sql = "INSERT INTO expenses (amount,date,category_id,payment_method) VALUES (%s,%s,%s,%s)"
    cursor.execute(sql, (amount, date, category, payment))
    con.commit()

    print("Expense added!")

def add_category():
    name = input("Category name: ")

    cursor.execute(
        "INSERT INTO categories (name) VALUES (%s)",
        (name,)
    )
    con.commit()

    print("Category added!")

def view_expenses():
    cursor.execute("""
        SELECT expenses.id, amount, date, categories.name, payment_method
        FROM expenses
        JOIN categories ON expenses.category_id = categories.id
    """)

    rows = cursor.fetchall()

    print("\n" + "=" * 50)
    print("              EXPENSE BILL")
    print("=" * 50)
    print("ID   Date          Category       Payment       Amount")
    print("-" * 50)

    for row in rows:
        print(f"{row[0]:<4} {row[2]}    {row[3]:<14} {row[4]:<13} ₹{row[1]:.2f}")

    print("=" * 50)

def monthly_total():
    month = input("Enter month (YYYY-MM): ")

    cursor.execute(
        "SELECT SUM(amount) FROM expenses WHERE DATE_FORMAT(date,'%Y-%m')=%s",(month,)
    )

    print("Total:", cursor.fetchone()[0] or 0)

def category_total():
    category = input("Category name: ")
    month = input("Month (YYYY-MM): ")

    cursor.execute("""
        SELECT SUM(amount)
        FROM expenses
        JOIN categories ON expenses.category_id = categories.id
        WHERE categories.name=%s AND DATE_FORMAT(date,'%Y-%m')=%s
    """, (category, month))

    print("Total:", cursor.fetchone()[0] or 0)

while True:
    print("\n1. Add Expense")
    print("2. Add Category")
    print("3. View Expenses")
    print("4. Monthly Total")
    print("5. Category Total")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        add_category()
    elif choice == "3":
        view_expenses()
    elif choice == "4":
        monthly_total()
    elif choice == "5":
        category_total()
    elif choice == "6":
        break
    else:
        print("Invalid choice")