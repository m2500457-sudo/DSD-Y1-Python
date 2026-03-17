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

def units_per_month():
    
    df["Date"] = pd.to_datetime(df["Date"], dayfirst=True)
    #This line of code converts the date column into datetime.

    monthly_units = (
    df.groupby(df["Date"].dt.to_period("M"))["Units Sold"]
    .sum()
    .reset_index()
)

    monthly_units["Date"] = monthly_units["Date"].astype(str)
    plt.bar(monthly_units["Date"], monthly_units["Units Sold"])
    #This line of code converts the data to a string so that it will show the dates in the bar chart.
    plt.xlabel("Month")
    plt.ylabel("Units Sold")
    plt.title("Units Sold per Month")
    plt.show()
#units_per_month()

def start():
    #This function is what starts the program, it has two functions for getting the users first and last name, both with input validation.
    #The third function prints the menu off and handles the users decisions.

    def first_name():

        #This function gets the users first name.
        #The while loop ensure the user can only input letters for their name
        while True:
            try:
                name = input("Please input your first name.")

                if name.isalpha():
                    break
                else:
                    print("Please enter your name using letters.")
            except ValueError:
                print("Please enter your name using letters.")
        return name.capitalize()

    def last_name():

        #This function gets the users last name.
        #The while loop ensure the user can only input letters for their name
        while True:
            try:
                last_name = input("Please input your last name.")

                if last_name.isalpha():
                    break
                else:
                    print("Please enter your name using letters.")
            except ValueError:
                print("Please enter your name using letters.")
        return last_name.capitalize()

    def main_menu():

        name = first_name()
        name_last = last_name()

        x = datetime.datetime.now()

        print("Hi!" ,name, name_last, "The date and time currently is," ,x,) 
        print(f"{"Main Menu":*<60}")
        print(f"{"1) Most Purchased Game (Bar Chart)":*<60}")
        print(f"{"2) Most Purchased Genre (Pie Chart)":*<60}")
        print(f"{"3) Average Price Per Genre (Line Chart)":*<60}")
        print(f"{"4) Total Sales Per Month (Bar Chart)":*<60}")

        with open("Programming_project_at_college.txt", "a") as f:
            f.write(f"User's name is {name} {name_last} date and time is {x}.\n")

        while True:
            try:
                choice = int(input("Enter a number between 1 and 4: "))
                
                if 1 <= choice <= 4:
                    break
                else:
                    print("Number must be between 1 and 4.")

            except ValueError:
                print("Invalid input. Please enter a number.")

        if choice == 1:
            print("You entered choice 1, loading...")
            with open("Programming_project_at_college.txt", "a") as f:
                f.write("The user chose to have a bar chart created of the most purchased game.\n")
            most_purchased_game()
        elif choice == 2:
            print("You entered choice 2, loading...")
            with open("Programming_project_at_college.txt", "a") as f:
                f.write("The user chose to have a pie chart created of the most purchased genre.\n")
            most_purchased_genre()
        elif choice == 3:
            print("You entered choice 3, loading...")
            with open("Programming_project_at_college.txt", "a") as f:
                f.write("The user chose to have a line chart created of the average price per genre.\n")
            average_price_per_genre()  
        elif choice == 4:
            print("You entered choice 3, loading...")
            with open("Programming_project_at_college.txt", "a") as f:
                f.write("The user chose to have a bar chart for the total amount of units sold per month.\n")
            units_per_month()

        else:
            print("Error, please restart program.")


    main_menu()
#This function contains function such as First_Name, Last_Name and Main_Menu, these functions are needed to start the program

start()
#This function starts the program.