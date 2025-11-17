energy_levels = {
    "09:00am":"60 Joules",
    "12:00pm":"90 Joules",
    "15:00pm":"120 Joules",
    "18:00pm":"150 Joules",
    "21:00pm":"180 Joules",
}

user_names = {
    "Username1":"Alfie",
    "Username2":"Beyonce",
    "Username3":"Rihanna",
    "Username4":"Nicki",
    "Username5":"Adele",
}

step_count = {
    "User1":"1000",
    "User2":"2000",
    "User3":"3000",
    "User4":"4000",
    "User5":"5000",
}

print(energy_levels)
print(energy_levels["09:00am"])
print(energy_levels["12:00pm"])
print(energy_levels["18:00pm"])
time = input("Please enter a time in the format 00:00.")
amount = input("Please enter an energy level.")
energy_levels[time] = amount
print(energy_levels)

print(user_names["Username1"])
print(user_names["Username3"])
print(user_names["Username5"])
username = input("Please enter a user in the format usernamex.")
name = input("Please enter a name.")
user_names[username] = name
print(user_names)

print(step_count)
print(step_count["User1"])
print(step_count["User3"])
print(step_count["User5"])
user = input("Please input a user.")
steps = input("Please enter the amount of steps for user.")
step_count[user] = steps
print(step_count)