# You are given two arrays  a1,a2,a3...an and b1,b2,b3...bn. 
# In each step, you can set ai=ai-bi  if ai => bi. 
# Determine the minimum number of steps that are required to make all a's equal.

# input format

#First line:  n
#Second line: a1,a2,a3...an
#Third line: b1,b2,b3...bn

# output format
#Print the minimum number of steps that are required to make all 's equal. 
# If it is not possible, then print -1.

n = int(input())

a = list(map(int, input().split()))

b = list(map(int, input().split()))

count = 0

# sort both the lists together

a,b = (list(l) for l in zip(*sorted(zip(a,b)))) # 

a_min = a[0] #min value

i = 0

while(i < n):

    while(a[i] > a_min):

        a[i] -= b[i]

        count += 1

    if a[i] == a_min:

        i += 1

        continue

    if a[i] < b[i]:

        count = -1

        break

    if a[i] < a_min: #rare case

        a_min = a[i]

        i = 0

    continue

    i+= 1

print(count)
            






   
 