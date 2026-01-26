import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv (r"C:\Users\M2500457\OneDrive - Middlesbrough College\Documents\GitHub\DSD-Y1-Python\lego_sets.csv")

test = df["list_price"]
rating = df["star_rating"]

def hidden():

    #this code finds the maximum amount in a column.
    print(test.max())

    #This section of code finds the average amount in a  column and rounds it to 2dp.
    #mean = test.mean()
    #rounded = round(mean, 2)
    #print(rounded)

    #This section of code shows what collums have some missing data by printing them out with a 0.
    #test = df.isna().sum()
    #print(test)
#hidden()

def histogram():

    plt.hist(test, bins=10, edgecolor='black')

    plt.title("Lego Set Prices")
    plt.xlabel("Price (£)")
    plt.ylabel("Frequency")
    plt.show()
#histogram()

def scatter_plot():
    data1 = df["list_price"]
    data2 = df["piece_count"]
    plt.scatter(data1, data2)
    
    plt.title("Realtionship between lego set prices and amount of peices")
    plt.xlabel("Price (£)")
    plt.ylabel("Piece count")
    plt.show()
#scatter_plot()

def theme_bar_chart():

    theme_scores = df.groupby('theme_name')['star_rating'].mean()
    top_10_themes = theme_scores.nlargest(10)


    plt.figure(figsize=(12, 6)) 
    top_10_themes.plot(kind='bar', color='skyblue', edgecolor='black')

  
    plt.title("Top 10 Highest Rated Lego Themes", fontsize=14)
    plt.xlabel("Lego Theme", fontsize=12)
    plt.ylabel("Average Star Rating", fontsize=12)
    plt.xticks(rotation=45) 
    plt.show()
#theme_bar_chart()