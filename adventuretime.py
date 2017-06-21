start = '''
Welcome to the 2020 Tokyo Olympics!! It's been a great start to the games.
Thank you for coming to support the swimmers competing today!
'''

bec = '''
Because you chose
'''

win = ''' you win!!! :-) '''

lose = ''' you lost. :-((( '''

print(start)

# co = input('Enter which country you would like to represent.')

#swi = input('Please choose a swimmer: ' )

#st = input('Now choose which stroke you wish to compete with: ')

pp  = '''
else: print('Please type in either Michael Phelps, Missy Franklin, Joshua Tibatemwa, Jamila Lunkuse, Pieter van den Hoogenband, Jolanda de Rover, Sun Yang, or Fu Yuanhui.')
'''

coun = '''Please type in either USA, Uganda, Netherlands, or China. '''


done = False
while not done:
    co = input('Enter which country you would like to represent.')
    if co == 'USA':
        swi = input('Please choose a swimmer: ' )
        if swi == 'Michael Phelps':
            st = input('Now choose which stroke you wish to compete with: ')
            if st == 'freestyle':
                print(bec, st, win)
            elif st == 'backstroke':
                print(bec, st, lose)
            elif st == 'breastroke':
                print(bec, st, lose)
            elif st == 'butterfly':
                print(bec, st, win)
            else:
                print('Please type in either freestyle, backstroke, breastroke, or butterfly.')
            done = True
        elif swi == 'Missy Franklin':
            st = input('Now choose which stroke you wish to compete with: ')
            if st == 'freestyle':
                print(bec, st, lose)
            elif st == 'backstroke':
                print(bec, st, win)
            elif st == 'breastroke':
                print(bec, st, lose)
            elif st == 'butterfly':
                print(bec, st, lose)
            else:
                print('Please type in either freestyle, backstroke, breastroke, or butterfly.')
            done = True
    elif co == 'Uganda':
        swi = input('Please choose a swimmer: ' )
        if swi == 'Joshua Timbatemwa':
            if st == 'freestyle':
                print(bec, st, win)
            elif st == 'backstroke':
                print(bec, st, lose)
            elif st == 'breastroke':
                print(bec, st, lose)
            elif st == 'butterfly':
                print(bec, st, lose)
            else:
                print('Please type in either freestyle, backstroke, breastroke, or butterfly.')
            done = True
        elif swi == 'Jamila Lunkuse':
            st = input('Now choose which stroke you wish to compete with: ')
            if st == 'freestyle':
                print(bec, st, lose)
            elif st == 'backstroke':
                print(bec, st, lose)
            elif st == 'breastroke':
                print(bec, st, win)
            elif st == 'butterfly':
                print(bec, st, lose)
            #done = True
            else:
                print('Please type in either freestyle, backstroke, breastroke, or butterfly.')
            done = True
    elif co == 'Netherlands':
        swi = input('Please choose a swimmer: ')
        if swi == 'Pieter van den Hoogenband':
            st = input('Now choose which stroke you wish to compete with: ')
            if st == 'freestyle':
                print(bec, st, win)
            elif st == 'backstroke':
                print(bec, st, lose)
            elif st == 'breastroke':
                print(bec, st, lose)
            elif st == 'butterfly':
                print(bec, st, lose)
            #done = True
            else:
                print('Please type in either freestyle, backstroke, breastroke, or butterfly.')
            done = True
        elif swi == 'Jolanda de Rover':
            st = input('Now choose which stroke you wish to compete with: ')
            if st == 'freestyle':
                print(bec, st, lose)
            elif st == 'backstroke':
                print(bec, st, win)
            elif st == 'breastroke':
                print(bec, st, lose)
            elif st == 'butterfly':
                print(bec, st, lose)
            #done = True
            else:
                print('Please type in either freestyle, backstroke, breastroke, or butterfly.')
            done = True
    elif co == 'China':
        swi = input('Please choose a swimmer: ' )
        if swi == 'Sun Yang':
            st = input('Now choose which stroke you wish to compete with: ')
            #done = True
            if st == 'freestyle':
                print(bec, st, win)
            elif st == 'backstroke':
                print(bec, st, lose)
            elif st == 'breastroke':
                print(bec, st, lose)
            elif st == 'butterfly':
                print(bec, st, lose)
            else:
                print('Please type in either freestyle, backstroke, breastroke, or butterfly.')
            done = True
        elif swi == 'Fu Yuanhui':
            st = input('Now choose which stroke you wish to compete with: ')
            if st == 'freestyle':
                print(bec, st, lose)
            elif st == 'backstroke':
                print(bec, st, win)
            elif st == 'breastroke':
                print(bec, st, lose)
            elif st == 'butterfly':
                print(bec, st, lose)
            else:
                print('Please type in either freestyle, backstroke, breastroke, or butterfly.')
            done = True
        else: print(pp)
    else:
        print(coun)
