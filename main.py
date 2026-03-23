from DATA.input_data import get_expenses
from DATA.class_methods import Expense
from DATA.SQL import create_connection, create_table, insert_into_table

from LOGIC.calculations import (
    product_above_below_average_price,
    average_per_category,
    category_above_average_price,
    product_above_average_price,
    max_min_category,
    max_min_price_product
)

from LOGIC.utility import (
    search_shopping_date,
    budget_checker,
    search_by_month
)


def analyze_expenses(expenses):

    print("\n------ GENERAL ANALYSIS ------")

    total, number_items, average = Expense.total_amount(expenses)

    print(f"Total spent: {total}")
    print(f"Number of items: {number_items}")
    print(f"Average price: {average}")

    print("\n------ CATEGORY TOTALS ------")

    categories = Expense.total_per_category(expenses)

    for cat, info in categories.items():
        print(f"{cat} -> Total: {info['total']} | Items: {info['items']}")

    print("\n------ PRODUCT VS GLOBAL AVERAGE ------")

    above, below = product_above_below_average_price(expenses)

    print("\nAbove average:")
    for product, price in above.items():
        print(product, "->", price)

    print("\nBelow average:")
    for product, price in below.items():
        print(product, "->", price)

    print("\n------ AVERAGE PER CATEGORY ------")

    averages = average_per_category(expenses)

    for cat, avg in averages.items():
        print(cat, "->", avg)

    print("\n------ CATEGORY VS GLOBAL AVERAGE ------")

    cat_above, cat_below = category_above_average_price(expenses)

    print("\nCategories above global average:")
    for cat, avg in cat_above.items():
        print(cat, "->", avg)

    print("\nCategories below global average:")
    for cat, avg in cat_below.items():
        print(cat, "->", avg)

    print("\n------ PRODUCT VS GLOBAL AVERAGE (SECOND METHOD) ------")

    above, below = product_above_average_price(expenses)

    print("\nProducts above global average:")
    for product, price in above.items():
        print(product, "->", price)

    print("\nProducts below global average:")
    for product, price in below.items():
        print(product, "->", price)

    print("\n------ MAX / MIN CATEGORY ------")

    max_cat, min_cat, max_total, min_total, max_items, min_items = max_min_category(expenses)

    print(f"Highest spending category: {max_cat} -> {max_total} ({max_items} items)")
    print(f"Lowest spending category: {min_cat} -> {min_total} ({min_items} items)")

    print("\n------ MOST / LEAST EXPENSIVE PRODUCT ------")

    top_price, top_product, top_category, low_price, low_product, low_category = max_min_price_product(expenses)

    print(f"Most expensive product: {top_product} ({top_category}) -> {top_price}")
    print(f"Cheapest product: {low_product} ({low_category}) -> {low_price}")


def main():

    conn = create_connection()
    create_table(conn)

    while True:

        print("\n===== EXPENSE TRACKER =====")
        print("1 - Enter new expenses")
        print("2 - Search shopping by date")
        print("3 - Budget checker")
        print("4 - Search expenses by month")
        print("5 - Exit")

        choice = input("Choose option: ").strip()

        if choice == "1":

            expenses = get_expenses()

            if not expenses:
                print("No expenses entered.")
                continue

            while True:
                save = input("Save expenses to database? (y/n): ").strip().lower()

                if save == "y":
                    insert_into_table(conn, expenses)
                    print("Expenses saved to database.")
                    break
                elif save == "n":
                    print("Expenses were not saved.")
                    break
                else:
                    print("Invalid option.")

            analyze_expenses(expenses)

        elif choice == "2":

            result = search_shopping_date(conn)

            if not result:
                continue

            shopping_date, user, total = result

            print(f"\nShopping date: {user}")
            print(f"Total spent: {total}")

            for date, products in shopping_date.items():
                for product, expense in products.items():
                    print(f"{product} | {expense.category} | {expense.amount}")

        elif choice == "3":

            result = budget_checker(conn)

            if not result:
                continue

            budgets, difference = result

            for date, products in budgets.items():
                for product, expense in products.items():
                    print(f"{product} | {expense.category} | {expense.amount}")

            if difference >= 0:
                print(f"You are within budget. Remaining: {difference}")
            else:
                print(f"You exceeded your budget by {-difference}")

        elif choice == "4":

            result = search_by_month(conn)

            if not result:
                continue

            month, user, monthly_spent = result

            print(f"\nMonth: {user}")
            print(f"Total spent: {monthly_spent}")

            for category, products in month.items():
                print(f"\n{category}")
                for product, total in products.items():
                    print(f"{product} -> {total}")

        elif choice == "5":
            print("Goodbye.")
            break

        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()