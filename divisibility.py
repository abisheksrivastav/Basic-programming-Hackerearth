# You are provided an array A of size N that contains non-negative integers. 
# Your task is to determine whether the number that is formed 
# by selecting the last digit of all the N numbers is divisible by 10 .

# Input Format
# First line: A single integer  N denoting the size of array A
# Second line: N space separated integers denoting the elements of array A

# output format
# Print YES if the number formed by selecting the last digit of all the N numbers is divisible by 10, else print NO.


# Sample Input
# 5
# 85 25 65 21 84

# Sample Output
# No 


# Explanation
# The number formed by selecting the last digit of all the numbers is 12345.
# Last digit of 85 is 5 .
# Last digit of 25 is 5 .
# Last digit of 65 is 5 .
# Last digit of 21 is 1 .
# Last digit of 84 is 4 .
# Hence, the number formed is 55514  by selecting the last digit of all the numbers is not divisible by 10.
# how to extract last digit of a number in a list in python
# last_digit = [int(i) % 10 for i in list_of_numbers]
# # from list to number in python
# last_digit = int(''.join(map(str, last_digit)))
#
# last_digit = int(str(number)[-1])

n = int(input())
numbers = list(map(int, input().split())) # map(int, input().split())
last_digit = [int(i) % 10 for i in numbers]  # list comprehension
la = int(''.join(map(str, last_digit)))  
if la % 10 == 0:
    print("Yes")
else:
    print("No")
 







