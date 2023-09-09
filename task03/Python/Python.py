def is_prime(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:
            return False
    return True

n = int(input("Enter a number: "))
print("prime numbers up to", n, "are:")
for i in range(2,n+1):
    if is_prime(i):
        print(i,end=' ')