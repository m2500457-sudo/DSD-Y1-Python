import pandas as pd 
import matplotlib.pyplot as plt

winter = pd.read_csv(r"C:\Users\M2500457\OneDrive - Middlesbrough College\Documents\GitHub\DSD-Y1-Python\WinterSD.csv")
summer = pd.read_csv(r"C:\Users\M2500457\OneDrive - Middlesbrough College\Documents\GitHub\DSD-Y1-Python\SummerSD.csv")
countries = pd.read_csv(r"C:\Users\M2500457\OneDrive - Middlesbrough College\Documents\GitHub\DSD-Y1-Python\CountriesSD.csv")

def summer_gender():
    #This code creates a pie chart, however it should be noted this pie chart needs more code because it deals with string instead of numbers.
    Gender = summer["Gender"].value_counts()
    plt.pie(
        Gender,
        labels=Gender.index,
        autopct="%1.1f%%",
        startangle=90)
    plt.title("Percentage of male participants vs female participants")
    plt.show()
#summer_gender()

def overall_gender():
    #The first twwo lines of this function merge the two gender columns of both dataframes 
    merged_df = pd.merge(winter,summer, on="Gender", how="inner")
    gender_counts = merged_df.groupby("Gender").size()
    plt.pie(
        gender_counts,
        labels=gender_counts.index,
        autopct="%1.1f%%",
        startangle=90)
    plt.title("Overall gender diustribution")
    plt.show()
#overall_gender()

