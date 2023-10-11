import argparse
'''
--variable_name or --number1, makes the argument optional, now code will get executed fullt without throwing error, 
but syntax of command line changes from  <python CLI-argparse.py 4 10 multiply> to <python CLI-argparse.py --number1 4 --number2 10 --operation multiply>
If i want to restict user to enter certain commands i can use choices=[], inside parser.add_argument()

'''
if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("--number1", help="first_number")
    parser.add_argument("--number2", help="second_number")
    parser.add_argument("--operation", help="operation",
                        choices=['add','subtract','multiply','divide '])

    args = parser.parse_args()

    n1 = int(args.number1)  #as python takes everything as a string.
    n2 = int(args.number2)

    print(args.number1)
    print(args.number2)
    print(args.operation)

    if args.operation == 'add':
        result = n1 + n2
    elif args.operation == 'subtract':
        result = n1 - n2
    elif args.operation == 'multiply':
        result = n1 * n2
    elif args.operation == 'divide':
        result = n1 / n2
    else:
        result = 'Invalid Operation'

    print(f"result is {result}")

"""
Instead of using terminal/ command Lie, If you want to run it in PyCharm IDE
Run the file first.
Go to Run --> Edit Confrigurations --> Enter the Parameters --> Ok

"""