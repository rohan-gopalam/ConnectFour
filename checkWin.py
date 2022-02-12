def checkwin(p):
    players = ["X", "O"]
    count = 0

    for play in players:
        # horizontal check
        for r in range(6):
            for c in range(7):
                if p[r][c] == play:
                    count += 1
                    if count == 4:
                        return play, True
                else:
                    count = 0
        # vertical check
        for c in range(7):
            for r in range(6):
                if p[r][c] == play:
                    count += 1
                    if count == 4:
                        return play, True
                else:
                    count = 0
        # check / diagonal spaces
        for x in range(7 - 3):
            for y in range(3, 6):
                if p[x][y] == play and p[x + 1][y - 1] == play and p[x + 2][y - 2] == play and \
                        p[x + 3][y - 3] == play:
                    return play, True

        # check \ diagonal spaces
        for x in range(7 - 3):
            for y in range(6 - 3):
                if p[x][y] == play and p[x + 1][y + 1] == play and p[x + 2][y + 2] == play and \
                        p[x + 3][y + 3] == play:
                    return play, True

    return "no one", False
