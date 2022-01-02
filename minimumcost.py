# You are given an array of numbers  which contains positive as well as negative numbers . 
# The cost of the array can be defined as C(X)
# c(x) = |A1+T1|+|A2+T2|+...+|An+Tn|, where T is the transfer array which contains N zeros initially.

#You need to minimize this cost . 
# You can transfer value from one array element to another if and only if the distance between them is 
# at most K.

#Also, transfer value can't be transferred further.

#Say array contains 3,-1,-2 and k=1

#if we transfer 3 from 1 element to 2 , the array becomes Original Value -3, -1, -2

# Transferred value -3,3,0
# c(x)= |3-3|+|-1+3|+...+|-2+0|=4 which is minimum in this case

#Input:

#First line contains N and K separated by space

#Second line denotes an array of size N

#Output

#Minimum value of C(X)

size,k = map(int, input().split())

arr = map(int, input().split())


 

total=0

counter=0

m=k

flag=False


 

for i in arr:


 

    if flag==False:

            if(i>=0):

                counter=counter+1

                total=total+i

                m=k

            else:

                if(counter==0):

                    print(abs(sum(arr)+i))

                    flag=True

                else:

                    m-=1

                    if(m<0):

                        total=total+abs(i)

                    else:

                        total=total+i

    else:

        break


 

if flag==False:

    print(abs(total))