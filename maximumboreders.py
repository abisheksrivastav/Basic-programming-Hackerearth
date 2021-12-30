# ou are given a table with n  rows and  m columns. Each cell is colored with white or black. 
# Considering the shapes created by black cells, what is the maximum border of these shapes?

#A shape is a set of connected cells. Two cells are connected if they share an edge. 
# Note that no shape has a hole in it.

#Input format

#The first line contains t denoting the number of test cases.
#The first line of each test case contains integers n,m  denoting the number of rows and columns of the matrix.
#  Here, '#' represents a black cell and '.' represents a white cell. 
#Each of the next n lines contains m integers.
#Output format

#Print the maximum border of the shapes.

# black cells represent # 
# white cells represent .

'''

I guess the border is a straight line vertical or horizontal, having '#' on one side and '.' on the other

I checked length of top and bottom borders only.

'''

t = int(input()) # test cases

for i in range(t):

    h, w = map(int, input().split())# height and width of the matrix

    p = ['.'*w] # adding extra dots on top, p is my matrix

    for j in range(h):

        c = input()

        p.append('.' + c + '.') # adding extra dots on left and right

    p.append('.'*w) # adding extra dots on bottom

 

    r = 0 # result

    # check for top boarder 

    for k in range(len(p)-1):

        b = 0 # length of border

        for l in range(len(p[0])):

            if p[k][l] == '.'and p[k+1][l] =='#':

                b += 1

            else:

                b = 0

            if b > r: r =b


 

    # checking for bottom boarder

    for k in range(len(p)-1,1,-1):

        b = 0

        for l in range(len(p[0])):

            if p[k][l] == '.'and p[k-1][l] =='#':

                b += 1

            else:

                b = 0

            if b > r: r =b

    print(r)
