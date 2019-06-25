""" The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ? """

largest_prime_factor = 0

testnumber = 600851475143

# code below works but is inefficient
""" for x in reversed(range(1, testnumber+1)):
    if testnumber % x == 0:
        factorial_counter = 0
        for y in range(2, 1+x):
            if x % y == 0:
                factorial_counter += 1
            if factorial_counter > 1:
                break
        if factorial_counter == 1:
            largest_prime_factor = x
            break """

largest_prime_factor = 0
number_copy = testnumber
prime = 0
while largest_prime_factor == 0:
    for i in range(2, int(number_copy)+1):
        if number_copy % i == 0:
            prime = i
            number_copy /= i
            break
    if number_copy == 1:
        largest_prime_factor = prime
print(largest_prime_factor)
