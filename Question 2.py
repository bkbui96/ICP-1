#Take three digits number from the user then reverse it
num1 = int(input("Enter 3 numbers: "))
num2 = num1 % 10
num3 = (num1 % 100) // 10
num4 = num1 // 100

print(num2, num3, num4)