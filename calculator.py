"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""
import arithmetic2

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
        else:
            if tokens[0] in ["+" , "-" , "*" , "/" , "square" , "cube" , "pow" , "mod"]:
                input_int1 = int(tokens[1])
                input_int2 = int(tokens[2])
                    #if tokens[0] ==
                print input_int1
                print input_int2 
                #[0] == ("+" , "-" , "*" , "/" , "square" , "cube" , "pow" , "mod"):
            #input_int1 = int(tokens[1])
            #input_int2 = int(tokesn[2])
            # answer = arithmetic2.add(int(tokens[1] , tokens[2])
            # print answer
            #print(input_int1 , input_int2)
       


if __name__ == '__main__':
    main()
