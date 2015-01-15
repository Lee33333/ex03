"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""


def main():
    # repeat forever:
    while True:
        #    read input
        user_input = raw_input("Enter your operation > ")

    #    tokenize input
        tokens = user_input.split(" ")
        #print tokens
    #    if the first token is 'q', quit
        if tokens[0] == "q":
            return
    #    otherwise decide which math function to call based on the tokens we read


if __name__ == '__main__':
    main()
