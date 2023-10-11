'''
rock wins against paper
paper wins againts rock
scissors wins againts paper
'''
import random
#ROCK 0, PAPER 1, SCISSORS 2
'''
2-1 user
0-2 user
1-0 user

1-2 comp
2-0 comp
0-1 comp
'''

# def game():
#     user_in = int(input('Choose from ROCK-0, PAPER-1, SCISSORS-2 '))
#     if user_in  not in [0,1,2]:
#         print('Invalid Choice, Please Choose from 0 ,1 and 2 only')
#
#     else:
#         comp_in = random.randint(0,2)
#         def fun(user_in):
#             if user_in == 0:
#                 a='0 -> ROCK'
#             elif user_in ==1:
#                 a='1 -> PAPAER'
#             else:
#                 a='2 -> SCISSORS'
#             return a
#
#         print('YOUR SELECTION is:', fun(user_in))
#         print('COMPUTER SELECTION is:', fun(comp_in))
#
#
#
#         if user_in==comp_in:
#             print('DRAW')
#         elif user_in==2 and comp_in==1 or user_in==0 and comp_in==2 or user_in==1 and comp_in==0:
#             print('You Win')
#         else:
#             print('Computer Wins')
#         '''
#         elif user_in==2 and comp_in==1 or user_in==0 and comp_in==2 or user_in==1 and comp_in==0:
#             print('You Win')
#         '''
#
# rounds=print('We will be playing 5 rounds')
# for i in range(5):
#     game()

# import math
# print("This paint can paint upto 7 sq/m of area  ")
# a=int(input('Enter the width of the wall'))
# b=int(input('Enter the height of the wall'))
#
# total=(a*b)/7
#
# print(f'So the total cans required to paint your wall are/is: {math.ceil(total)}')

#CEASER CYPHER:

data='ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstvwxyz'
length=len(data)
msg='Deepakz'
lst=[]
def encrypt(msg):
    for j in msg:
        if j in data:
            # Find the index of the character in 'data'
            index = data.index(j)
            # Shift the character by 2 positions
            shifted_char = data[(index + 2) % length]  # (% length) wraps up the index when it ends.
            shifted_char
            # Append the shifted character to 'lst'
            lst.append(shifted_char)
encrypt(msg)
print(lst)

lst2=[]
def decrypt(msg):
    for j in msg:
        if j in data:
            # Find the index of the character in 'data'
            index = data.index(j)
            # Shift the character by 2 positions
            shifted_char = data[(index - 2) % length]  # (% length) wraps up the index when it ends.
            # Append the shifted character to 'lst'
            lst2.append(shifted_char)
decrypt(lst)
print(lst2)

a=''.join(lst2)
print(a)