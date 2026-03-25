

while True:
    try:
        parcel_code = int(input("Input parcel code"))

        if lenght == 11:
            break
        else:
            print("Please enter 11 digits.")
    except ValueError:
        print("Please enter your name using digits.")
return parcel_code