

accounts = {
    "1234": {
        "saldo":50,
        "transactions":[(100, "deposit"), (50, "witdraw")] },
        
    "5555": {
        "saldo":250,
        "transactions":[(150, "deposit"), (100, "witdraw"),(200, "deposit")] }
        
}


while True:
    print("PYTHON BANK!")
    print("1. Skapa konto")
    print("2. Logga in")
    print("0. Avsluta")

    choice = input("Ange önskat val: ")

    if choice == "1":
        new_account_number = input("Ange kontonummer: ")
        if not new_account_number.isdigit():
            print("Endas tal kan vara kontonummer!!")

        elif len(new_account_number) != 4:
            print("Vi har fyrsiffriga kontonummer här!")

        elif new_account_number in accounts:
            print("Kontonummer finns redan!")
        
        else:
            accounts[new_account_number] = {"saldo": 0, "transactions":[]}


    elif choice == "2":

        current_account = input("Ange kontonummer: ")

        if current_account not in accounts:
            print("Kontonummer finns inte! Vi går tillbaka till huvuvdmenyn!")
            continue

        # current_account är alltså nuvarande existerande kontonummer
        # accounts[current_account]["saldo"] ger värdet saldo
        # accounts[current_account]["saldo"] = 89 skriver in 89 som värde
        # accounts[current_account]["transactions"] -> [(<belop>, <typ>), ...]

        while True:
            print("1. Sätt in")
            print("2. Ta ut")
            print("3. Visa saldo")
            print("4. Visa transaktioner")
            print("0. Logga ut")

            admin_choice = input("Ange val:")

            if admin_choice == "1":
                pass

            elif admin_choice == "2":
                pass

            elif admin_choice == "3":
                pass

            elif admin_choice == "4":
                pass

            elif admin_choice == "0":
                print("Vi loggar ut nu! Bye bye!")
                break

            else:
                print("Ogiltligt val!")

    elif choice == "0":
       break
        
    else:
        print("Ogiltligt val!")


print("Vi stänger ner banken nu!")