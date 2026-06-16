from database import (
    add_transaction_db,
    update_transaction,
    delete_transaction
)


def add_transaction():

    transaction_type = input(
        "Income or Expense: "
    ).lower()

    if transaction_type not in [
        "income",
        "expense"
    ]:
        print("Invalid type")
        return

    try:
        amount = float(
            input("Amount: ")
        )
    except ValueError:
        print("Invalid amount")
        return

    category = input(
        "Category: "
    )

    add_transaction_db(
        transaction_type,
        amount,
        category
    )

    print("Transaction Added")


def update_existing_transaction():

    try:

        transaction_id = int(
            input(
                "Transaction ID: "
            )
        )

        transaction_type = input(
            "Income or Expense: "
        ).lower()

        amount = float(
            input("Amount: ")
        )

        category = input(
            "Category: "
        )

        update_transaction(
            transaction_id,
            transaction_type,
            amount,
            category
        )

        print(
            "Transaction Updated"
        )

    except ValueError:

        print(
            "Invalid input"
        )


def delete_existing_transaction():

    try:

        transaction_id = int(
            input(
                "Transaction ID: "
            )
        )

        delete_transaction(
            transaction_id
        )

        print(
            "Transaction Deleted"
        )

    except ValueError:

        print(
            "Invalid ID"
        )