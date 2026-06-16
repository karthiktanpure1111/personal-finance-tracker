from database import get_transactions


def view_transactions():

    transactions = get_transactions()

    if not transactions:

        print(
            "No Transactions Found"
        )

        return

    print("\n===== Transactions =====")

    for transaction in transactions:

        print(
            f"ID:{transaction[0]} | "
            f"{transaction[1]} | "
            f"{transaction[2]} | "
            f"{transaction[3]}"
        )


def calculate_balance():

    transactions = get_transactions()

    income = 0
    expense = 0

    for transaction in transactions:

        if transaction[1] == "income":

            income += transaction[2]

        else:

            expense += transaction[2]

    print("\n===== Summary =====")

    print(
        f"Income : {income}"
    )

    print(
        f"Expense: {expense}"
    )

    print(
        f"Balance: {income-expense}"
    )