from finance import (
    add_transaction,
    update_existing_transaction,
    delete_existing_transaction
)

from reports import (
    view_transactions,
    calculate_balance
)

from database import (
    close_db
)

while True:

    print(
        "\n===== PERSONAL FINANCE TRACKER ====="
    )

    print(
        "1. Add Transaction"
    )

    print(
        "2. View Transactions"
    )

    print(
        "3. Calculate Balance"
    )

    print(
        "4. Update Transaction"
    )

    print(
        "5. Delete Transaction"
    )

    print(
        "6. Exit"
    )

    choice = input(
        "Choose: "
    )

    if choice == "1":

        add_transaction()

    elif choice == "2":

        view_transactions()

    elif choice == "3":

        calculate_balance()

    elif choice == "4":

        update_existing_transaction()

    elif choice == "5":

        delete_existing_transaction()

    elif choice == "6":

        close_db()

        print(
            "Goodbye"
        )

        break

    else:

        print(
            "Invalid Choice"
        )