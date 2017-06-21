start = '''
Welcome to the 2020 Tokyo Olympics!! It's been a great start to the games.
Thank you for coming to support the swimmers competing today!
'''

bec = '''
Because you chose
'''

win = " you win!!! :-) "

lose = ''' you lost. :-((( '''

print(start)

# co = input('Enter which country you would like to represent.')

#swi = input('Please choose a swimmer: ' )

#st = input('Now choose which stroke you wish to compete with: ')

pp  = '''
else: print('Please type in either Michael Phelps, Missy Franklin, Joshua Tibatemwa, Jamila Lunkuse, Pieter van den Hoogenband, Jolanda de Rover, Sun Yang, or Fu Yuanhui.')
'''

coun = '''Please type in either USA, Uganda, Netherlands, or China. '''

co = input('Enter which country you would like to represent.')

swi = input('Please choose a swimmer: ' )

st = input('Now choose which stroke you wish to compete with: ')

done = False
while not done:
    if co == 'USA':
        if swi == 'Michael Phelps':
            if st == 'freestyle':
                print(bec, st, win)
                done = True
            elif st == 'backstroke':
                print(bec, st, lose)
                done = True
            elif st == 'breastroke':
                print(bec, st, lose)
                done = True
            elif st == 'butterfly':
                print(bec, st, win)
                done = True
            else:
                st = input("Please type in either freestyle, backstroke, breastroke, or butterfly: ")
        elif swi == 'Missy Franklin':
            if st == 'freestyle':
                print(bec, st, lose)
                done = True
            elif st == 'backstroke':
                print(bec, st, win)
                done = True
            elif st == 'breastroke':
                print(bec, st, lose)
                done = True
            elif st == 'butterfly':
                print(bec, st, lose)
                done = True
            else:
                print('Please type in either freestyle, backstroke, breastroke, or butterfly.')
            done = True
    elif co == 'Uganda':
        swi = input('Please choose a swimmer: ' )
        if swi == 'Joshua Timbatemwa':
            if st == 'freestyle':
                print(bec, st, win)
                done = True
            elif st == 'backstroke':
                print(bec, st, lose)
                done = True
            elif st == 'breastroke':
                print(bec, st, lose)
                done = True
            elif st == 'butterfly':
                print(bec, st, lose)
                done = True
            else:
                print('Please type in either freestyle, backstroke, breastroke, or butterfly.')
            done = True
        elif swi == 'Jamila Lunkuse':
            if st == 'freestyle':
                print(bec, st, lose)
                done = True
            elif st == 'backstroke':
                print(bec, st, lose)
                done = True
            elif st == 'breastroke':
                print(bec, st, win)
                done = True
            elif st == 'butterfly':
                print(bec, st, lose)
                done = True
            #done = True
            else:
                print('Please type in either freestyle, backstroke, breastroke, or butterfly.')
            done = True
    elif co == 'Netherlands':
        swi = input('Please choose a swimmer: ')
        if swi == 'Pieter van den Hoogenband':
            if st == 'freestyle':
                print(bec, st, win)
                done = True
            elif st == 'backstroke':
                print(bec, st, lose)
                done = True
            elif st == 'breastroke':
                print(bec, st, lose)
                done = True
            elif st == 'butterfly':
                print(bec, st, lose)
                done = True
            #done = True
            else:
                print('Please type in either freestyle, backstroke, breastroke, or butterfly.')
            done = True
        elif swi == 'Jolanda de Rover':
            if st == 'freestyle':
                print(bec, st, lose)
                done = True
            elif st == 'backstroke':
                print(bec, st, win)
                done = True
            elif st == 'breastroke':
                print(bec, st, lose)
                done = True
            elif st == 'butterfly':
                print(bec, st, lose)
                done = True
            #done = True
            else:
                print('Please type in either freestyle, backstroke, breastroke, or butterfly.')
            done = True
    elif co == 'China':
        swi = input('Please choose a swimmer: ' )
        if swi == 'Sun Yang':
            #done = True
            if st == 'freestyle':
                print(bec, st, win)
                done = True
            elif st == 'backstroke':
                print(bec, st, lose)
                done = True
            elif st == 'breastroke':
                print(bec, st, lose)
                done = True
            elif st == 'butterfly':
                print(bec, st, lose)
                done = True
            else:
                print('Please type in either freestyle, backstroke, breastroke, or butterfly.')
            done = True
        elif swi == 'Fu Yuanhui':
            if st == 'freestyle':
                print(bec, st, lose)
                done = True
            elif st == 'backstroke':
                print(bec, st, win)
                done = True
            elif st == 'breastroke':
                print(bec, st, lose)
                done = True
            elif st == 'butterfly':
                print(bec, st, lose)
                done = True
            else:
                print('Please type in either freestyle, backstroke, breastroke, or butterfly.')
            done = True
        else:
            swi = input('Please choose a swimmer: ' )
    else:
        co = input('Enter which country you would like to represent.')
