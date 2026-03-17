import pandas as pd
import matplotlib.pyplot as plt
import math 
 
df = pd.read_csv(r"C:\Users\M2500457\OneDrive - Middlesbrough College\Documents\GitHub\DSD-Y1-Python\singers_dataset.csv")

def artist_streams():
    data = df.groupby("Name")["TotalStreamsBillions"].sum()
    data.plot(kind="bar")
    plt.title("Streams per Singer (Billions)")
    plt.xlabel("Singer")
    plt.ylabel("Streams (Billions)")
    plt.show()
#This is a bar chart showing streams per artist (in the billions).
#artist_streams()

def awards_won():
    data = df.groupby("Name")["AwardsWon"].sum()
    data.plot(kind="pie")
    plt.title("Singers and the Distribution of How Many Awards They Have Won")
    plt.show()
#This is a pie chart showing the percentage distribution of awards against artists.
#awards_won()

def average_streams_per_genre():
    data = df.groupby("Genre")["TotalStreamsBillions"].mean()
    data.plot(kind="line")
    plt.title("Genres and Their Streams")
    plt.xlabel("Genre")
    plt.ylabel("Average streams (billions)")
    plt.show()
#This is a line chart showing genres and their average strems (in the billions).
#average_streams_per_genre()

def age_vs_streams():

    plt.scatter(df["Age"], df["TotalStreamsBillions"])
    plt.xlabel("Age")
    plt.ylabel("Streams (Billions)")
    plt.title("Age vs Streams")
    plt.show()
#This is a scatter graph showing the relationship between age and amount of streams.
#age_vs_streams()