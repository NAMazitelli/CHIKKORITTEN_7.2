import random, pygame, sys
STONE_M = 0
STONE_COR = 1
STONE_MU = 2
STONE_OFF = 3
ALLFORMS = [STONE_M, STONE_COR, STONE_MU, STONE_M, STONE_COR, STONE_MU, STONE_OFF]

def mapGen():
    map = ''
    topLeft = getPart()
    topRight = getPart()
    botLeft = getPart()
    botRight = getPart()
    #top = map(list, zip(topLeft, topRight))
    #bot = map(list, zip(botLeft, botRight))
    #map = top+bot
    #for column in map:
   #     map.join(column)
    return topLeft+topRight+botLeft+botRight
    #readableMap = open('unmapa.txt', 'a')
   # readableMap.write(map)
   # readableMap.close()



def getPart():
    part = []
    partHeight = 30
    partWidth = 30
    for column in range(partHeight):
        newCol = []
        for line in range(partWidth):
            newCol.append('#')
        part.append(newCol)

    part_pattern = random.choice(ALLFORMS)

    if part_pattern == STONE_M:
        return stoneMid(part)
    if part_pattern == STONE_COR:
        return stoneCorner(part)
    if part_pattern == STONE_MU:
        return multipleStones(part)
    if part_pattern == STONE_OFF:
        return part


def stoneMid(part):
    rockHeight = random.randint(4,10)
    rockWidth = random.randint(4,10)

    return generateStone(rockWidth, rockHeight, (15,15), part)

def stoneCorner(part):
    rockHeight = random.randint(4,10)
    rockWidth = random.randint(4,10)
    avCorners = ['TL', 'TR', 'BL', 'BR']
    corner = random.choice(avCorners)
    if corner == 'TL' or corner == 'TR':
        top = random.randint(1, 10)
    else:
        top = random.randint(15, 20)

    if corner == 'TL' or corner == 'BL':
        left = random.randint(1,10)
    else:
        left = random.randint(15, 20)
    part[top][left] = '0'

    return generateStone(rockWidth, rockHeight, (top + rockHeight/2, left + rockWidth/2), part)


def multipleStones(part):
    nStones= random.randint(2,4)
    stoneSize = int(15/nStones)
    for stone in range(nStones):
        part = generateStone(stoneSize, stoneSize, (random.randint(stoneSize+1, len(part)-(stoneSize+1)), random.randint(stoneSize+1, len(part)-(stoneSize+1))), part)
    return part




def generateStone(rockWidth, rockHeight, centre, part):
    X, Y = centre
    for i in range(int(Y-rockHeight/2), int(Y+rockHeight/2)):
        part[i][Y] = '0'
    for j in range(int(X-rockWidth/2), int(X+rockWidth/2)):
        part[X][j] = '0'

    for column in range(Y-rockHeight, Y+rockHeight):
        for tile in range(X-rockWidth, X+rockWidth):
            if column > 28:
                column = column-(column-28)
            if tile > 28:
                tile = tile-(tile-28)
            if part[column][tile] == '#':
                rockChances = 0
                if part[column-1][tile] == '0':
                    rockChances+=20
                if part[column+1][tile] == '0':
                    rockChances+=20
                if part[column][tile-1] == '0':
                    rockChances+=20
                if part[column][tile+1] == '0':
                    rockChances+=20
                nextTile = random.randint(0,100)
                if nextTile < rockChances:
                    part[column][tile] = '0'
                else:
                    part[column][tile] = '#'
    return part

print mapGen()


