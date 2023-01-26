def calculate(choice):
    operations = {"+": lambda x, y: x + y, "-": lambda x, y: x - y, "x": lambda x, y: x * y, "/": lambda x, y: x / y}

    for operation in operations:
        if operation in choice:
            nums = choice.split(operation)
            return operations[operation](int(nums[0]), int(nums[1]))
    return "Invalid operation. Try typing 2+2."

choice = input("Enter an operation between 2 numbers: ")
print(calculate(choice))
