""" 
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

def isPalindrome(num):
	if str(num) == str(num)[::-1]:
		return True
	else:
		return False
		
largestPalindrome = 0
for m in range(901,1000):
	for n in range(901,1000):
		if isPalindrome(m*n) and m*n>largestPalindrome:
			largestPalindrome=m*n
			print(m,n)

print(largestPalindrome)
