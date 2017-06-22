from random import *

def isPrime(num):
    if num > 1:
        for factor in range(2, num):
            if num % factor == 0:
                return False
        return True

num_list = []

for number in range(0,100):
    num_list.append(randint(10,99))

print(num_list)

sum = 0
for number in num_list:
    if isPrime(number):
        sum += number

print(sum)
