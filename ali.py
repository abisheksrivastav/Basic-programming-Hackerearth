# ali knows that a tag is valid if the sum of every two consecutive digits of 
# it is even and its letter is not a vowel. 
# Determine if the tag of the truck is valid or not.
#We consider the letters "A","E","I","O","U","Y" to be vowels for this problem.

# input format 
# The first line contains a string of length 9. 
# The format is "DDXDDD-DD", where D stands for a digit (non zero) and X is an uppercase english letter.
# output format
#Print "valid" (without quotes) if the tag is valid, print "invalid" otherwise (without quotes)

#sample input
#12X345-67
#sample output
# invalid

# explanination 
#The tag is invalid because the sum of first and second digit of it is odd 
# (also the sum of 4'th and 5'th, 5'th and 6'th and 8'th and 9'th are odd).
l=list(input())

s1=(int(l[0])+int(l[1]))%2

s2=(int(l[4])+int(l[3]))%2

s3=(int(l[5])+int(l[4]))%2

s4=(int(l[8])+int(l[7]))%2

if(s1+s2+s3+s4==0and l[2]not in"AEIOUY"):

    print("valid")

else:

    print("invalid")





    



s = input()
if len(s) != 9:
    print("invalid")
    exit()

for i in s:
    if i.isdigit():
        if int(i)%2==0:
            continue
        else:
            print("invalid")
            break
    else:
        if i in "AEIOUY":
            print("invalid")
            break
        
else:
    print("valid")
