
class Solution(object):
    def wallsAndGates(self, rooms):

        wall = -1
        gate = 0
        unknown = 2147483647

        if not rooms or not rooms[0]:
            return

        rows = len(rooms)
        cols = len(rooms[0])

        currLevel = []

        for x in range(rows):
            for y in range(cols):
                if rooms[x][y] == gate:
                    currLevel.append( (x,y) )


        while currLevel:
            nextLevel = []
            for x,y in currLevel:
                currDist = rooms[x][y]

                for nx,ny in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
                    if 0<=nx<rows and 0<=ny<cols and rooms[nx][ny] == unknown:
                        rooms[nx][ny] = currDist + 1
                        nextLevel.append( (nx,ny) )

            currLevel = nextLevel
