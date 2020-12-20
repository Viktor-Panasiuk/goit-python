last_data_input = None
result = 0
while True:
    if last_data_input != "number":
        input_number = input("Enter number: ")
    else:
        input_operator = input("Enter operator: ")
        if input_operator == "+" or input_operator == "-" or input_operator == "*" or input_operator == "/":
            operator = input_operator
            last_data_input = "operator"
            continue
        elif input_operator == "=":
            print(f"Result = {result}")
            break
        else:
            print(f"Error, '{input_operator}' is not operator")
            continue
        
    try:
        input_number = float(input_number)
        if last_data_input == None:
            result = input_number
            last_data_input = "number"
            continue
        else:
            # Обчислення виразу
            if operator == "+":
                result += input_number
            elif operator == "-":
                result -= input_number
            elif operator == "*":
                result *= input_number
            else:# Операція ділення
                try:
                    result /= input_number
                except:
                    print("Division by zero. Enter another number") 
                    continue    
            last_data_input = "number"

    except ValueError: # не число
        print(f"Error, '{input_number}' is not number")
        continue
            
    