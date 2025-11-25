from datetime import datetime

information = {

    "Student_first_name": "",
    "Student_second_name": "",
    "Student_id" : "",
    "Device_id" : "",
    "Device_type" : "",
    "Entry_date" : "",
    "Return_date" : "",

}

def get_first_name():
    while True:
        first_name = input("Please input your first name: ")
        if first_name.isalpha():
            information ["Student_first_name"] = first_name
            return first_name
        else:
            print("Please only use letters.")
get_first_name()

def get_second_name():
    while True:
        last_name = input("Please input your Last name: ")
        if last_name.isalpha():
            information ["Student_second_name"] = last_name
            return last_name
        else:
            print("Please only use letters.")
get_second_name()

def get_student_id(information):
    while True:
        student_id = input("Please input your numerical student ID.")
        if student_id.isdigit():
            information ["Student_id"] = student_id
            return student_id
        else:
            print("Please only use numbers.")
get_student_id(information)

def device_type():
    while True:
        device = input("What device are you loaning? ")
        if device.isalpha():
            information["Device_type"] = device
            return device
        else:
            print("Please only use letters.")
device_type()

def get_device_id(information):
    while True:
        device_id = input("Please input the device ID: ")
        if device_id.isdigit():
            information ["Device_id"] = device_id
            return device_id
        else:
            print("Please only use numbers.")
get_device_id(information)

def get_entry_date(information):
    flag = True
    while flag:
        date_out = input("Please confirm the date you are taking the device (DD/MM/YYYY): ")
        try:
            datetime.strptime(date_out, "%d/%m/%Y").date()
        except:
            print("Sorry, you did not enter a valid date")
            flag = True
        else:
            information["Entry_date"] = date_out
            return datetime.strptime(date_out, "%d/%m/%Y").date()
get_entry_date(information)

def get_return_date(information):
    flag = True
    while flag :
        date_in = input("Please enter the date you are returning the device.")
        try:
            datetime.strptime(date_in, "%d/%m/%Y").date()
        except:
            print("Sorry, you did not enter a valid date")
            flag = True
        else:
            information["Return_date"] = date_in
            return datetime.strptime(date_in, "%d/%m/%Y").date()
get_return_date(information)

print(information)
