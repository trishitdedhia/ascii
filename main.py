from PIL import Image
import math
import sys

#greyscale to ascii index
#ascii_string = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1[]?-_+~<>i!lI;:,^`'. "
ascii_string = " .:-=+*#%@"
#ascii_string = "@%#*+=-:. "
index = [*ascii_string]

#fetch image and downsize
img = Image.open(sys.argv[1])
width , height = img.size
ratio = height / width

#convert to greyscale
img = img.convert('L')

#Scale image to required size
img = img.resize((150, round(150*ratio*0.5)))
width , height = img.size #Update the new size

#initialise new dataset
ascii = []

#get pixel data from image
data = img.getdata()

#Get divisor and set line character count
count = 0

#Run a loop for each pixel in th image
for item in data:
    #Map the greyscale value to the elements in our index
    ascii.append(index[round(((item/255)*len(index))-1)])
    count += 1
    #check if new line '\n' is needed.
    if count == width:
        ascii.append("\n")
        count = 0

#Print each pixel as an ascii character
for x in ascii:
    print(f'{x}', end="")

    
