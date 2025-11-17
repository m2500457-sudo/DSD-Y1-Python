def calculate_steps():
    goal = int(1000)
    steps = int(input("Please input your steps."))
    
    if steps < goal:
        percent = goal / steps
        total = percent * 10
        percent_round = round(total)
        print ("Your step count is" ,steps, "your percentage of your goal is" ,percent_round,)
    
    
    elif steps > goal:
        total = steps / 1000
        totalt = total * 100
        rounded = round(totalt)
        print ("You outdid your goal of 1000! You did" ,steps, "steps! Your percentage is" ,rounded, "%")

def BMI():
    height = float(input("Please input your height in metres"))
    weight = float(input("Please input your weight in kg"))
    bmi = weight / (height ** 2)
    if bmi < 18.5:
        print ("Your BMI indicates you are underweight.")
    elif bmi > 30:
        print("Your bmi indicates you are overweight.")
    elif bmi < 30 and bmi > 18.5:
        print("Your BMI is healthy.")
    else:
        print("Error")

def screen_time_flag():
    daily_minutes = int(input("please input the daily minutes."))
    steps = int(input("Please input your steps."))
    night_screen_time = int(input("please input the night screen time minutes."))
    flag_user(daily_minutes,steps,night_screen_time)
    return flag_user()

def flag_user(daily_minutes,steps,night_screen_time):
    if daily_minutes > 240 and steps < 5000 or night_screen_time > 60:
        return True
    else:
        return False

#print(screen_time_flag())

score = 0

def Hydration_streak(score):
    water = int(input("Please input the amount of water in ml"))
    if water < 1999:
        points = water // 250
        score = score + points
        print (score)
    elif water >= 2000:
        points = water // 250
        score = score + points + 5
        print (score)

#score = Hydration_streak(score)

def free_class():
    age = int(input("Please input your age."))
    #low = input("Are you a registered low-income participant?")
    last_month = input("Have you received a free class in the past 30 days?")
    
def eligible_for_free_class(age,last_month):
    if age =< 25 and age >=16 or last
    


