from datetime import datetime

name = input("Please input your name: ")

student_id = input("Please input your student ID: ")
device = input("What device are you loaning? ")
device_id = input("Please input the device ID: ")
date_out = input("Please enter the date you are taking the device (DD/MM/YYYY): ")
if date_out != 10:
    
    def get_entry_date(date_out):
        
        flag = True
        
        while flag:
            date_out = input("Please confirm the date you are taking the device (DD/MM/YYYY): ")

            try:
                datetime.strptime(date_out, "%d/%m/%Y").date()
            except:
                print("Sorry, you did not enter a valid date")
                flag = True
            else:
                return datetime.strptime(date_out, "%d/%m/%Y").date()
    get_entry_date(date_out)

date_in = input("Please enter the date you are returning the device.")
if date_in != 10:
    
    def get_entry_date(date_in):
        
        flag = True
        
        while flag:
            date_in = input("Please confirm the date you are returning the device (DD/MM/YYYY): ")

            try:
                datetime.strptime(date_in, "%d/%m/%Y").date()
            except:
                print("Sorry, you did not enter a valid date")
                flag = True
            else:
                return datetime.strptime(date_in, "%d/%m/%Y").date()
    get_entry_date(date_in)




info = {
    "name": name,
    "student_id": student_id,
    "device": device,
    "device_id": device_id,
    "date_out": date_out,
    "date_in" : date_in

}

print(info)
