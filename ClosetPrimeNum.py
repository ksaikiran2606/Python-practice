def prime_number(num):
    count = 0
    for i in range(1,num+1):
        if num % i == 0:
            count += 1
    if count == 2:
        return True
    else:
        return False
        
def closet_prime(num):
    front = num 
    back  = num-1 
    while True:
        if (prime_number(front)):
            return front
        elif (prime_number(back)):
            return back 
        front = front + 1 
        back  = back  - 1 

num = int(input("Enter a number :-- "))
print(closet_prime(num))