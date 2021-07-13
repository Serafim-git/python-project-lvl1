print('Welcome to the Brain Game!')
user_name = input('May I have your name? ')
print('Hello ' + user_name + '! ' + 'What number is missing in this progression?')

q1 = int(input('Question: 14 .. 18 20 22 24 26 28 '))
if q1 == 16:
    print('Correct!')
else:
    print('Error! Try again!')

q2 = int(input('Question: 5 6 7 8 9 .. 11 12 '))
if q2 == 10:
    print('Correct!')
else:
    print('Error! Try again!')

q3 = int(input('Question: 12 15 18 21 .. 27 30 33 '))
if q3 == 24:
    print('Correct!')
    print('Congratulations, ' + user_name + '!')
else:
    print('Error! Try again!')

#test