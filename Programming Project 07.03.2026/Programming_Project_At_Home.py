import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import math
import datetime

df = pd.read_csv(r"/Users/alfiecausier/Documents/python programs/chilled_clean_unique_final.csv")


def top_ten_artists():
    data = df["Artist"].value_counts()
    data_10 = data.head(10)
    data_10.plot(kind="bar")
    plt.xlabel("Artist")
    plt.ylabel("Artists Frequency in Chilled")
    plt.title("Most Frequent  in 'Chilled' Playlist")
    plt.xticks(rotation=90)
    plt.show()

def pie_chart_genre():
    #This code creaytes a pie chart showing the distribution of the different genres.
    genre_counts = df["Genre"].value_counts()


    plt.figure()
    plt.pie(
        genre_counts,
        labels=genre_counts.index,
        autopct="%1.1f%%",
        startangle=90
    )
    plt.axis("equal")
    plt.title("Genre Distribution in 'Chilled' Playlist")
    plt.show()

def bar_chart_decades(df):

    #This code creates a bar chart of what decades the songs were released and how many are from that decade in that playlist.

    df = df.dropna(subset=["Release Year"])

    df["Release Year"] = df["Release Year"].astype(int)

    df["Decade"] = (df["Release Year"] // 10) * 10
    df["Decade"] = df["Decade"].astype(str) + "s"

    decade_counts = df["Decade"].value_counts().sort_index()

    plt.figure()
    decade_counts.plot(kind="line")

    plt.xlabel("Decade")
    plt.ylabel("Number of Songs")
    plt.title("Number of Songs by Decade in 'Chilled' Playlist")

    plt.xticks(rotation=45)

    plt.tight_layout()
    plt.show()

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
                last_name = input("Please input your first name.")

                if last_name.isalpha():
                    break
                else:
                    print("Please enter your name using letters.")
            except ValueError:
                print("Please enter your name using letters.")
        return last_name.capitalize()

    def main_menu():
        
        #This function prints the menu off and handles the users decisions.

        name = first_name()
        name_last = last_name()


        x = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        print("Welcome to the main menu", name, name_last, "the date and time current are", x, "these are your current options.")

        print("1) Top Ten Artists (Bar Chart).")
        print("2) Genre Distribution (Pie Chart).")
        print("Distribution of Music Per Decade (Line Chart).")

        with open("Programming_project.txt", "a") as f:
            f.write(f"User's name is {name} {name_last} date and time is {x}.\n")

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
            with open("Programming_project.txt", "a") as f:
                f.write("The user chose to have a bar chart created of the top ten artists in the playlist.\n")
            top_ten_artists()
        elif choice == 2:
            print("You entered choice 2, loading...")
            with open("Programming_project.txt", "a") as f:
                f.write("The user chose to have a pie chart created of the different genres in the playlist.\n")
            pie_chart_genre()
        elif choice == 3:
            print("You entered choice 3, loading...")
            with open("Programming_project.txt", "a") as f:
                f.write("The user chose to have a line chart created of the different tracks distributed through out decades in the playlist.\n")
            bar_chart_decades(df)
        else:
            print("Error, please restart program.")

        with open("Programming_project.txt") as f:
            print(f.read())

    main_menu()

start()


