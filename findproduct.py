# You have been given an array A of size N consisting of positive integers. 
# You need to find and print the product of all the number in this array Modulo 10^9+7 .

#Input Format:
#The first line contains a single integer N denoting the size of the array. 
# The next line contains N space separated integers denoting the elements of the array

#Output Format:
#Print a single integer denoting the product of all the elements of the array Modulo 10^9+7 .
# how to import reduce function from functools module
from functools import reduce

n=int(input())
arr=list(map(int,input().split()))
# Print a single integer denoting the product of all the elements of the array Modulo 
# product of all the elements in the array
print(int(reduce(lambda x,y:x*y,arr))%(10**9+7)) # reduce function is used to find the product of all the elements in the array




