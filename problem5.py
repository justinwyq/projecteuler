"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

def divisible_by(num, div):
	result_list = [num % x for x in range(1,div + 1)]
	if max(result_list) == 0: return True
	else: return False

smallest_div20 = 0
x = 20
while smallest_div20 == 0:
	if divisible_by(x,20): smallest_div20 = x
	x += 20
print(smallest_div20)