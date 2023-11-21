# 4. Develop a program that takes a sentence from the user and counts the number of vowels in it using a loop and conditional statement.

vowel_count = 0
sentence = input('Enter a Sentence: ')
sentence = sentence.lower()
for letter in sentence:
    if letter in ['a', 'e', 'i', 'o', 'u']: 
        vowel_count += 1
print(vowel_count)
