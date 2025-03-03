#1.#####################################################################################
sentence = ["the", "quick", "brown", "fox", "jumped", "over", "the", "lazy", "dog"]
for word in sentence:
    print(word)
#2-Multiples of 5 #########################################################################
for number in range(5,31,5):
    print(number)
##3- Password Generator####################################################################
import random
letters=["adgdklfdjfksjdaqdsfsfslkff"]
symbol=["@!#$%^&*()_+"]
numbers=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
num_letters=4
num_symbols=2
num_numbers=3
letters=random.sample(letters)
symbols=random.sample(symbol)
numbers=random.sample(numbers)
password=numbers+letters+symbols
print(password)
# I have a problem
#########################################################################################
#4-Factorial Numbeber
# i have a problem
