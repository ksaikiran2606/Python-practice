
# Print the 1 to n factorial number 
num = int(input("Enter a number: ")) 
count = 1 
for i in range(1, num + 1):
    count = count * i
print("The sum of all numbers from 1 to", num, "is:", count)  





# print the largest and smallest number from a list of numbers
num = input("Enter a number: ").split() 
largest = int(num[0])
smallest = int(num[0])

for i in range(len(num)):
    if int(num[i]) > int(largest):
        largest = int(num[i])
    elif int(num[i]) < int(largest):
        smallest = int(num[i])
print("Largest number is:", largest)
print("Smallest number is: ",smallest)      


