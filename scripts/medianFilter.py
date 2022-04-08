import cv2
import numpy as np

filterWindowSize = 1
imgName = 'grainy-2.jpg'
img = cv2.imread(f"./images/{imgName}", flags=cv2.IMREAD_COLOR)

def getSurroundingValues(image, row, column, windowSize):
    returnList = []
    rowIndexList = listFromMinusNtoN(windowSize)
    columnIndexList = listFromMinusNtoN(windowSize)
    for rowIndex in rowIndexList:
        currentRow = row + rowIndex
        if currentRow < 0 or currentRow > len(img) - 1:
            continue
        for columnIndex in columnIndexList:
            currentColumn = column + columnIndex
            if currentColumn < 0 or currentColumn > len(img[0]) - 1:
                continue
            returnList.append(img[currentRow][currentColumn])


    return returnList


def listFromMinusNtoN(n):
    return list(range(-n,n + 1))

def getMedianFromList(pixelList):
    medianValues = [[], [], []]
    medians = []
    for pixel in pixelList:
        index = 0
        for value in pixel:
            medianValues[index].append(value)
            index += 1
    for valueIndex in range(len(medianValues)):
        median = np.median(medianValues[valueIndex])
        medians.append(median)
    return medians



for row in range(len(img)):
    for pixel in range(len(img[row])):
        valuesList = getSurroundingValues(img, row, pixel, filterWindowSize)
        medians = getMedianFromList(valuesList)
        img[row][pixel] = medians


cv2.imwrite(f"blurred-{imgName}", img)



