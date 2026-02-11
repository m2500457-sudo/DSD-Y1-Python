import datetime
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r'C:\Users\M2500457\OneDrive - Middlesbrough College\Documents\GitHub\DSD-Y1-Python\Core Employer Set Project - Task4A - Data - Summer 2022 1(in).csv')

def mainmenu():
    print("\t\t****Welcome to the Dashboard****")
    print('1) Return all current data')
    print('2) Return data for a specific region')
    print("3) Return data or house sizes for a specific region")
    print("4) A graph for the increases in price over the entire period.")
    return int(input(""))

def alldata():
    print(df)

def region_check(region, startdate, enddate):  # region, startdate, enddate

    df1 = df.loc[:, startdate:enddate]
    df2 = df.loc[:, 'Region Code':'Rooms']

    result = pd.concat([df2, df1], axis=1, join='inner').where(df2["Region"] == region)
    result = pd.DataFrame(result)
    result.dropna(inplace=True)
    print(result)
    ave = df1.mean()
    ave.plot()
    plt.show()
    return result
    
def region_property_type_size():
    valid_entry = False
    
    while not valid_entry:
        location = input("Please enter the name of the region you would like to check: ").strip()
        
        if location in df["Region"].values:
            valid_entry = True
            
            filtered = df[df["Region"] == location]
            
            table = pd.crosstab(filtered["Property Type"], filtered["Rooms"])
            

            table.plot(kind="bar")
            plt.xlabel("Property Type")
            plt.ylabel("Number of Properties")
            plt.title(f"Property Sizes in {location}")
            plt.xticks(rotation=45)
            plt.show()

        else:
            print("Please enter a valid region choice.")

def region_highest_increase():
    month_cols = df.columns[df.columns.get_loc("Rooms") + 1:]
    long_df = df.melt(
        id_vars=["Region Code", "Region", "Property Type", "Rooms"],
        value_vars=month_cols,
        var_name="Month",
        value_name="Percentage")
    
    long_df["Month"] = pd.to_datetime(long_df["Month"], format="%b-%y")
    region_month = (
        long_df.groupby(["Region", "Month"], as_index=False)["Percentage"]
        .mean()
        .sort_values(["Region", "Month"]))
    
    region_increase = region_month.groupby("Region").agg(
        Start_Value=("Percentage", "first"),
        End_Value=("Percentage", "last"))
    region_increase["Increase"] = (
        region_increase["End_Value"] - region_increase["Start_Value"])
    
    region_increase = region_increase.sort_values("Increase", ascending=False)
    

    #This part of the code creates the graph.
    region_increase.plot(kind="bar")
    plt.xlabel("Region")
    plt.ylabel("Percentage Increased")
    plt.title("Price Percentage Across Diffeent Regions.")
    plt.show()

while True:
    x = mainmenu()

    if x == 1:
        alldata()

    elif x == 2:
        while True:
            region = input("Please enter the name of the region you would like to check: ").strip().title()
            if region not in df["Region"].values:
                print("Region not found. Try again.")
                continue

            startdate = input("PLEASE ENTER A START DATE AS MONTH-YEAR e.g. Jan-20: ").strip().title()
            if startdate not in df.columns:
                print("Error start date not found")
                continue

            enddate = input("PLEASE ENTER AN END DATE AS MONTH-YEAR e.g. Mar-20: ").strip().title()
            if enddate not in df.columns:
                print("Error end date not found")
                continue

            region_check(region, startdate, enddate)
            break

    elif x == 3:
        region_property_type_size()

    elif x == 4:
        region_highest_increase()

    else:
        print("Invalid menu option. Please choose 1-4.")



