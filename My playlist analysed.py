import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\Users\M2500457\OneDrive - Middlesbrough College\Documents\GitHub\DSD-Y1-Python\chilled_clean_unique_final(in).csv")
#CHANGE THE FILE LOCATION BEFORE USE
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

def bar_chart_decades(df):
    #This code creates a bar chart of what decades the songs were released and how many are from that decade in that playlist.

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
#bar_chart_decades(df)

def bar_chart_year(df):

    #This code creates a bar chart of what decades the songs were released and how many are from that decade in that playlist.

    df = df.dropna(subset=["Release Year"])

    df["Release Year"] = df["Release Year"].astype(int)

    
    

    decade_counts = df["Release Year"].value_counts().sort_index()

    plt.figure()
    decade_counts.plot(kind="bar")

    plt.xlabel("Year")
    plt.ylabel("Number of Songs")
    plt.title("Number of Songs by Decade in 'Chilled' Playlist")

    plt.xticks(rotation=45)

    plt.tight_layout()
    plt.show()
#bar_chart_year(df)

def newest_and_oldest_tracks():
    #This code prints the name and release year of the two oldest tracks in the playlist.

    df_clean = df.dropna(subset=["Release Year"]).copy()
    df_clean["Release Year"] = pd.to_numeric(df_clean["Release Year"], errors="coerce")
    df_clean = df_clean.dropna(subset=["Release Year"])

    oldest_index = df_clean["Release Year"].idxmin()
    newest_index = df_clean["Release Year"].idxmax()

    oldest_track = df_clean.loc[oldest_index]
    newest_track = df_clean.loc[newest_index]

    print("Oldest Track:")
    print(oldest_track["Track Name"], "-", oldest_track["Release Year"])

    print("\nNewest Track:")
    print(newest_track["Track Name"], "-", newest_track["Release Year"])
#newest_and_oldest_tracks()

def average_release_year_per_genre():

    dff = df.groupby("Genre")["Release Year"].mean().sort_values()

    x = dff.index
    y = round(dff)

    plt.bar(x, y)
    plt.xticks(rotation=45)
    plt.ylim(y.min() - 5, y.max() + 5)
    plt.show()
#average_release_year_per_genre()

def modern_bias():
    # This entire function was made by AI decided to keep to show how data is cleaned and prepped.
    df_clean = df.dropna(subset=["Release Year"]).copy()
    df_clean["Release Year"] = pd.to_numeric(df_clean["Release Year"], errors="coerce")
    df_clean = df_clean.dropna(subset=["Release Year"])
    df_clean["Release Year"] = df_clean["Release Year"].astype(int)
    df_clean["Decade"] = (df_clean["Release Year"] // 10) * 10

    total = len(df_clean)
    modern_counts = df_clean["Decade"].value_counts().reindex([2010, 2020], fill_value=0)
    modern_percent = (modern_counts / total) * 100

    print("Total songs (with a release year):", total)
    print("\nPercent from 2010s and 2020s:")
    for decade, pct in modern_percent.items():
        print(f"{decade}s: {pct:.1f}%")

    plt.figure()
    modern_percent.index = modern_percent.index.astype(str) + "s"
    modern_percent.plot(kind="bar")
    plt.xlabel("Decade")
    plt.ylabel("Percentage of Songs (%)")
    plt.title("Does the playlist favour modern music?")
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.show()
#modern_bias()


def years():
    print("HI")


def interactive(df):

    def decades(df):

        df = df.dropna(subset=["Release Year"])
        df["Release Year"] = df["Release Year"].astype(int)

        user_input = input("Enter a decade (e.g., 1990s, 2000s, 2010s): ").strip()

        if not user_input.endswith("s") or not user_input[:-1].isdigit():
            print("Invalid format. Please use format like 1990s.")
            return None

        decade_start = int(user_input[:-1])
        decade_end = decade_start + 9

        filtered = df[
            (df["Release Year"] >= decade_start) &
            (df["Release Year"] <= decade_end)
        ]

        if filtered.empty:
            print(f"No songs found from the {user_input}.")
            return None

        print(f"\nSongs from the {user_input}:\n")

        print(
            filtered[["Track Name", "Artist", "Album", "Release Year"]]
            .to_string(index=False)
        )

        return filtered


    option = input("Would you like to use decades or years?")
    if option == "Decades" or option == "decades":
        decades(df)
    elif option == "Years" or option == "years":
        years()
    else:
        print("Error! Please try again")

interactive(df)