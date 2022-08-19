print("*****       welcome to meff calculator    *********** ")
print("enter the number1:")
num1=int(input())
print("enter the number2:")
num2=int(input())
print("thses are the operation you can:")
print("1.Addition")
print("2.subtration")
print("3.multiplication")
print("4.division")
print("5.modulus")
a=input("please choose an option (1,2,3,4,5):")
def add(num1,num2):
    return num1+num2
if a=="1":
    result=add(num1,num2)
    print(" This is an addition")
    print(result)
def sub(num1,num2)  :
    return num1-num2
if a=="2":
    result=sub(num1,num2)
    print(" this is an substration")
    print(result)
def mul(num1,num2):
    return num1*num2
if a=="3":
    result=mul(num1,num2)
    print("This is an multiplication")
    print(result)
def div(num1,num2):
    return num1/num2
if a=="4":
    result = div(num1, num2)
    print(" this is an division")
    print(result)
def mod(num1,num2):
    return num1%num2
if a=="5":
    result=mod(num1,num2)
    print("this is an modulus")
    print(result)


