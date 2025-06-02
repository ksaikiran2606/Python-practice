# Print 1 to n even and odd numbers

num = int(input("Enter a number: ")) 

for i in range(1, num + 1):
    if i % 2 == 0:
        print(f"{i} is even")
    else:
        print(f"{i} is odd") 