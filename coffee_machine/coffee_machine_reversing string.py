word = input()
reversedString = ''
index = len(word) # calculate length of string and save in index
while index > 0:
    reversedString += word[index - 1] # save the value of str[index-1] in reverseString
    index = index - 1 # decrement index
if reversedString == word:
    print('Palindrome')
else:
    print('not palindrome')
