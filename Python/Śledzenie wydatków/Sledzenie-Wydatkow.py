expenses = []

def show_expenses(month):
    for expense_amount, expemse_type, expense_month in expenses:
        if expense_month == month:
            print(f'{expense_month} - {expemse_type}')

def add_expense(month):
    print()
    expense_amount = int(input("Podaj kwotę [zł]: "))
    expense_type = input("Podaj typ wydatku (jedzenie, rozrywka, dom, inny): ")

    expense = (expense_amount, expense_type, month)
    expenses.append(expense)

while True:
    print()
    month = int(input("Wybierz miesiąc[1-12]:"))

    if month == 0:
        break

    while True:
        print()
        print("0. Powrót do wyboru miesiąca")
        print("1. Wyświetl wszystkie wydatki")
        print("2. Dodaj wydatek")
        choice = int(input("Wybierz opcję:"))

        if choice == 0:
            break

        if choice == 1:
            print()
            show_expenses(month)

        if choice == 2:
            print()
            add_expense(month)

