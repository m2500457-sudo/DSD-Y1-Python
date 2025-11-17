def lab_results__convertor():
    test_type = input("Is it a glucose or cholesterol test?")
    value = float(input("What is the value?"))
    units = input("What are the units?")

    num = 18

    # = value * 18
    #mmol_l = value / 18

    if units == "mmol/L":
        converted = value / num

        print("The original number was" ,value, "in the units mmo/L, the new number is " ,converted, "in the units mg/dL")
    elif units == "mg/dL":
        converted = value * num

        print("The original number was" ,value, "in the units mg/dL, the new number is " ,converted, "in the units mmo/L")
    else:
        print("Unknown")

def average_temprature_tracker():
    num1 = float(input("Please input the first temprature."))
    while num1 <30 or num1>45:
        num1 = float(input("Please input the first temprature."))
 
    num2 = float(input("Please input the second temprature."))
    while num2 <30 or num2>45:
        num2 = float(input("Please input the second temprature."))

    num3 = float(input("Please input your third temprature"))
    while num3 <30 or num3>45:
        num3 = float(input("Please input the third temprature."))

    av = num1 + num2 + num3
    average = av / 3
    rounded = round(average ,2)
    print (rounded)

    if rounded <30:
        print("Your average temprature is" ,rounded, "that is too low.")
    elif rounded >45:
        print("Your average temprature is" ,rounded, "that is too high")
    elif rounded >30 and rounded <45:
        print("Your temprature is" ,rounded, "that is a healthy temprature")
    else:
        print("Error")

age = int(input("Please enter your age."))
heart = int(input("Please enter your resting heart rate."))

safe = int()
maximum = int()

if age  >19 and age <30:
   maximum = 171
   minimum = 100
   if heart >100 and heart <170:
    print("You are in your twenties and your heart rate is healthy.")
   elif heart <= 100:
    print("Your in your twenties and your heartrate is too low!")
   elif heart >= 170:
       print("Your in your twenties and your heartrate is too high!")

if age  >29 and age <40:
   maximum = 162
   minimum = 95
   if heart >95 and heart <162:
    print("You are in your thirties and your heart rate is healthy.")
   elif heart <= 95:
    print("Your in your thirties and your heartrate is too low!")
   elif heart >= 162:
       print("Your in your thirties and your heartrate is too high!")






       
   
    




    



