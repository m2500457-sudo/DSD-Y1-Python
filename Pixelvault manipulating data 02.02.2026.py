import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv (r"C:\Users\M2500457\OneDrive - Middlesbrough College\Documents\GitHub\DSD-Y1-Python\pixelvault game sales.csv")

def Task_1():

    print(df.tail())
    #Prints the last 5 values of the dataframe.

    print(df.head())
    #Prints the first 5 values of the dataframe.

    print(df.info())
    #Print information about the dataset.

def Task_3():

    test = df.isna().sum()
    print(test)
    #This code shows what collums have some missing data by printing them out with a 0.

    print(df.duplicated())

    #This checks to see if there are any incorrect calculations.
    is_correct = df['total_sale'].equals(df['price'] * df['quantity'])
    print(f"All calculations correct: {is_correct}")
    #This prints out the incorrect calculations.
    discrepancies = df[df['total_sale'] != (df['price'] * df['quantity'])]
    print(discrepancies)

def Task_4():

    test = df["game_title"]   
    print(test.mode())
    #This code prints the most common game name in the database.

    testing = df.groupby ("category") ["price"].max()
    print(testing)
    #This code groups the two colums together and shows the columns with the highest value in the database.

    tested = df["total_sale"]
    print(tested.max())
    #This code prints of the highest total sale value.

    tester = df["price"]
    mean = tester.mean()
    rounded = (mean.__round__,2)
    #This code finds the average price of games sold in the datset, it then rounds and prints out the number.

def scatter_plot():
    data1 = df["price"]
    data2 = df["category"]
    plt.scatter(data2, data1)
    plt.title("Realtionship game categorys and prices")
    plt.xlabel("Category")
    plt.ylabel("Price (£)")
    plt.show()

scatter_plot()

