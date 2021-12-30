#You are required to enter a word that consists of x and y  that denote the number of Zs and Os respectively. 
# The input word is considered similar to word zoo if 2*x=y

# Determine if the entered word is similar to word zoo.

#For example, words such as zzoooo and zzzoooooo are similar to word zoo but not the words such as zzooo and zzzooooo.

#Input format

#First line: A word that starts with several Zs and continues by several Os.
#Note: The maximum length of this word must be 20.
#Output format

#Print Yes if the input word can be considered as the string zoo otherwise, print No.

word = input() # input word
for i in range(len(word)):#loop through the word
    if word[i] == 'z':   #if the letter is z
        z = word[i:].count('z')  #count the number of z
        o = word[i:].count('o')  #count the number of o
        # word zoo if 2*x=y
        if 2*z == o:  #if 2*z=o

            print("Yes")  #print yes
            break
        else:
            print("No")  #print no
            break #break the loop
else:
    print("No")  #if the loop is not broken, print no


 

