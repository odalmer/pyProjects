def Calculate(choice):
    operations = ["+", "-", "x", "/"]
    for operation in operations:
        print(operation)
        if operation in choice:
            nums = choice.split(operation);
            print(operation)
            print(nums)
        
    r = 0;
    n1 = int(nums[0])
    n2 = int(nums[1])
    
    # Arithmetics operations 
    def Add():
        r = n1 + n2;
        return r

    def Subs():
        r = n1 - n2;
        return r    

    def Mult():
        r = n1 * n2;
        return r
        
    def Div():
        r = n1 / n2;
        return r

    # Conditionals
    if "+" in choice:
        return Add()   

    elif "-" in choice:
        return Subs() 

    elif "x" in choice:
        return Mult() 

    elif "/" in choice:
        return Div()

    else:
        print("Operation invalid \ntry typing 2+2") 

choice = input("Enter an operation between 2 numbers: ")
print(Calculate(choice))


