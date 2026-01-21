import pandas as pd

#CREATING DATA FILES---------------------------------------------------------------------------------------------------------------------------

def DataFrame():

    #This code makes a table of the data below.
    test = pd.DataFrame({"Yes": [50, 21], "No": [131, 2]})
    print(test)

def DataFrame_Opinions():

    #This makes a table out of the data again but it shows it can use words and not just numbers.
    test = pd.DataFrame({"Beyonce": ["I can sing" ,"I can dance"], "JLO": [ "Where is Ashanti","I cant"]})
    print(test)

def DataFrame_Labeling():

    
    test = pd.DataFrame({"Beyonce": ["I can sing","I can dance"],
                   "JLO": [ "Where is Ashanti","I cant"]},
                   #This is the part that will add labels to the side rather than just numbers
                   index=["Can you sing?", "Can you dance?"])
    print(test)

def Series():
    #A Series, by contrast, is a sequence of data values. If a DataFrame is a table, a Series is a list. And in fact you can create 
    # one with nothing more than a list:
    test = pd.Series([1,2,3,4,5])
    print(test)

def Series_Yearly():
    #A Series is, in essence, a single column of a DataFrame. So you can assign row labels to the Series 
    # the same way as before, using an index parameter. However, a Series does not have a column name, it only has one overall name
    test = pd.Series([30, 35, 40], index=["2015 Sales", "2016 Sales", "2017 Sales"], name ="product A")
    print(test)

#READING DATA FILES----------------------------------------------------------------------------------------------------------------------------


def Reading_Into_A_Data_Frame():

    #This function opens the file
    return pd.read_csv(
        r"C:\Users\M2500457\OneDrive - Middlesbrough College\Python\RBClassics (1).csv"
    )
df = Reading_Into_A_Data_Frame()
print(df)

Reading_Into_A_Data_Frame()

