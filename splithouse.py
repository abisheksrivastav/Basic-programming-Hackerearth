# You live in a village. The village can be represented as a line that contains n grids. 
# Each grid can be denoted as a house that is marked as H or a blank space that is marked as .. .

#A person lives in each house. A person can move to a grid if it is adjacent to that person. 
# Therefore, the grid must be present on the left and right side of that person.

#Now, you are required to put some fences that can be marked as B  on some blank spaces 
# so that the village can be divided into several pieces. 
# A person cannot walk past a fence but can walk through a house. 

#You are required to divide the house based on the following rules:

#A person cannot reach a house that does not belong to that specific person.
#The number of grids each person can reach is the same and it includes the grid 
# in which the house is situated.
#In order to show that you are enthusiastic and if there are many answers, 
# then you are required to print the one where most fences are placed.
#Your task is to decide whether there is a possible solution. Print the possible solution.

#Input Format
# First line: An integer  that represents the number of grids (1<=n<=20).
# Second line:  n characters that indicate the villages that are represented as H or .. .  
#Output format
#First line: If possible, then print YES. Otherwise, print NO.
#Second line: If the answer is YES , then print the way to do so.

n = int(input())
village = input()
if "HH" in village or "BB" in village:
    print("NO")
else:
    print("YES")
    print(village.replace(".","B"))

