replace1=""
#flag="print"
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
result=0
operator=input("please choose an option (1,2,3,4,5):")
if operator=="1":
    replace1="addition"
    result=num1+num2
if operator=="2":
    if num1<num2:
        flag="do not print"
        print("cannot substrat the first number is less thsn the second ")
    else:
        flag="print"
        replace1="subtration"
        result=num1-num2
if operator=="3":
    if num2==0 or num1==0:
        print("cannot multiply by zero")
    else:
        result=num1*num2
        print("the result of multiplication of",num1,"and",num2,"is",result)
    #replace1="multiplication"
    #result=num1*num2
if operator=="4":
    if num2==0:
        print("cannot divide by zero")
    else:
        result = num1 // num2
    #replace1 = "division"
    #result = num1 // num2
    print("the result of multiplication of", num1, "and", num2, "is", result)

if operator=="5":
    if num2==0:
        print("cannot modulus by zero")
    else:
        result = num1 % num2

   # replace1 = "modulus"
    #result = num1 % num2
    print("the result of modulus of ",num1,"and",num2,"is",result)
#if flag=="print":
#print("the result of",replace1,"of",num1,"and",num2,"is",result)





