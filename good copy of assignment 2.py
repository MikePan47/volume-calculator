## main will check to see if the user input was correc (i.e. C, P, E, OR Q)
#if input was correct, main will call on one of the functions to compute the volume based on the user input
# if input was incorrect, main will continue to ask user until user correctly inputs something.


def main():
    userInput = input("please input the shape you wish to calculate the volume for.\n  Input C for Cube, P for pyramid, E for ellipsoid, or Q to quit ")
    #hile userInput.upper != ("Q" or "C") or userInput.upper() != ("P" or "E"):
        #euserInput = input("please input the shape you wish to calculate the volume for.\n  Input C for Cube, P for pyramid, E for ellipsoid, or Q to quit ")
    while userInput.upper() != "Q" :
        if userInput.upper() == "C":
            cubeLength = float(input("please input the side length of the cube "))
            cube(cubeLength)
            userInput = input("please input the shape you wish to calculate the volume for.\n  Input C for Cube, P for pyramid, E for ellipsoid, or Q to quit ")
        elif userInput.upper() == "P":
            lengthPyramid= float(input("please input the length of the base of the pyramid "))
            heightPyramid = float(input("please input the height of the pyramid "))
            pyramid(lengthPyramid, heightPyramid)
            userInput = input("please input the shape you wish to calculate the volume for.\n  Input C for Cube, P for pyramid, E for ellipsoid, or Q to quit ")
        elif userInput.upper() == "E":
            radius1 = float(input("please input the length of the first radius "))
            radius2 = float(input("please input the length of the second radius "))
            radius3 = float(input("please input the length of the third radius "))
            ellipsoid(radius1, radius2, radius3)
            userInput = input("please input the shape you wish to calculate the volume for.\n  Input C for Cube, P for pyramid, E for ellipsoid, or Q to quit ")
        else:
            print("Input was incorrect, please try again ")
            userInput = input("please input the shape you wish to calculate the volume for.\n  Input C for Cube, P for pyramid, E for ellipsoid, or Q to quit ")

# will terminate program if user entered Q

    if userInput.upper() == "Q" and counter == 0 :
        print("You have come to the end of the session.\n You did not preform any volume calculations!")
    elif userInput.upper() == "Q" and counter != 0:
        print("You have come to the end of a session.\n The volumes you have calculated are below.\n cube ", cubeVolumeList, "\n pyramid ", pyramidVolumeList, "\n ellipsoid ", ellipsoidVolumeList)




# these are the lists that will be storing the volume information
# counter is used to see if any volumes have been calculated. if they have counter will be greater than 1


cubeVolumeList = []
pyramidVolumeList = []
ellipsoidVolumeList = []
counter = 0

#computes volume of a cube and stores the value to a list. it then sorts values from low to high.

def cube(area):
    volume = area**3
    volume = round(volume, 2)
    global cubeVolumeList
    cubeVolumeList.append(volume)
    cubeVolumeList.sort()
    print("The volume of a cube with length %.2f " % area, " is %.2f" % volume)
    global counter
    counter = counter + 1
    return cubeVolumeList

#computes volume of a pyramid and stores the value to a list. it then sorts values from low to high.
def pyramid(base, height):
    volume = (1/3 * ((base **2) * height))
    volum = round(volume, 2)
    global pyramidVolumeList
    pyramidVolumeList.append(volume)
    pyramidVolumeList.sort()
    print("The volume of a pyramid with base %.2f" % base, "and height %.2f" % height, "is %.2f" % volume)
    global counter
    counter = counter + 1
    return pyramidVolumeList

# computes volume of an epsilloid and stores the value to a list. it then sorts values from low to high.
def ellipsoid(r1, r2, r3):
    from math import pi
    volume = (((4/3) * pi) * (r1 * r2 * r3))
    volume = round(volume, 2)
    global ellipsoidVolumeList
    ellipsoidVolumeList.append(volume)
    ellipsoidVolumeList.sort()
    print("The volume of an epsilloid with radius1 %.2f" % r2, "radius2 %.2f" % r2, "and radius3 %.2f" % r3, "is %.2f" % volume)
    global counter
    counter = counter + 1
    return ellipsoidVolumeList


#calls main and begins the program
main()
