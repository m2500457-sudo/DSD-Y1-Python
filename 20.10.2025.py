#Task 1:

def Medication_Safety_Rule():
    
    age = int(input("Please enter your age."))
    weight = int(input("Please input weight in kg."))
    if age > 12 and weight > 40:
        print("Safe to give medication.")
    else:
        print("Unsafe to give medication.")

def Fitness_Centre_Access():

    age = int(input("Please input your age."))
    medical = input("Do you have medical clearance?")
    if age > 18 or medical == "Yes" or medical =="yes":
        print("Access granted")
    else:
        print("Access denied")

def Sleep_Tracker_Alert():

    asleep = input("Is the person asleep?")
    heart_rate = int(input("Input the person's heartrate."))
    if asleep == "No" or asleep == "no" and heart_rate > 100:
        print("Alert sent:")
    else:
        print("No alert sent.")

def menu():

    print("1) Medication Safetey Rule.")
    print("2) Fitness Centre Acess Check.")
    print("3) Slepp Tracker Alert")
    print("4) Exit.")
    choice = input("Welcome to the menu, pleae choose from the following options (1-4)")

    if choice == "1":
        Medication_Safety_Rule()
    elif choice =="2":
        Fitness_Centre_Access()
    elif choice =="3":
        Sleep_Tracker_Alert()
    elif choice =="4":
        print("Ok, goodbye!")

menu()