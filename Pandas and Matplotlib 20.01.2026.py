import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\Users\M2500457\OneDrive - Middlesbrough College\Python\retail_sales_data.csv")
#This line of code multiplies two different colums into a new one.
new_category = df["Total Sale"] = df["price"] * df["quantity"]

def total_revenues(new_category):

    #This section of code selects the products and their total revenue and then prints them out 
    total_revenue_product = df.groupby("product")["Total Sale"].sum()
    total_revenue_category = df.groupby("category")["Total Sale"].sum()
    print (total_revenue_category)
#total_revenues(new_category)

def top_3_categories(new_category):

    top_3_categories = (
        df.groupby("category")["Total Sale"]
        .sum()
        .sort_values(ascending=False)
        .head(3)
    )

    print(top_3_categories)
#top_3_categories(new_category)

def bar_chart(df, new_category,):
        
    df.plot(kind="bar", x="product", y="Total Sale", title="Total Sales by Product")
    plt.show()
#This function createsa a simple bar chart of total sales and the products being sold.
bar_chart(df, new_category,)


def daily_revenue(df,):
    