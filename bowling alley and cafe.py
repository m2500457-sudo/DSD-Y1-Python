def booking_system():
    total = 0
    adult = 15
    child = 5
    day = input("Please input the date you would like to book for in the format 00/00/0000.")



    running = True
    while running:

        try:
            adults = int(input("Please enter the number of adults for the booking (16+)."))
            children = int(input("Please enter the number of children for the booking (<16)."))
            games = int(input("Please input the number of games of bowling you would like to play."))
        except:
            print("Please only enter a number.")
        else:
            running = False

    games = int(games)
    adults = int(adults)
    children = int(children)

    adult_total = (adult * adults)
    children_total = (child * children)
    tix_total = (adult_total + children_total)
    total = (games * tix_total)

    if adults > 3 or children > 5: 
        print("You qualify for a 20% discount!")
        total = total * 0.80
        print("***************************SUMMARY********************************")
        print("There are" ,adults, "adults and" ,children, "kids on this booking.")
        print("You are going to play" ,games, "games of bowling.")
        print("You have a discount of 20%.")
        print("You are booked for" ,day, ".")
        print("You overall total is" ,total,)
    else:
        print("***************************SUMMARY********************************")
        print("There are" ,adults, "adults and" ,children, "kids on this booking.")
        print("You are going to play" ,games, "games of bowling.")
        print("You are booked for" ,day, ".")
        print("You overall total is" ,total,)

booking_system()