# Q3 String Manipulator

sentence = input("Enter a sentence: ") #input sentence is taken and stored in variable called "sentence"

words = sentence.split()  #split() function used to split the words from the sentences .. stored in "word" variable

print("Original:", sentence)  #prints original sentence
print("Characters (with spaces):", len(sentence)) # It gives length of sentence i.e len() counts the characters in a sentence
print("Characters (without spaces):", len(sentence.replace(" ", ""))) #here replace(" "," ") removes the spaces the len() counts the characters 
print("Words:", len(words)) #words variable has list of words so len() counts total number of words in that list
print("UPPERCASE:", sentence.upper()) #upper() converts all letter to upper case(capital) letters
print("lowercase:", sentence.lower()) #lower() converts all letters to lower case(small) letters
print("Title Case:", sentence.title()) #title() capitaizes the first letter of every word 
print("First word:", words[0]) #since list index starts from 0 , it prints first word in the list
print("Last word:", words[-1]) #[-1] indicates last word or item in the list , so it prints last word of the word list
print("Reversed:", sentence[::-1]) #[start:end:step], so [::-1] -1 indicates move backward ..hence it reverses the sentence