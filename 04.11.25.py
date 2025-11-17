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


    
Game_System()
        


  
  


    


 

  
