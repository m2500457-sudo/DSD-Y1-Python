def area():
    height = float(input("Enter the height of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    area = height * width

    print (area)

def time():
    type = input("Is the time in hours or minutes?")

    if type == "minutes":
        minutes = float(input("Please input how many minutes."))
        calculation = minutes // 60
        print ("there are" , calculation, "hours in", minutes ,"minutes")
    elif type == "hours":
        hours = float(input("Please input how many hours."))
        calculation = hours * 60
        print (hours, "is equal to" ,calculation, "minutes")
    else:
        print("Error.")

def bill():
    name = input("Please eneter your name.")
    age = int(input("please enter your age."))

    bill_amount = input("How much is your bill?")
    bill_amount = float(bill_amount)
    total = float(bill_amount * 1.2)

    if age < 18:
        total = total * 0.20
    else:
        total = total

    print ("Your name is", name, "you are", age, "years old and your bill is", total,)

    if total > 1000:
        payment = total / 12
        print ("You cna pay", payment, "once a month for 12 months.")
    else:
        ()

def password():
    while True:
        user_password = input("Please enter the password: ")
        if user_password == "Password1":
            print("Login successful! Welcome.")
            break
        else:
            print("Incorrect password. Please try again.")

def dosage_calculator():
        current = int(0)
        dosage = int(5)
        OVERDOSE = int(100)


        medicine = int(input("How many doses has the patient had?"))
        ml = (medicine * dosage)
        safe = (OVERDOSE - ml)
        leftover = (safe / 5)



        if medicine <100:
            print ("The patient can have " ,leftover, "more dose of medicine.")
        elif medicine == 100:
            print ("The patient can't have anymore.")
        elif medicine >100:
            print ("The patient has had too much.")

        else:
            print("error")
    
def bmi_calculator():
    age = input("Please input your age")
    HEIGHT = float(input("Please enter your height (in metres)"))
    weight = float(input("Please input your weight (in kg)"))

    new_height = (HEIGHT * HEIGHT)
    BMI = (weight / new_height)
    rounded_bmi = round(BMI, 1)
    print (rounded_bmi)

        
    if rounded_bmi  < 18.5:
        print("Your BMI is too low for your age range.")
    elif rounded_bmi > 24.9: 
        print("Your BMI is too high for your age range.")
    else:
        print("Your Bmi is healthy")

def add_patient_info():
    
    MAX_AGE = int(100)
    MIN_AGE = int(18)

    age = int(input("Please input your age"))
    name = input("Please input your name.")
    dob = input("Please enter your Date Of Birth.")
    weight = input("Please input your weight")
    height = input("Please enter your height")

    print ("Your name is," ,name , ".")
    print ("Your Date Of Birth is," ,dob, "." )
    print ("You are," ,age, "years old.")
    print ("You weigh," ,weight, "pounds.")
    print ("You are" ,height, "tall.")

def main_menu():
    while True:
        print("\n--- Hospital Menu ---")
        print("1. Patient Info")
        print("2. BMI Calculator")
        print("3. Dosage Checker")
        print("4. Exit Program")
        choice = input("Enter your choice (1-4): ")
        if choice == "1":
            add_patient_info()
        elif choice =="2":
            bmi_calculator()
        elif choice == "3":
            dosage_calculator()
        elif choice == "4":
            print("Closing program, goodbye!")
            break
        else:()

main_menu()


