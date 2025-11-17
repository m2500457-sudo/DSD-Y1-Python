def temprature():
    temprature = float(input("Please input your temprature in the format 00.00"))
    if temprature >= 37.5:
        print("High Temprature")
    elif temprature <= 20:
        print("Low temprature")
    else:
        print("Your tempratue is" ,temprature, "that is safe.")

def oxygen():
    oxygen = int(input("Please input your oxygen levels"))
    if oxygen <= 92:
        print("Low Oxygen")
    elif oxygen >=120:
        print("Oxygen is too high.")
    else:
        print("Your oxygen is" ,oxygen, "that is safe.")

def heart_rate():
    heart_rate = int(input("Please input your heart rate."))
    if heart_rate >= 60 and heart_rate <= 100:
        print ("Heart rate out off bounds!")
    else:
        print("Heartrate is safe.")

def main_menu():
    while True:
        print("\n--- Hospital Utility Menu ---")
        print("1. Temprature Check")
        print("2. Oxygen Levels")
        print("3. Heart Rate Check")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            temprature()
        elif choice == '2':
            oxygen()
        elif choice == '3':
            heart_rate()
        elif choice == '4':
            print("Exiting program. Take care!")
            break
        else:
            print("Invalid choice. Please select a number from 1 to 5.")

#main_menu()

#NEW PROGRAM (STEP GAME COUNTER)------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

score = 0

def step_score(score):
    today_step = int(input("Please input your step count on today."))
    yesterday_step = int(input("Please input your step count on yestday."))

    

    if today_step > yesterday_step:
        print("Great! Your step count improved.")
        score = score + 1
        print("Your score went up by 1, your score is now" ,score,)
    else:
        print("No change or lower reading.")
        score = score
    return score

def play_again(score):
    while True:
        
        choice = input("Would you like to play again?")

        if choice == 'Yes' or choice == "yes":
            score = step_score(score)
        elif choice == "No" or choice == "no": 
            print("Exiting program. Take care!")
            break
        else:
            print("Invalid choice.Please answer yes or no.")
        return score

score = step_score(score)
play_again(score)

# The symbol == checks if two things are equal to eachother. Whilst = is used to assign variables.
# You would use the symbols >= if you wanted to check if one thing was higher than or the save value as another number.
# Arithmatic and relational operators work together because the arithmetic operator determines the value, then the
# relational operator compares the values.