def m_to_n_prime_number(m,n):
    for i in range(m,n+1):
        if i > 1:
            count = 0 
            for j in range(2,i):
                if i % j == 0:
                    count += 1 
            if count == 0:
                print(i)

m = int(input("Enter a number :-- "))
n = int(input("Enter a number :--"))
m_to_n_prime_number(m,n)