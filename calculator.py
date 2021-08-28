def add(x,y):
    return x + y
def subtract(x,y):
    return x - y
def multiply(x,y):
    return x * y
def divide(x,y):
    return x / y
while True:
    print('Basic Calculator\nSelect your Operator')
    print('1. Add')
    print('2. Subtract')
    print('3. multiply')
    print('4. Divide')
    Operator = input("Select your input(1/2/3/4): ")
    if Operator in ('1','2','3','4'):
        try:
            num1 = float(input("Enter first Number: "))
            num2= float(input("Enter Second Number: "))
            if Operator in ('1'):
                ans = add(num1, num2)
                num1 = str(num1)
                num2 = str(num2)
                ans = str(ans)
                print(num1+'+'+num2 +'='+ans)
            if Operator in ('2'):
                ans = subtract(num1, num2)
                num1 = str(num1)
                num2 = str(num2)
                ans = str(ans)
                print(num1+ '-'+num2 +'='+ans)
            if Operator in ('3'):
                ans = multiply(num1, num2)
                ans = str(ans)
                num1 = str(num1)
                num2 = str(num2)
                print(num1+'*'+num2 +'='+ans)
            if Operator in ('4'):
                ans = divide(num1, num2)
                ans = str(ans)
                num1 = str(num1)
                num2 = str(num2)
                print(num1+'/'+num2 +'='+ans)
        except:
            print('Invalid Number')
        print('Next Challenge \n ')
    else:
        print('\nInvalid Operator\nTry Again\n ')
