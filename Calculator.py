def calculate(exp):
    try:
        #used to check if user input is valid
        allowed = set("0123456789+-*/. ")
        if not set(exp).issubset(allowed): #checks it contains only allowed characters
            raise ValueError("Invalid characters in expression.")
        #eval is function that evaluates the expression
        return eval(exp)
    except Exception as e:
        raise ValueError(f"Invalid expression: {e}") #if user input is not valid, it show a error message
    

# loop to take user input and calculate the result multiple times
while True:
    exp = input("Enter an expression: ")
    try:
        result = calculate(exp)
        print(f"Result: {result}")
    except Exception as e: #if there is an error in the user input, it will show a error message
        print(f"Error: {e}")

    forExit = input("write 'exit' to exit or press enter to continue: ")
    if forExit.lower() == 'exit':
        break
    else:
        continue
