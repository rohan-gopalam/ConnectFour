from checkWin import checkwin


def minimax(arr, isMax, depth):
    bestScore = 0
    scoreVal = {"X": -1, "O": 1, "no one": 0}
    d = depth - 1
    if d > 0:
        vals = checkwin(arr)
        win = vals[1]
        winner = vals[0]

        if win:
            score = scoreVal.get(winner)
            if isMax:
                bestScore = -2
                if bestScore <= score:
                    bestScore = score

            else:
                score = scoreVal.get(winner)
                bestScore = 2
                if bestScore >= score:
                    bestScore = score

        if not win:
            if isMax:
                bestScore = -2
                place = False
                for col in range(7):
                    for k in range(6):
                        if arr[5 - k][col] == " " and place is False:
                            arr[5 - k][col] = "O"
                            findNextBest = minimax(arr, False, d)
                            arr[5 - k][col] = " "
                            place = True
                            if findNextBest > bestScore:
                                bestScore = findNextBest
                    place = False

            else:
                bestScore = 2
                place = False
                for col in range(7):
                    for k in range(6):
                        if arr[5 - k][col] == " " and place is False:
                            arr[5 - k][col] = "X"
                            findNextBest = minimax(arr, True, d)
                            arr[5 - k][col] = " "
                            place = True
                            if findNextBest < bestScore:
                                bestScore = findNextBest
                    place = False

    return bestScore
