import math
import random
from datetime import datetime
import numpy as np 

def maths():

    number = float(input("Please enter a number"))

    num_sqr_root = math.sqrt(number)
    print(number, "squared is" ,num_sqr_root)

    num_sqr = number * number
    print(number, "squared is" ,num_sqr)

    rounded_up = (math.ceil(number))
    print(number, "rounded up is" ,rounded_up)

    rounded_down = (math.floor(number))
    print(number, "rounded down is" ,rounded_down)

    area = math.pi * (number ** 2)
    print("The area of a circle calculated using the number" ,number, "as a radius is" ,area,)
#maths()

def dice_roll():

    lives = 3
    while lives > 0:

        data1 = (random.randint(1,6))
        data2 = (random.randint(1,6))
        total = data1 + data2
        if total == 7 or total == 11:
            print("You Win! Number is" ,total,)
        else:
            print("Try Again. Number is" ,total,)
            lives = lives - 1
#dice_roll()

def birthday():

    def calculate_age():
        print(datetime.now())
        year = input("Please input your birthdate in the format DD/MM/YYYY: ")
        birthdate = datetime.strptime(year, "%d/%m/%Y")

        today = datetime.today()
        age = today.year - birthdate.year
        if (today.month, today.day) < (birthdate.month, birthdate.day):
            age -= 1
        return age
    print("You are", calculate_age(), "years old.")
    calculate_age()
#birthday()

def sales_analysis():

    #This funcion shows how you can analyse arrays in different ways.
    x = np.array([120,135,150,98,175,200,143])

    mean = x.mean()
    print("The mean of the numbers in the array is" ,mean,)

    total = sum(x)
    print("The total of all of the numbers in the array is" ,total,)

    highest_value = x.max()
    print("The highest value in the array is" ,highest_value)

    lowest_value = x.min()
    print("The lowest value in the array is" ,lowest_value)
#sales_analysis()

def final():

    print(datetime.now())

    data1 = (random.uniform(1,100))
    print("The first random number is" ,data1,)
    data2 = (random.uniform(1,100))
    print("The second random number is" ,data2,)
    data3 = (random.uniform(1,100))
    print("The third random number is" ,data3,)
    x = np.array([data1, data2, data3])
    print (x)

    rounded1 = round(data1,0)
    rounded2 = round(data2)
    rounded3 = round(data3)

    new_x = np.array([rounded1, rounded2, rounded3])
    print("The list has been rounded, this is the rounded list",new_x,)
final()