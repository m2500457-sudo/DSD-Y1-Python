name = input("Please enter your name")
score = input("Please enter your score?")
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



    
    