#Given number is Harshad number or not 

num = input("Enter a number :")

s = 0 
for i in num:
    s = s + int(i) 

if (int(num) % s == 0):
    print(num, "is a Harshad number")
else:
    print(num, "is not a Harshad number")