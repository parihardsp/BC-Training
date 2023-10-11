def SilentAuction():
    check = True

    dict = {}
    while check:
        name = input('Enter The Name of Bidder: ')
        bid = int(input('Enter the Bid amount: '))
        dict[name] = bid
        check = input('Are there any bidder? \n No to exit, otherwise anything to continue : ').capitalize()
        if check == 'No':
            check = False
            print('List of all the bidders')
            print(dict)
        else:
            check = True

    # list out keys and values separately
    key_list = list(dict.keys())
    val_list = list(dict.values())

    maxx = max(val_list)
    # print key with val 100
    position = val_list.index(maxx)
    return f'The heighest bidder is : {key_list[position]}'


# print(SilentAuction())

import game_art

print(game_art.game_logo)
a = int(input('Enter the number'))
def cal(a):
    operations = ['+', "-", '*', "/"]
    sign=input('Enter the operation: ')
    b=int(input('Enter other number'))
    if sign=='+':
        c=a+b
        print(f"{a}{sign}{b}={c}")

    a=input(f'If you want to continue on {c}, press y else n ').lower()

    if a=='y':
        cal(c)
    else:
        return f"The total is {a}{sign}{b} = {c}

print(cal(a))