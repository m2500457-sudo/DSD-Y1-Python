def inputs():

    name = input("Please enter your name")
    score = input("Please enter your score?")
    while True:
        if score.isdigit():
            return name, score
        else:
            score = input("Please enter your score?")
def file(name,score):

    with open("python.txt","a") as file:
        file.write(f" {name}: {score}\n")

    file_path = "python.txt"

    try:
        with open(file_path, "r") as file:
            file_content = file.read()
            print(file_content, end="")
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def search():
    search_string = input("What name would you like to search?")
    file_path = "python.txt"

    with open(file_path, "r") as file:
        content = file.read()
        if search_string in content:
            print("The name" ,search_string, "was found in the file")
        else:
            print("The name" ,search_string, "was not found in the file.")

def average():
    with open(file_path)







tmep = inputs()
#inputs = ("alex", 24)   
file(tmep[0], tmep[1])
search()