# 616167
# INTPROG Python coursework
# Semester 1, 2011/12

from graphics import *
from math import *

#defining constants
scale = 100
patchSize = 100
coloursNr = 4
minWidth = minHeight = 2
maxWidth = maxHeight = 8

#constants used by patch2
numberOfRows = 3
boatsPerRow = 4
sideTriangle = patchSize / boatsPerRow
triangleHeight = sideTriangle * sqrt(3) / 2
sticksPerColumn = 3
trapezoidsPerColumn = 3
spacesBetweenRows = 2
stickLength = (patchSize - numberOfRows * triangleHeight) / \
              (sticksPerColumn + trapezoidsPerColumn + spacesBetweenRows)
#end constants used by patch2


#constants used by patch1
numberOfSquares = 10
squareSide = patchSize / numberOfSquares
#end cosntants used by patch1

#end defining constants


def drawTriangle(win, boatX, boatY, colour):

    p1 = Point(boatX + sideTriangle / 2, boatY)
    p2 = Point(boatX, boatY + triangleHeight)
    p3 = Point(boatX + sideTriangle, boatY + triangleHeight)
 
    triangle = Polygon(p1, p2, p3)
    triangle.setFill(colour)
    triangle.draw(win)

def drawStick(win, boatX, boatY):
    
    p1 = Point(boatX, boatY)
    p2 = Point(boatX, boatY + stickLength)

    stick = Line(p1, p2)
    stick.draw(win)

def drawTrapezoid(win, boatX, boatY):
    
    p1 = Point(boatX, boatY)
    p2 = Point(sideTriangle + boatX, boatY)
    p3 = Point(boatX + sideTriangle - stickLength, boatY + stickLength)
    p4 = Point(boatX + stickLength, boatY + stickLength)

    trapezoid = Polygon(p1, p2, p3, p4)
    trapezoid.draw(win)


def drawBoat(win, boatX, boatY, colour):
    drawTriangle(win, boatX, boatY, colour)
    drawStick(win, boatX + sideTriangle / 2, boatY + triangleHeight)
    drawTrapezoid(win, boatX, boatY + triangleHeight + stickLength)

def drawBackground(win, x, y):
    backgroundP1 = Point(x, y)
    backgroundP2 = Point(x + patchSize, y + patchSize)
    background = Rectangle(backgroundP1, backgroundP2)
    background.setFill("white")
    background.draw(win)


def drawPatch2(win, x, y, colour):
    drawBackground(win, x, y)

    #drawing the boats
    for i in range(numberOfRows):
        for j in range(boatsPerRow):
            boatX = x + j * sideTriangle
            boatY = y + i * triangleHeight + numberOfRows * stickLength * i
            drawBoat(win, boatX, boatY, colour)
    #end drawing the boats


def drawPatch1(win, x, y, colour):
    
    drawBackground(win, x, y)

    px = patchSize - squareSide + x
    py = y
    i = numberOfSquares
    #drawing the squares
    while i >= 1:
        p1 = Point(px, py)
        p2 = Point(px + squareSide, py + squareSide)
        rectangle = Rectangle(p1, p2)
        rectangle.setFill(colour)
        rectangle.draw(win)
        px = px - squareSide
        py = py + squareSide
        i = i - 1
    #end drawing the squares

        
def drawPatchWork(win, width, height, colours):
    k = 0
    patchList = []
    for i in range(height):
        patchList.append([" "]*width)
    for i in range(height):
        for j in range(width):
            listValue = []
            patchColour = colours[k % coloursNr]
            k = k + 1
            if (i + j) % 2 == 0:
                drawPatch1(win, scale * j, scale * i, patchColour)
                patchType="patch1"
            else:
                drawPatch2(win, scale * j, scale * i, patchColour)
                patchType="patch2"
            listValue.append(patchType)
            listValue.append(patchColour)
            patchList[i][j] = listValue

    return patchList

def getInputs():
    valid = False
    while valid == False:
        width = input("Enter the patchwork's width: ")
        if width.isdigit():
            width = eval(width)
            if width >= minWidth and width <= maxWidth:
                valid = True
        if valid == False:
            print("The width has to be an integer between 2 and 8")
    valid = False
    while valid == False:
        height = input("Enter the patchwork's height: ")
        if height.isdigit():
            height = eval(height)
            if height >= minHeight and height <= maxHeight:
                valid = True
        if valid == False:
            print("The height has to be an integer between 2 and 8")

    colours = []
    colourNr = 0
    availableColours = ["red", "green", "blue", "yellow", "magenta", "cyan"]
    while colourNr < coloursNr:
        colour = input("Enter a patch colour: ")
        if (colour in availableColours) and (not (colour in colours)) :
            colourNr = colourNr + 1
            colours.append(colour)
        else:
            print("You entered an invalid colour ! ")
        
    return width, height, colours

def getClick(win, patchList):
    p = win.getMouse()
    px = p.getX()
    py = p.getY()
    patchLine = py // scale
    patchColumn = px // scale
    return patchLine, patchColumn

def drawNewPatch(win, patchLine, patchColumn, patchList):

    patchX = patchColumn * scale
    patchY = patchLine * scale
    
    patchType = patchList[patchLine][patchColumn][0]
    patchColour = patchList[patchLine][patchColumn][1]
    if patchType == "patch1":
        drawPatch1(win, patchX, patchY, patchColour)
    else:
        drawPatch2(win, patchX, patchY, patchColour)

    
def switchPatches(win, width, height, patchList):

    patchLine1, patchColumn1 = getClick(win, patchList)
    patchLine2, patchColumn2 = getClick(win, patchList)

    #switching the types and colours
    aux = patchList[patchLine1][patchColumn1]
    patchList[patchLine1][patchColumn1] = patchList[patchLine2][patchColumn2]
    patchList[patchLine2][patchColumn2] = aux
    #end switching the types and colours

    drawNewPatch(win, patchLine1, patchColumn1, patchList)
    drawNewPatch(win, patchLine2, patchColumn2, patchList)

    return patchList


def main():
    width, height, colours = getInputs()
    win = GraphWin("Patch Work", width * scale, height * scale)
    patchList = drawPatchWork(win, width, height, colours)
    #advanced feature
    while True:
        patchList = switchPatches(win, width, height, patchList)
    #end advanced feature

main()
