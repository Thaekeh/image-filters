import cv2
img = cv2.imread('./images/kolibri.jpg', flags=cv2.IMREAD_COLOR)
print(img[0][0])

def getSurroundingValues(image, row, column, windowSize):
    returnList = []
    rowIndexList = listFromMinusNtoN(windowSize)
    columnIndexList = listFromMinusNtoN(windowSize)
    for rowIndex in rowIndexList:
        currentRow = row + rowIndex
        if currentRow < 0:
            continue
        for columnIndex in columnIndexList:
            currentColumn = column + columnIndex
            if currentColumn < 0:
                continue
            returnList.append(img[currentRow][currentColumn])


    return returnList

    
def listFromMinusNtoN(n):
    return list(range(-n,n + 1))

def getMedianFromList(pixelList):
    medianValues = [[], [], []]
    for pixel in pixelList:
        index = 0
        for value in pixel:
            medianValues[index].append(value)
            index += 1
    print(medianValues)



for row in range(len(img)):
    if row == 1:
        break
    for pixel in range(len(img[row])):
        # get surrounding values
        if pixel == 1:
            break
        valuesList = getSurroundingValues(img, row, pixel, 1)
        median = getMedianFromList(valuesList)

# getSurroundingValues(img, 0, 0, 1)

# cv2.imwrite('./result.jpg', img)



