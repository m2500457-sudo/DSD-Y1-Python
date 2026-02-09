import matplotlib.pyplot as plt
import pandas as pd

#This code is from Monday 09th February, there is a csv to go alongside the code, the csv file contains data about sales at amazon, the code below
#explores the csv, creating charts, etc to explain and contextualise the data.

df = pd.read_csv(r"C:\Users\M2500457\OneDrive - Middlesbrough College\Documents\GitHub\DSD-Y1-Python\amazon_sales_dataset.csv")
#print(df.head())

def sales_performance():
    #This code wil calculate the total of all the sales:
    total = df["total_revenue"].sum()
    rounded = round(total, 2)
    print(rounded)

    #This code will calculate the average sale:
    average = df["total_revenue"].mean()
    end = round(average, 2)
    print(end)
#sales_performance()

def bar_chart_category():
    #This code creates a bar chart that displays the amount of products sold in eahc category.
    grouped = df.groupby("product_category")["quantity_sold"].sum()
    x = grouped.index
    y = grouped.values

    plt.bar(x,y)
    plt.title("Quantity Sold per Product Category")
    plt.ylabel("Quantity Sold")
    plt.xlabel("Product Category")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
#bar_chart_category()

def sales_by_region(df):
    #This code creates a bar chart that represents the sales in each region.
    grouped = df.groupby("customer_region")["total_revenue"].sum()

    x = grouped.index
    y = grouped.values

    plt.bar(x, y)
    plt.xlabel('Region')
    plt.ylabel('Total Revenue')
    plt.title('Sales by Region')
    plt.show()
#sales_by_region(df)