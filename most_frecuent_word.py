from collections import Counter

def most_common_word(sentence):
    # split the sentence into words
    words = sentence.split()
    # create a dictionary to store the frequency of each word
    word_freq = Counter(words)
    # find the word with the highest frequency
    most_common = word_freq.most_common(1)
    return most_common[0][0]

print("This python script prints the most repeated word in a sentence")
userInput = input("Enter a sentence:")
print("The most common word in the sentence is:", most_common_word(userInput))
