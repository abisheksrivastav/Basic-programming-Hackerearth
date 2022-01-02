#Minimum dimension of the picture can be L x L, where L is the length of the side of square.

#Now Roy has N photos of various dimensions.
#Dimension of a photo is denoted as W x H
#where W - width of the photo and H - Height of the photo

#When any photo is uploaded following events may occur:

#[1] If any of the width or height is less than L, user is prompted to upload another one. 
# Print "UPLOAD ANOTHER" in this case.
#[2] If width and height, both are large enough and
#(a) if the photo is already square then it is accepted. Print "ACCEPTED" in this case.
#(b) else user is prompted to crop it. Print "CROP IT" in this case.

#(quotes are only for clarification)

#Given L, N, W and H as input, print appropriate text as output.

#Input:
#First line contains L.
#Second line contains N, number of photos.
#Following N lines each contains two space separated integers W and H.

#Output:
#Print appropriate text for each photo in a new line.

l = int(input())
n = int(input())
for i in range(n):
    w, h = map(int, input().split())
    if w < l or h < l:
        print("UPLOAD ANOTHER")
       
    else:
        if w==h:
            print("ACCEPTED")
        else:
            print("CROP IT")
    
    
    
