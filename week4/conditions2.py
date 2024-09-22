def checkEven(value):
    if value % 2 == 0:
        return "the number is even"
    else:
       return "the number is odd"

def main():
    value= int(input("enter your number to check wether it is odd or even"))
    returnedResult= checkEven(value)
    print(returnedResult)

    main()



