'''By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?'''


# inefficient prime checker
# def is_Prime(num):
#     if min([num % n for n in range(2, num)]):
#         return True
#     else:
#         return False

# efficient prime checker
def is_Prime(num):
    if num < 2:
        return False

    if num == 2:
        return True

    if num & 1 != 1:
        return False

    for x in range(3, int(num**0.5) + 1, 2):
        if num % x == 0:
            return False
    return True


num_prime = 6
x = 13

while num_prime < 10001:
    x += 2
    if is_Prime(x):
        num_prime += 1
        print(num_prime, x)
    if num_prime == 10001:
        print(x)
