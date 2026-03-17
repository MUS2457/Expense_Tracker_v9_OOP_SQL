from DATA.class_methods import Expense

def get_product_name():
    while True:
        product_name = input("Enter product name , 'done' to finish or 'exit' to quit: ").strip()

        if product_name.lower() in ['done', 'exit']:
            return product_name.lower()
        elif not product_name or any(char.isdigit() for char in product_name):
            print("Invalid product name")
            continue

        return product_name.capitalize()

def get_product_category(product):
    while True:
        category = input(f"Enter product category of the product  {product}: ").strip()

        if not category or any(letter.isdigit() for letter in category):
            print("Invalid product category")
            continue
        return category.upper()

def get_product_price(product, category):
    while True:
       try:
           price = float(input(f"Enter product price of the product  {product} "
                               f"from category {category}: "))

           if price < 0:
               print("product price cannot be negative")
               continue
           return price

       except ValueError:
           print("Invalid product price")
           continue # but not required


def get_expenses() :
    shopping_expenses = []

    while True:
        product_name = get_product_name()

        if product_name == "exit" :
            print("Exit the program")
            break
        elif product_name == "done" :
            break

        category = get_product_category(product_name)
        price = get_product_price(product_name, category)

        expense = Expense(product_name, category, price)

        shopping_expenses.append(expense)

    return shopping_expenses
