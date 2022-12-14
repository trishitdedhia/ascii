from os.path import isfile
from PIL import Image
import sys
import os
from os import system

#Set number parameters
args = len(sys.argv)
#print(f'Total args = {args}')

#Default parameters
size = 150
ascii_string = " .:-=+*#%@"
filename = "__na__"

#Check parameters
ready = False
i=1
while i < args:

    #print(f'{sys.argv[i]}, {i}')

    # --width or -w
    if sys.argv[i] == "-w" or sys.argv[i] == "--width":
        if (i + 1 < args) and int(sys.argv[i + 1]) > 0:
            size = int(sys.argv[i + 1])
            i += 1
        else:
            #print(sys.argv[i])
            print("Value for --width not specified correctly")
            print("Invalid sytax, -w needs a positive integer")
            exit(1)

    # --set or -s
    elif sys.argv[i] == "-a" or sys.argv[i] == "--ascii":
        if i + 1 < args:
            if sys.argv[i + 1] == "invert":
                ascii_string = "@%#*+=-:. "
            elif sys.argv[i + 1] == "extended":
                ascii_string = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1[]?-_+~<>i!lI;:,^`'. "
            else:
                ascii_string = sys.argv[i + 1]
            i += 1
        else:
            print("Value for --set not specified correctly.")
            exit(1)

    # -s or --save
    elif sys.argv[i] == '-s' or sys.argv[i] == "--save":
        if i + 1 < args:
            filename = sys.argv[i + 1]
            i += 1
        else:
            print("Value for --save not specified correctly.")
            exit(1)
        

    #CHECK FOR THE LAST ARG
    elif i == args - 1:

        # HELP
        if sys.argv[i] == "--help" or sys.argv[i] == "-h":
            system('cat .help')
            exit(0)

        elif sys.argv[i] == "--version" or sys.argv[i] == "-v":
            system('head -1 .help')
            exit(0)

        # CHECK IMAGE
        elif os.path.isfile(sys.argv[i]) == True:
            ready = True
            break
        else:
            print("File not found")
            exit(1)

    #Go to next iteration
    else:
        print("Invalid syntax for passing arguments.")
        print("Please try using karla ascii --help")
        exit(1)

    #Increment loop iteration
    i += 1

#Ensure all arguments are passed properly and image is given
if ready == False:
    print("File not found")
    exit(1)

#Unpack string into 
index = [*ascii_string]

#fetch image and downsize
img = Image.open(sys.argv[i])
width , height = img.size
ratio = height / width

#convert to greyscale
img = img.convert('L')

#Scale image to required size
img = img.resize((size, round(size*ratio*0.5)))
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
if filename == "__na__":
    for x in ascii:
        print(f'{x}', end="")
else:
    with open(filename, 'w+') as f:
        for x in ascii:
            print(f'{x}', end="", file=f)

    
