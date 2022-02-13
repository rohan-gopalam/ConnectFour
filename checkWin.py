def checkwin(p):
    players = ["X", "O"]
    boardHeight = len(p[0])
    boardWidth = len(p)
    for tile in players:
        # check horizontal spaces
        for y in range(boardHeight):
            for x in range(boardWidth - 3):
                if p[x][y] == tile and p[x+1][y] == tile and p[x+2][y] == tile and p[x+3][y] == tile:
                    return tile, True

        # check vertical spaces
        for x in range(boardWidth):
            for y in range(boardHeight - 3):
                if p[x][y] == tile and p[x][y+1] == tile and p[x][y+2] == tile and p[x][y+3] == tile:
                    return tile, True

        # check / diagonal spaces
        for x in range(boardWidth - 3):
            for temp in range(boardHeight - 3):
                y = temp + 3
                if p[x][y] == tile and p[x+1][y-1] == tile and p[x+2][y-2] == tile and p[x+3][y-3] == tile:
                    return tile, True

        # check \ diagonal spaces
        for x in range(boardWidth - 3):
            for y in range(boardHeight - 3):
                if p[x][y] == tile and p[x+1][y+1] == tile and p[x+2][y+2] == tile and p[x+3][y+3] == tile:
                    return tile, True

    return "no one", False


