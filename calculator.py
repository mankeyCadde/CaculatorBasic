#first we will make functions

def Add(z,y):
    return z + y

def subs(z,y):
    return z - y

def multiple(z,y):
    return z * y

def devide(z,y):
    if y == 0:
        return "this is the error by zero"
    else:
        return z/y
    
#now we will make one function that will do all works.......

def FCalculator():
    print("Select The Operation: ")
    print("1. Add")
    print("2. Substract")
    print("3. Multiply")
    print("4. Divide")


    while True:
        choise = input("Enter Your Choise (1/2/3/4): ")

        if choise in ['1', '2', '3', '4']:
            num1 = float(input("Enter First Number"))
            num2 = float(input("Enter Second Number"))



            if choise == '1':
                print(f"{num1} + {num2} = {Add (num1,num2)}")

            elif choise == '2':
                print(f"{num1} - {num2} = {subs (num1, num2)}")


            elif choise == '3':
                print(f"{num1} * {num2} = {multiple(num1,num2)}")


            elif choise == '4':
                print (f"{num1} / {num2} = {devide(num1,num2)}")


        #now we ended the work lets look if you stop or restart

        againCalc = input("Restart the Calculation Again  (y/n): ")
        if againCalc.lower() != "y":
            break

        print("thanks for your using our calculator:.....")



FCalculator()
#this will excute the function 