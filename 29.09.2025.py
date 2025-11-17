
def dr_info():
    name = input("Please input your name.")
    dob = input("Please enter your Date Of Birth.")
    age = input("Please input your age")
    weight = input("Please input your weight")
    height = input("Please enter your height")

    MAX_AGE = int(100)
    MIN_AGE = int(18)

    print ("Your name is," ,name , ".")
    print ("Your Date Of Birth is," ,dob, "." )
    print ("You are," ,age, "years old.")
    print ("You weigh," ,weight, "pounds.")
    print ("You are" ,height, "tall.")


#BMI CALCULATOR ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    
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

#DOSAGE CALCULATOR -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

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
    




#HOSPITAL BILLING SYSTEM ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def calculate_hospital_bill():
    bill = float(0)
    days = float(input("How many days did you stay?"))
    ROOM = float(100.)
    roomcost = float((ROOM * days))
    bill = bill + roomcost
    physio_cost =float(100)
    physio = input("Did the pateint do physio-therapy?")
    if physio == "yes":
        times = float(input("How many times?"))
        physio_total = (times * physio_cost)
        bill = bill + physio_total 
    else:
        bill = bill
    doctor = float(100)
    dr = input("Did the patient have a consultation with the Doctor?")
    if dr == "yes":
        dr_times = float(input("How many consultations?"))
        dr_cost = (dr_times * doctor)
        bill = bill + dr_cost
    else:
        bill = bill
    
    VAT = float(1.20)
    total_bill = (bill * VAT)
    rounded_total = round(total_bill, 2)
    print("Your total is" ,rounded_total, )

def main_menu():
    while True:
        print("\n--- Hospital Utility Menu ---")
        print("1. Patient Info")
        print("2. BMI Calculator")
        print("3. Dosage Calculator")
        print("4. Hospital Billing System")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            dr_info()
        elif choice == '2':
            bmi_calculator()
        elif choice == '3':
            dosage_calculator()
        elif choice == '4':
            calculate_hospital_bill()
        elif choice == '5':
            print("Exiting program. Take care!")
            break
        else:
            print("Invalid choice. Please select a number from 1 to 5.")


main_menu()