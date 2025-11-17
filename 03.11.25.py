def music_app():

    #takes the users input and converts into a list 
    user_input = input("Enter your favorite songs ")
    my_list = user_input.split()
    print(my_list)

    #this adds a new item to the list 
    my_list.append("Heated")
    print (my_list)

    #this removes a specific item from the list 
    removed_item = my_list.pop(1)
    print(my_list)

    #this will order the list into alphabetical order 
    sorted_list = sorted(my_list)
    print(sorted_list)

def Cinema_Booking_System():
    print ("Welcome to the cinema.")
    #this creates a list of movies to select from, rather than printing so that it gets the same properties of a list.
    movies = ["1)Dreamgirls", "2)Homecoming", "3)Final Destination", "4)Mean Girls", "5)Barbie"]
    print("1) View all movies.")
    print("2) Add a new movie.")
    print("3) Remove a movie.")
    print("4) Find a movie.")
    print("5) exit.")
    choice = input("Please choose from the menu above")

    if choice == "1":
        print (movies)
    
    elif choice == "2":
        movie = input("Please input your new movie.")
        movies.append(movie)
        print (movies)
    elif choice == "3":
        remove = int(input("Please input the number that you would like to remove"))
        removing = remove - 1
        removed_item = movies.pop(removing)
        print(movies)
    elif choice == "4":
        #this is the same list as before but removed the numbers to find the movie the user inputs.
        movies = ["Dreamgirls", "Homecoming", "Final Destination", "Mean Girls", "Barbie"]
        find = input("Enter the movie you want to look for.")
        if find in movies:
            print(find, "was found in the list.")
        else:
            print(find, "was not found in the list.")
    elif choice == "5":
        choose = input("Are you sure?")
        if choose == "no" or choose == "No":
            Cinema_Booking_System()
        elif choose == "Yes" or choose == "yes":
            print("Ok goodbye!")
        else:
            print("ERROR!")

def Game_System():

    games = [ "1) The Sims 4", "2) Minecraft", "3) GTA5", "4) Fortnite", "5) Fifa"]
    for game in games:
        print(game)

    favorite = input("Do you have a favorite from the list?")
    if favorite == "Yes" or favorite == "yes":
        choose = input("What game is your favorite from the list?")
    elif favorite == "No" or favorite == "no":
        print("Ok, bye!")
    else:
        print("ERROR!")

    if choose == "The Sims 4" or choose == "the sims 4":
        games[0] += (" (Favorite)")
        for game in games:
            print(game)

    elif choose == "Minecraft" or choose == "minecraft":
        games[1] += (" (Favorite)")
        for game in games:
            print(game)
            
    elif choose == "GTA5" or choose == "gta5":
        games[2] += (" (Favorite)")
        for game in games:
            print(game)

    elif choose == "Fortnite" or choose == "fortnite":
        games[3] += (" (Favorite)")
        for game in games:
            print(game)

    elif choose == "FIFA" or choose == "fifa":
        games[4] += (" (Favorite)")
        for game in games:
            print(game)
    else:
        ("Game not found.")

    before = input("Have you played before any games from the list before?")
    if before == "yes" or before == "Yes":
        what = input("What game was it?")
    elif before == "No" or before == "no":
        print("Ok, goodbye!")
    else:
        print("ERROR!")
    
    if what == "The Sims 4" or what == "the sims 4":
        games[0] += (" (Played before)")
        for game in games:
            print(game)
    
    elif what == "Minecraft" or what == "minecraft":
        games[1] += ("(Played before)")
        for game in games:
            print(game)
    
    elif what == "GTA5" or what == "gta5":
        games[2] += (" (Played before)")
        for game in games:
            print(game)

    elif what == "Fortnite" or what == "fortnite":
        games[3] += (" (Played before)")
        for game in games:
            print(game)

    elif what == "FIFA" or what == "fifa":
        games[4] += (" (Played before)")
        for game in games:
            print(game)

    else:
        print("Game not found.")

def main_menu():
    #this function creates a menu for the user to choose from, the menu includeds the functions and the option to end the experiance.
    print("Hi, welcome to the main menu.")
    print("1) My Playlist Manager.")
    print("2) Cinema System.")
    print("3) Video Games.")
    print("4) Exit.")
    choice = input("Please choose from the menu above")

    if choice == "1":
        music_app()
    elif choice == "2":
        Cinema_Booking_System()
    elif choice == "3":
        Game_System()
    elif choice == "4":
        print("Goodbye!")
    else:
        print("ERROR!")

def question():
    #this function will ask the user if they want to go to the main menu, at the menu the user can either user the functions or end the experiance.
    #the function will keep asking and can be stopped if the user inputs "no" or "No" when they are asked "Would you like to go to the main menu?".
    menu = input("Would you like to go to the main menu?")
    if menu == "yes" or menu == "Yes":
        while menu == "Yes" or menu == "yes":
            main_menu()
            menu = input("Would you like to go to the main menu?")
            if menu == "no" or menu == "No":
                print("Ok! Goodbye!")
    elif menu == "no" or menu == "No":
        print("Ok! Goodbye!")






#these two functions are being called.
main_menu()
question()





