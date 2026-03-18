class Expense:
    def __init__(self, expense, category, amount):
        self.expense = expense
        self.category = category
        self.amount = amount

    @classmethod
    def total_amount(cls, expenses):
        total = 0
        number_items = 0
        if not expenses:
            return None, None, None

        for expense in expenses:
            total += expense.amount
            number_items += 1

        average = round(total / number_items ,1)

        return total, number_items, average

    @classmethod
    def total_per_category(cls, expenses):
        category = {}

        if not expenses:
            return category

        for expense in expenses:

            if expense.category not in category:

                category[expense.category] = {"total": expense.amount , "items": 1 }

            else:
                category[expense.category]["total"] += expense.amount
                category[expense.category]["items"] += 1

        return category
