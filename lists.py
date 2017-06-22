#this is for the name generator
names = ['Anne', 'Jessie', 'Starla', 'Michelle', 'Meghna', 'Shannon', 'Erin', 'Alison', 'Akhila']
print(' ')
for i in range(9):
    print(names[i])

print(' ')
from random import *

#this 2nd portion of the code is for the desserts
main = ['chicken pot pie', 'lasagna', 'alfredo pasta']
desserts = ['tiramisu', 'fried banana and ice cream', 'mango sorbet']
sides = ['artichoke dip', 'mozzarella sticks', 'calamari']

v1 = randint(0,2)
v2 = randint(0,2)
v3 = randint(0,2)

print('Your main dish is:', main[v1])
print('Your side dish is:', sides[v2])
print('Your dessert is:', desserts[v3])
print(' ')

#this bottom portion of the code is for the haiku
line1 = ['Jessie', 'Michelle', 'Starla', 'chipotle', 'chocolate', 'Symantec']
line2 = [ 'fatigue', 'hungry', 'growling', 'became', 'flower', 'pooping', 'basketball', 'appendix', 'integral']
line3 = ['laughter', 'hangry', 'messy', 'annoying', 'fashionable', 'courageous']


print(line1[randint(0,2)], line1[randint(3,5)])
print(line2[randint(0,2)], line2[randint(3,5)], line2[randint(6,8)])
print(line3[randint(0,2)], line3[randint(3,5)])
print(' ')
