def largestWord(s):
    
    # Sort the words in increasing
    # order of their lengths
    s = sorted(s, key = len)
 
    # Print last word
    print(s[-1])
    return

userInput = ""
while userInput != "quit":
    # Given string
    userInput = input("Enter a sentence: ")

    # Closing the app if the input is quit
    if userInput == "quit":
        quit()
    
    # Split the string into words
    l = list(userInput.split(" "))

       
    largestWord(l)

