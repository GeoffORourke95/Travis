#In task I was asked to let the user create a sentence.
#Then ask for a word in the sentence to replace.
#The replaced word then is replaced by a new work.
#Both words are printed
#Both sentences are printed

def replacer(sentence, word1, word2):
    replace = sentence.replace(word1, word2) #replacing word1 with word2
    return replace

print('''Welcome to task 4,
Please enter a sentence.
Then input a word you wish to replace,
then a word to replace the selected word with.

 ''')
print('Input sentence here: ')
sentence = input() #Reads the input sentence of user
words = sentence.split() #Use of the split command to seperate the sentence into words

print('Enter the word you wish to replace: ')
word1  = input()
if word1 in words: #Looks for word1 in the inputted sentence
    print('Enter the word you wish to be its replacement: ')
    word2 = input() #Input for word2
    print('Word1: "' + (word1) + '"')
    print('Word2: "' + (word2) + '"')
    print('Output')
    print(sentence)
    print(replacer(sentence, word1, word2)) #Calls replacer to change sentence
else:
    print('This word wasnt found in the sentence') #If word1 doesnt exist in sentence


        

