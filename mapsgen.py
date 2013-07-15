import random, pygame, sys
CHARS = {VOID : '0', LAND : '#' }


def mapGen():
    map = ''
    for line in xrange(1,61):
        newLine = '#'
        for tile in range(1,61):
            nextTile = random.randint(0,100)
            if newLine[tile-1] == '#':
                if nextTile >= 90:
                    newLine = newLine+ '0'
                if nextTile < 90:
                    newLine = newLine + '#'
            if newLine[tile-1] == '0':
                if nextTile >= 75:
                    newLine = newLine+ '#'
                if nextTile < 75:
                    newLine = newLine + '0'
        map= map + newLine + '\n'

    readableMap = open('unmapa.txt', 'a')
    readableMap.write(map)
    readableMap.close()



partHeight = 30
partWidth = 30
part1 = []


