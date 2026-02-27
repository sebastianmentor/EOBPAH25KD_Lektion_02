""" Ett lite program som hantera lag och fotbollspelare!"""

# Tanken att det ska vara en konstant!
POSISTIONS = {
    "1": "Back", 
    "2": "Mittspelare", 
    "3": "Anfallsspelare",
    "4": "Målvakt"
    }

teams = {
    "Västerås Vikings": [
        {"name": "Erik Storm", "jersy": 7, "pos": "3", "shoe_size": 44},
        {"name": "Liam Frost", "jersy": 14, "pos": "4", "shoe_size": 46},
        {"name": "Noah Blad", "jersy": 9, "pos": "2", "shoe_size": 43},
        {"name": "Felix Grön", "jersy": 22, "pos": "1", "shoe_size": 45},
    ],
    "Uppsala Unicorns": [
        {"name": "Alice Stjärna", "jersy": 10, "pos": "3", "shoe_size": 41},
        {"name": "Maja Skog", "jersy": 17, "pos": "2", "shoe_size": 39},
        {"name": "Tilda Måne", "jersy": 3, "pos": "1", "shoe_size": 40},
        {"name": "Elin Flod", "jersy": 1, "pos": "4", "shoe_size": 42},
    ],
    "Göteborg Gorillas": [
        {"name": "Anton Berg", "jersy": 8, "pos": "3", "shoe_size": 45},
        {"name": "Lukas Palm", "jersy": 4, "pos": "1", "shoe_size": 44},
        {"name": "Oscar Nil", "jersy": 12, "pos": "2", "shoe_size": 43},
        {"name": "Hugo Ström", "jersy": 30, "pos": "4", "shoe_size": 47},
    ],
    "Lund Lightning": [
        {"name": "Sara Falk", "jersy": 5, "pos": "2", "shoe_size": 38},
        {"name": "Clara Sol", "jersy": 16, "pos": "3", "shoe_size": 39},
        {"name": "Emil Nyström", "jersy": 11, "pos": "1", "shoe_size": 42},
        {"name": "Viktor Ås", "jersy": 24, "pos": "4", "shoe_size": 44},
    ],
}


while True:
    print("1. Skapa nytt lag")
    print("2. Hantera lag")
    print("0. Avsluta")


    choice = input("Ange önskat val: ")

    if choice == "1":
        new_team = input("Ange nytt fotbollslag:")

        if new_team not in teams:
            teams[new_team] = []
        
        else:
            print("Laget finns redan! Opsii!!")

    elif choice == "2":
        team_name = input("Ange lag att hantera: ")

        if team_name not in teams:
            print("Laget fanns inte! Skapa det först om du vill kunna hantera det!")
            continue
        
        current_team = teams[team_name]
        while True:
            print("1. Lägg till spelare")
            print("2. Hitta spelare")
            print("3. Skriv ut laget")
            print("4. Kicka ur spelare")
            print("0. Gå tillbaka")

            second_choice = input("Gör ditt val: ")

            if second_choice == "1":
                name = input("Ange namn")
                jersy = input("Ange tröjnummer")

                if not jersy.isdigit():
                    print("Tröjnummer måste vara ett tal! Vi går tillbaka!")
                    continue
                
                for input_choice, pos in POSISTIONS.items():
                    print(f"{input_choice}. {pos}")

                posistion = input("Ange position: ")

                if posistion not in POSISTIONS:
                    print("Ogiltlig position! vi går tillbaka!")
                    continue
                
                shoe_size = input("Ange skostorlek")

                # new_player = dict(name=name, jersy=jersy, pos=posistion, shoe_size=shoe_size)

                new_player = {
                    "name":name, 
                    "jersy":jersy, 
                    "pos":posistion, 
                    "shoe_size":shoe_size
                    } 
                
                # Lägger till spelare i nuvande lags lista med spelare
                current_team.append(new_player)

            elif second_choice == "2":
                player_name_to_search_for = input("Ange namn på spleare att söka efter!")

                for player in current_team:
                    if player["name"] == player_name_to_search_for:
                        print("Spelaren hittades! Här kommer den:")
                        print(player)
                        break
                else:
                    print(f"Spelaren {player_name_to_search_for} fanns inte i laget!")


            elif second_choice == "3":
                
                print(team_name)
                for player in current_team:
                    print("Tröjnummer:", player["jersy"])
                    print(f"\tNamn:       {player["name"]}")
                    print(f"\tPosition:   {player["pos"]}")
                    print(f"\tSkostorlek: {player["shoe_size"]}")


            elif second_choice == "4":
                player_name_to_delete = input("Ange namn på spleare vi önskar kicka ur laget:")

                for index, player in enumerate(current_team):
                    if player["name"] == player_name_to_delete:
                        print("Spelaren hittades! Nu åker han ut!")
                        current_team.pop(index)
                        break
                else:
                    print(f"Skelaren {player_name_to_delete} fanns inte i laget!")

            elif second_choice == "0":
                break
                 

    elif choice == "0":
        break

    else:
        print("Ogiltlig val!!")
