def hello_world():
    
    user_input = input("Enter a sentence: ")
    titled_input = user_input.title()
    print("Titled string:", titled_input)


def get_letter():
    while True:
        input_str = input("Please enter a letter: ")
        if input_str.isalpha() and len(input_str) == 1:
            return input_str
        else:
            print("That's not a valid letter. Please try again.")