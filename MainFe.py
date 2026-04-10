from Feature.Addition import add_tow_number
from Feature.sub import sub_two_num
from Feature.mul import mul

print("Hello This is my main application")

print("This is calculator")

num1= input("Enter num1: ")
num2=input("Enter num2: ")
if not num1.isnumeric() or not num2.isnumeric():
    print("enter correctly")

n1=int(num1)
n2=int(num2)



