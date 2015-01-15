"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""
import arithmetic2

def main():
    print"Enter your math problem starting with the operator and number(s) or type 'q' to quit the calculator"
    # repeat forever:
    while True:
        #    read input
        user_input = raw_input(">  ")

    #    tokenize input
        tokens = user_input.split()
        print(tokens)
        #print tokens
    #    if the first token is 'q', quit
        if tokens[0] == "q":
            break
    #    otherwise decide which math function to call based on the tokens we read
        elif tokens[0] in ["+" , "-" , "*" , "/" , "pow" , "mod"]:
            input_int1 = float(tokens[1])
            input_int2 = float(tokens[2])
            # if tokens[1] = False or tokens[2] = False:
            #     print "Those are not valid numbers. Try again."
            if tokens[0] == "+":
                answer = arithmetic2.add(input_int1 , input_int2)
                print answer
            if tokens[0] == "-":
                answer = arithmetic2.subtract(input_int1 , input_int2)
                print answer
            if tokens[0] == "*":
                answer = arithmetic2.multiply(input_int1 , input_int2)
                print answer
            if tokens[0] == "/":
                answer = arithmetic2.divide(input_int1 , input_int2)
                print answer
            if tokens[0] == "pow":
                answer = arithmetic2.power(input_int1 , input_int2)
                print answer
            if tokens[0] == "mod":
                answer = arithmetic2.mod(input_int1 , input_int2)
                print answer
        elif tokens[0] in ["square" , "cube"]:
            input_int1 = float(tokens[1])
            if tokens[0] == "square":
                answer = arithmetic2.square(input_int1)
                print answer
            if tokens[0] == "cube":
                answer = arithmetic2.cube(input_int1)
                print answer
        else:
            print "Invalid math operator or format. Try again"

if __name__ == '__main__':
    main()
