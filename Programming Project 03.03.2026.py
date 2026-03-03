import pandas as pd
import matplotlib.pyplot as plt
import math

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

    average_per_genre = df.groupby("Category")["Units Sold"].mean()
    
    average_per_genre.plot(kind="bar")
    plt.title("Average Price per Genre")
    plt.xlabel("Genres")
    plt.ylabel("Price")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
average_price_per_genre()

