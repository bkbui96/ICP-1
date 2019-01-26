#Write a program that accepts a sentence and prints the number of letters, words and digits in Sentence.
sentence = input("Enter a sentence: ")
countL = 0
countD = 0
countW = sentence.count(' ') +1

for x in sentence:
    if x.isalpha():
        countL += 1

for x in sentence:
    if x.isdigit():
        countD += 1


print("Letters = %d" % (countL))
print("Digits = %d" % (countD))
print("Words = %d" % (countW))