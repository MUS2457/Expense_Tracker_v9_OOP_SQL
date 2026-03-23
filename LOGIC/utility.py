from DATA.class_methods import Expense

def search_shopping_date(conn):
    shopping_date = {}
    cursor = conn.cursor()

    while True:
        user = input("Enter shopping date (YYYY-MM-DD) or 'exit' to quit: ").strip()

        if user.lower() == "exit":
            print("Quitting...")
            break

        cursor.execute(
            "SELECT * FROM expenses WHERE DATE(created_at) = ?",
            (user,)
        )

        rows = cursor.fetchall()

        if not rows:
            print("No shopping records found.")
            continue

        total = 0

        for row in rows:
            product = row["product"]
            category = row["category"]
            amount = row["amount"]
            date = row["created_at"]

            total += amount

            if date not in shopping_date:
                shopping_date[date] = {}

            shopping_date[date][product] = Expense(product, category, amount)

        #for date, name in shopping_date.items():  Looping possible true dic to calculate TL
        #   for product, expense in name.items():
        #       total += expense.amount

        return shopping_date, user, total


def budget_checker(conn):
    cursor = conn.cursor()
    budgets = {}

    while True:

        user_1 = input("Enter first date (YYYY-MM-DD) or 'exit' to quit : ").strip()

        if user_1.lower() == "exit":
            print("Quitting...")
            break

        user_2 = input("Enter second date (YYYY-MM-DD): ").strip()

        cursor.execute(
            "SELECT * FROM expenses WHERE DATE(created_at) BETWEEN ? AND ?",
            (user_1, user_2)
        )

        rows = cursor.fetchall()

        if not rows:
            print("No expense records found.")
            continue

        while True:
            try:
                budget = float(input("Enter budget: "))
                if budget < 0:
                    print("Budget cannot be negative.")
                    continue
                break
            except ValueError:
                print("Invalid budget.")

        total = 0

        for row in rows:
            product = row["product"]
            category = row["category"]
            amount = row["amount"]
            date = row["created_at"]

            total += amount

            if date not in budgets:
                budgets[date] = {}

            budgets[date][product] = Expense(product, category, amount)

        difference = budget - total

        return budgets, difference


def search_by_month(conn):
    cursor = conn.cursor()
    month = {}

    while True:
        user = input("Enter month (YYYY-MM) or 'exit' to quit: ").strip()

        if user.lower() == "exit":
            print("Quitting...")
            break

        cursor.execute("""
            SELECT product, category, amount, SUM(amount) AS total
            FROM expenses
            WHERE strftime('%Y-%m', created_at) = ?
            GROUP BY product, category
            ORDER BY product
        """, (user,))

        rows = cursor.fetchall()

        if not rows:
            print("No expense records found in this specific month.")
            continue
        monthly_spent = 0

        for row in rows:
            product = row["product"]
            category = row["category"]
            total = row["total"]

            monthly_spent += total

            if category not in month:
                month[category] = {}

            month[category][product] = total

        return month, user, monthly_spent


