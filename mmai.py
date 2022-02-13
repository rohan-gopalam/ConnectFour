from mm import minimax


def aimove(p, depth):
    scenario = p
    d = depth
    place = False
    bestScore = -2
    bestMove = 0

    for col in range(7):
        for k in range(6):
            if scenario[5 - k][col] == " " and place is False:
                scenario[5 - k][col] = "O"
                findNextBest = minimax(scenario, False, d)
                scenario[5-k][col] = " "
                place = True
                if findNextBest > bestScore:
                    bestScore = findNextBest
                    bestMove = col
        place = False
    return bestMove

