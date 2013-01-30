# Artur Salagean
# INTPROG Python coursework
# Semester 1, 2011/12

from graphics import *
from math import *

def drawBoat(win,column,row,colour,sideTriangle,triangleHeight,stickLength):

    #drawing the triangle
    px = sideTriangle / 2
    py = 0
    p1 = Point(px + column, py + row)
    
    px = 0
    py = triangleHeight
    p2 = Point(px + column, py + row)

    px = sideTriangle
    py = triangleHeight
    p3 = Point(px + column, py + row)
 
    triangle = Polygon(p1, p2, p3)
    triangle.setFill(colour)
    triangle.draw(win)
    #end drawing the triangle

    #drawing the stick
    stickX = sideTriangle / 2
    stickY = triangleHeight
    pStick1 = Point(stickX + column, stickY + row)

    stickY = stickY + stickLength
    pStick2 = Point(stickX + column, stickY + row)

    stick = Line(pStick1, pStick2)
    stick.draw(win)
    #end drawing the stick

    #drawing the trapezoid
    px = 0
    py = stickY
    p1 = Point(px + column, py + row)

    px = sideTriangle
    py = stickY
    p2 = Point(px + column, py + row)

    px = sideTriangle - stickLength
    py = stickY + stickLength
    p3 = Point(px + column, py + row)

    px = stickLength
    py = stickY+stickLength
    p4 = Point(px+column,py+row)

    trapez = Polygon(p1, p2, p3, p4)
    trapez.draw(win)
    #end drawing the trapezoid

def setPatchOutline(win, x, y):
    patchSize=100
    #setting patch outline
    backgroundP1 = Point(x, y)
    backgroundP2 = Point(x + patchSize, y + patchSize)
    background = Rectangle(backgroundP1, backgroundP2)
    background.setOutline("black")
    background.draw(win)
    #end setting patch outline

def drawPatch2(win, x, y, colour):

    #defining constants
    patchSize = 100
    numberOfRows = 3
    boatsPerRow = 4
    sideTriangle = patchSize / boatsPerRow
    triangleHeight = sideTriangle * sqrt(3) / 2
    stickLength = (patchSize - numberOfRows * triangleHeight) / 8
    #end defining constants

    setPatchOutline(win, x, y)

    #drawing the boats
    for i in range(numberOfRows):
        for j in range(boatsPerRow):
            column = j * patchSize / boatsPerRow + x
            row = i * triangleHeight + numberOfRows * stickLength * i + y
            drawBoat(win, column, row, colour, sideTriangle,triangleHeight,
                     stickLength)
    #end drawing the boats
        
    return "patch2"

def drawPatch1(win, x, y, colour):

    #defining constants
    patchSize=100
    numberOfSquares = 10
    px = 90 + x
    py = y
    i = numberOfSquares
    squareSide=patchSize/numberOfSquares
    #end defining constants

    setPatchOutline(win,x,y)

    #drawing the squares
    while i >= 1:
        p1 = Point(px, py)
        p2 = Point(px + squareSide, py + squareSide)
        rectangle=Rectangle(p1, p2)
        rectangle.setFill(colour)
        rectangle.draw(win)
        px = px - squareSide
        py = py + squareSide
        i = i - 1
    #end drawing the squares

    return "patch1"
        
def drawPatchWork(win, width, height, colours):
    k = 0
    patchList = []
    for i in range(height):
        patchList.append([" "]*width)
    for i in range(height):
        for j in range(width):
            listValue = []
            patchColour = colours[k % 4]
            k = k + 1
            if (i + j) % 2 == 0:
                patchType = drawPatch1(win, 100*j, 100*i, patchColour)
            else:
                patchType = drawPatch2(win, 100*j, 100*i, patchColour)
            listValue.append(patchType)
            listValue.append(patchColour)
            patchList[i][j] = listValue

    return patchList

def getInputs():
    valid=False
    while valid==False:
        width=input("Enter the patchwork's width: ")
        if width.isdigit():
            width=eval(width)
            if width>=2 and width<=8:
                valid=True
        if valid==False:
            print("The width has to be an integer between 2 and 8")
    valid=False
    while valid==False:
        height=input("Enter the patchwork's height: ")
        if height.isdigit():
            height=eval(height)
            if height>=2 and height<=8:
                valid=True
        if valid==False:
            print("The height has to be an integer between 2 and 8")

    colours=[]
    colourNr=0
    availableColours=["red","green","blue","yellow","magenta","cyan"]
    while colourNr<4:
        colourNr=colourNr+1
        validColour=False
        while validColour==False:
            colour=input("Enter a patch colour: ")
            if colour in availableColours:
                validColour=True
                colours.append(colour)
            else:
                print("You entered an invalid colour !")
        
    return width,height,colours

def getClick(win, patchList):
    p = win.getMouse()
    px = p.getX()
    py = p.getY()
    patchLine = py // 100
    patchColumn = px // 100
    patchType = patchList[patchLine][patchColumn][0]
    colour = patchList[patchLine][patchColumn][1]
    return colour, patchType, patchLine, patchColumn

def makeWhite(win, whiteX, whiteY):
    p1 = Point(whiteX, whiteY)
    p2 = Point(whiteX + 100, whiteY + 100)
    whiteRectangle = Rectangle(p1, p2)
    whiteRectangle.setFill("white")
    whiteRectangle.setOutline("black")
    whiteRectangle.draw(win)


def drawNewPatch(win,patchType,patchLine,patchColumn,patchColour):

    makeWhite(win,patchLine,patchColumn)

    if patchType=="patch1":
        drawPatch1(win,patchLine,patchColumn,patchColour)
    else:
        drawPatch2(win,patchLine,patchColumn,patchColour)

    
def switchPatches(win, width, height, patchList):

    patchColour1, patchType1, patchLine1, patchColumn1=getClick(win, patchList)
    patchColour2, patchType2, patchLine2, patchColumn2=getClick(win, patchList)

    aux=patchList[patchLine1][patchColumn1]
    patchList[patchLine1][patchColumn1]=patchList[patchLine2][patchColumn2]
    patchList[patchLine2][patchColumn2]=aux

    patchY1=patchLine1*100
    patchY2=patchLine2*100
    patchX1=patchColumn1*100
    patchX2=patchColumn2*100

    drawNewPatch(win,patchType2,patchX1,patchY1,patchColour2)
    drawNewPatch(win,patchType1,patchX2,patchY2,patchColour1)

    return patchList


def main():
    width, height, colours = getInputs()
    win = GraphWin("Patch Work", width*100, height*100)
    win.setBackground("white")
    patchList = drawPatchWork(win, width, height, colours)
    #advanced feature
    while True:
        patchList = switchPatches(win, width, height, patchList)
    #end advanced feature

main()    
