import pandas as pd
import matplotlib.pyplot as plt
import math
import datetime
import numpy as np

df = pd.read_csv(r"C:\Users\M2500457\OneDrive - Middlesbrough College\Documents\GitHub\DSD-Y1-Python\Game_Shop_Sales_300_Rows.csv")

def most_purchased_game():

    #This code creates a bar chart of how many untis each game has sold.

    units_per_game = df.groupby("Game Title")["Units Sold"].sum()
    #This code groups togther the name of the game and the amount of times i was sold.
    #This is important because each transaction can have more than 1 unit sold.
    
    plt.figure(figsize=(8,5))
    units_per_game.plot(kind="bar")
    
    plt.title("Most Purchased Games")
    plt.xlabel("Game Title")
    plt.ylabel("Number of Purchases")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
#most_purchased_game()

def most_purchased_genre():

    #This code creates a pie chart of all of the different genres as what portion they sold.

    units_per_genre = df.groupby("Category")["Units Sold"].sum()
   
    units_per_genre.plot(kind="pie")
    plt.title("Most Purchased Genres")
    plt.xlabel("Genres")
    plt.ylabel("")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
#most_purchased_genre()

def average_price_per_genre():

    avg_price = df.groupby("Category")["Price"].mean()

    plt.figure(figsize=(8,5))
    avg_price.plot(kind="line", marker="o")

    plt.title("Average Price per Genre")
    plt.xlabel("Genres")
    plt.ylabel("Price")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()    
#average_price_per_genre()

def start():

    x = datetime.datetime.now()

    print("Hi! The date and time currently is," ,x,) 
    print(f"{"Main Menu":*^60}")
    print(f"{"1) Most Purchased Game (Bar Chart)":*^60}")
    print(f"{"2) Most Purchased Genre (Pie Chart)":*^60}")
    print(f"{"3)Average Price Per Genre (Line Chart)":*^60}")
    print(f"{"3) Average Price Per Genre (Line Chart)":*^60}")


    while True:
        try:
            choice = int(input("Enter a number between 1 and 3: "))
            
            if 1 <= choice <= 3:
                break
            else:
                print("Number must be between 1 and 3.")

        except ValueError:
            print("Invalid input. Please enter a number.")

    if choice == 1:
        print("You entered choice 1, loading...")
        most_purchased_game()
    elif choice == 2:
        print("You entered choice 2, loading...")
        most_purchased_genre()
    elif choice == 3:
        print("You entered choice 3, loading...")
        average_price_per_genre()
    else:
        print("")

start()