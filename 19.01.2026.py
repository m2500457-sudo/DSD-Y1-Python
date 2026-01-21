import pandas as pd 

def adding_to_dataset():

    data = {
        "Name":["Alex","Jamie","Sam"],
        "Attendance":[92, 85, 78],
        "Grade":["B","C","D"],
        "Passed":["Yes","Yes","No"]
    }

    df = pd.DataFrame(data)
    print(df)

    name= input("Enter new name.")
    attendance = input("Enter attendance.")
    grade = input("Enter grade.")
    passed = input("Did they pass?")

    new_row = pd.DataFrame({
        "Name": [name],
        "Attendance": [attendance],
        "Grade": [grade],
        "Passed": [passed]
    })

    df = pd.concat([df, new_row], ignore_index=True)
    print(df)

def loading_and_inspecting_data():

    df = pd.read_csv(r"C:\Users\M2500457\Downloads\students.csv")
    print(df.head())
    print(df.info())

def basic_data_analysis():

    df = pd.read_csv(r"C:\Users\M2500457\Downloads\students.csv")
    mean = df["Attendance"].mean()
    highest = df["Attendance"].max()
    lowest = df["Attendance"].min()
    below = df[df["Attendance"] < 80]
    above = df[df["Attendance"] >= 90]
    A = df[df["Grade"] == "A"]
    B = df[df["Grade"] == "B"]
    C = df[df["Grade"] == "C"]
    D = df[df["Grade"] == "D"]
    E = df[df["Grade"] == "E"]
    print(E)

def filtering_and_conditions():

    #This line of code selects only two of the categories from the csv file.
    df = pd.read_csv(r"C:\Users\M2500457\Downloads\students.csv", usecols=["Name", "Attendance"])
    #This line of code filters out all students with an attendance thats 80% or higher.
    df = df[df["Attendance"] < 80]
    print(df)
filtering_and_conditions()