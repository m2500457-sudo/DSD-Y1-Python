import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv(r"C:\Users\M2500457\OneDrive - Middlesbrough College\Documents\GitHub\DSD-Y1-Python\beyonce_tracks.csv")

def bar_chart():
    y = df["danceability"]
    x = df["track_name"]
    plt.bar(x,y)
    plt.title("Beyonce songs and their danceability")
    plt.xlabel("Track Name")
    plt.xticks(rotation=45)
    plt.ylabel("Danceability")
    plt.show()
    #This bar chart shows the ratings for danceability on eahc beyonce song from RENAISSANCE

def pie_chart():
    counts = df["is_explicit"].value_counts()
    plt.pie(
        counts,
        labels=counts.index,
        autopct="%1.1f%%",
        startangle=90
    )
    plt.axis("equal")
    plt.title("All beyonce songs are explicit?")
    plt.show()

def idk():
    album_name = "B'Day Deluxe Edition"
    album_songs = df[df["album_name"] == album_name]

    x = album_songs["track_name"]   # song names
    y = album_songs["loudness"]     # loudness values

    plt.figure(figsize=(10,5))
    plt.bar(x, y)
    plt.xticks(rotation=90)
    plt.title(f"Loudness per Song — {album_name}")
    plt.ylabel("Loudness")
    plt.xlabel("Song")
    plt.show()

idk()
