from mm import minimax


def aimove(p, depth):
    scenario = p
    d = depth
    place = False
    bestScore = -2
    bestMove = 0
    bestMoves = depth + 1

    for col in range(7):
        for k in range(6):
            if scenario[5 - k][col] == " " and place is False:
                scenario[5 - k][col] = "O"
                findNextBest = minimax(scenario, False, d, 0)
                scenario[5-k][col] = " "
                place = True
                if findNextBest[0] > bestScore:
                    bestScore = findNextBest[0]
                    bestMoves = findNextBest[1]
                    bestMove = col
                elif findNextBest[0] == bestScore:
                    if findNextBest[1] > bestMoves and bestScore == -1:
                        bestScore = findNextBest[0]
                        bestMoves = findNextBest[1]
                        bestMove = col
                    elif findNextBest[1] < bestMoves and bestScore == 1:
                        bestScore = findNextBest[0]
                        bestMoves = findNextBest[1]
                        bestMove = col
        place = False
    return bestMove

