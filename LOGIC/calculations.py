from DATA.class_methods import Expense

def product_above_below_average_price(expenses):
    above = {}
    below = {}

    if not expenses:
        return above, below

    total, number_items, average = Expense.total_amount(expenses)

    for expense in expenses:

        if expense.amount > average:
            above[expense.product] = expense.amount
        else:
            below[expense.product] = expense.amount

    return above, below

def average_per_category(expenses):
    averages = {}

    if not expenses:
        return averages

    categories = Expense.total_per_category(expenses)

    for cat, info in categories.items():

        averages[cat] = round(info["total"] / info["items"] ,2)

    return averages


def category_above_average_price(expenses):
    above = {}
    below = {}

    if not expenses:
        return above, below

    averages = average_per_category(expenses)
    total, number_items, tl_average = Expense.total_amount(expenses)

    for cat, average in averages.items():

        if average > tl_average:
            above[cat] = average
        else:
            below[cat] = average

    return above, below

def product_above_average_price(expenses):
    above = {}
    below = {}

    if not expenses:
        return above, below

    total, number_items, tl_average = Expense.total_amount(expenses)

    for expense in expenses:

        if expense.amount > tl_average:
            above[expense.product] = expense.amount
        else:
            below[expense.product] = expense.amount

    return above, below

def max_min_category(expenses):

    if not expenses:
        return None, None

    categories = Expense.total_per_category(expenses)

    max_category = max(categories, key=lambda cat: categories[cat]["total"])
    min_category = min(categories, key=lambda cat: categories[cat]["total"])

    return (
        max_category,
        min_category,
        categories[max_category]["total"],
        categories[min_category]["total"],
        categories[max_category]["items"],
        categories[min_category]["items"]
    )


def max_min_price_product(expenses):
    shopping = []

    for expense in expenses:
        shopping.append((expense.amount, expense.product, expense.category))

    if not shopping:
        return None, None, None, None, None, None

    top_price, top_product, top_category = max(shopping)
    lowest_price, lowest_product, lowest_category = min(shopping)

    return (
        top_price, top_product, top_category,
        lowest_price, lowest_product, lowest_category
    )

def max_min_price_product_v2(expenses):

    if not expenses:
        return None, None, None, None, None, None

    max_expense = max(expenses, key=lambda e: e.amount)
    min_expense = min(expenses, key=lambda e: e.amount)

    return (
        max_expense.amount,
        max_expense.product,
        max_expense.category,
        min_expense.amount,
        min_expense.product,
        min_expense.category
    )