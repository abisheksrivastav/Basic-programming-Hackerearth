#You are conducting a contest at your college. 
# This contest consists of two problems and  n participants. 
# You know the problem that a candidate will solve during the contest.

#You provide a balloon to a participant after he or she solves a problem. 
# There are only green and purple-colored balloons available in a market. 
# Each problem must have a balloon associated with it as a prize for solving that specific problem. 
# You can distribute balloons to each participant by performing the following operation:

#Use green-colored balloons for the first problem and purple-colored balloons for the second problem
#Use purple-colored balloons for the first problem and green-colored balloons for the second problem
#You are given the cost of each balloon and problems that each participant solve. 
# Your task is to print the minimum price that you have to pay while purchasing balloons.

#Input Format
#First line:   T that denotes the number of test cases (1 <= T <= 10)
#For each test case: 
#First line: Cost of green and purple-colored balloons 
#Second line: n that denotes the number of participants (1 < n< 10)
#Next n lines: Contain the status of users. 
#For example, if the value of the j integer in the i row is 0, 
#then it depicts that the i participant has not solved the j problem. Similarly, 
#if the value of the   j integer in the i row is 1 , 
#then it depicts that the i participant has solved the j problem.

#Output Format
#For each test case, print the minimum cost that you have to pay while purchasing balloons.
 

testcase = int(input())
 

for tc in range(0,testcase):

    first, second = input().split(" ")

    if tc%2==0:

        first, second = int(first), int(second)

    else:

        second, first = int(first), int(second)

    participants = int(input())

    cost = 0

    for each_person in range(0, participants):

        value1, value2 = input().split(" ")

        cost = cost  + (int(value1) * first)

        cost = cost  + (int(value2) * second)

    print(cost)


