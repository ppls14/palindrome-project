name = "Palindrome program" #program name
def palindrome(word):
    """
    Takes one argument (string type) and returns a boolean value: True/False, 
    indicating whether the text is a palindrome. A palindrome is a word, number,
    phrase, or other sequence of symbols that reads the same backwards as forwards.
    Arguments: 
    word
    """
    reversed_word = word[::-1]      #reverse of string
    if reversed_word != word:       
        return False
    return True

word = ''                       #input any word to check is it a palindrome
answer = palindrome(word)   #variable assigned to the function

print(name) #display program name

if (answer):
    print(f"Yes, the word {word} is a palindrome!")
else:
    print(f"No, the word {word} is not a palindrome!")