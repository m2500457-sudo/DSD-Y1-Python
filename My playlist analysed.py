import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\Users\M2500457\OneDrive - Middlesbrough College\Documents\GitHub\DSD-Y1-Python\chilled_clean_unique_final(in).csv")
#print(df.tail())

def bar_chart_artists():
    #This code shows the top ten most frequent arists of the plalist.
    #To show all artists and their own frequancies remove .head(10)
    artist_counts = df["Artist"].value_counts()

    plt.figure()
    artist_counts.plot(kind="bar")

    plt.xlabel("Artist")
    plt.ylabel("Number of Songs")
    plt.title("Artist Frequency in 'Chilled' Playlist")
    plt.xticks(rotation=90)
    plt.show()
#bar_chart_artists()

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
#pie_chart_genre()

def bar_chart_decades():
    #This code creates a bar chart of what decades the songs were released and how many are from that decade in that playlist.
    df = pd.read_csv(r"/Users/alfiecausier/Downloads/chilled_clean_unique_final.csv")

    df = df.dropna(subset=["Release Year"])

    df["Release Year"] = df["Release Year"].astype(int)

    df["Decade"] = (df["Release Year"] // 10) * 10
    df["Decade"] = df["Decade"].astype(str) + "s"

    decade_counts = df["Decade"].value_counts().sort_index()

    plt.figure()
    decade_counts.plot(kind="bar")

    plt.xlabel("Decade")
    plt.ylabel("Number of Songs")
    plt.title("Number of Songs by Decade in 'Chilled' Playlist")

    plt.xticks(rotation=45)

    plt.tight_layout()
    plt.show()
bar_chart_decades()