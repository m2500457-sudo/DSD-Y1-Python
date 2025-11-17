arcade = {
    "Pinball":"Working",
    "Claw Machine":"Working",
    "Car Simulator":"Not Working",
    "Pac-Man":"Not Working",
}

def viewing(arcade):

    print(arcade)

def adding(arcade):
    #this function allows users to input a new machine and say wether it is working or not.
    add = input("Would you like to add to the dictonary?")
    if add == "Yes" or add == "yes":
        what = input("Input what you would like to add to the dictionary.")
        working = input("Is the game working?")
        if working == "No" or working == "no":
            arcade[what] = "Not Working"
            print (arcade)
        elif working == "Yes" or working == "yes":
            arcade[what] = "Working"
            print (arcade)
        else:
            print("ERROR!")
    elif add == "No" or add == "no":
        print("Ok.")
        print(arcade)
        question()
    else:
        print("ERROR!")

def updating_status(arcade):
    #this function allows the user to select the key whos value is going to be changed, then allows the user to change it.
    which = input("What machine's status would you like to update?")
    working = input("Is the machine working? Yes/No")
    if working == "Yes" or working == "yes":
        #rather than having more if statements, aracde[which] allows the key the user enetered to be found in arcade, in order for it to be altered.
        arcade[which] = "Working"
        print(arcade)
    elif working == "No" or working == "no":
        arcade[which] = "Not Working"
        print(arcade)
    else:
        print("ERROR!")

def deleting(arcade):
    delete = input("What machine would you like to delete?")
    del arcade[delete]
    print(arcade)
    
def main_menu(aracde):
    #this function creates a menu for the user to choose from, the menu includeds the functions and the option to end the experiance.
    print("Hi, welcome to the main menu.")
    print("1) Viewing.")
    print("2) Add new machine.")
    print("3) Updating status.")
    print("4) Delete a machine")
    print("5) Exit.")
    choice = input("Please choose from the menu above")

    if choice == "1":
        viewing(arcade)
    elif choice == "2":
        adding(arcade)
    elif choice == "3":
        updating_status(arcade)
    elif choice =="4":
        deleting(arcade)
    elif choice == "5":
        print("Goodbye!")
    else:
        print("ERROR!")

def question():
    #this function will ask the user if they want to go to the main menu, at the menu the user can either user the functions or end the experiance.
    #the function will keep asking and can be stopped if the user inputs "no" or "No" when they are asked "Would you like to go to the main menu?".
    menu = input("Would you like to go to the main menu? Yes/No")
    if menu == "yes" or menu == "Yes":
        while menu == "Yes" or menu == "yes":
            main_menu(arcade)
            menu = input("Would you like to go to the main menu?")
            if menu == "no" or menu == "No":
                print("Ok! Goodbye!")
    elif menu == "no" or menu == "No":
        print("Ok! Goodbye!")
    else:
        print("ERROR!")
#these two functions are being called.
main_menu(arcade)
question()
