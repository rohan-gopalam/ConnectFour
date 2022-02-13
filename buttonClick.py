from nextTurn import nextturn
from checkWin import checkwin
from mmai import aimove


def buttonclick(col):
    global positions, turn, color, buttons, ai, depth
    winner = checkwin(positions)
    if winner[1] is False:
        place = False
        for k in range(6):
            if positions[5 - k][col] == " " and place is False:
                positions[5 - k][col] = turn
                buttons[5 - k][col].configure(bg=color)
                place = True
        if place:
            nt = nextturn(turn, color)
            turn = nt[0]
            color = nt[1]
            winner = checkwin(positions)
            if winner[1]:
                print(winner[0])
            if ai:
                bestPlay = aimove(positions, depth)
                place = False
                for row in range(6):
                    if positions[5 - row][bestPlay] == " " and place is False:
                        positions[5 - row][bestPlay] = turn
                        buttons[5 - row][bestPlay].configure(bg=color)
                        place = True
                nt = nextturn(turn, color)
                turn = nt[0]
                color = nt[1]
                winner = checkwin(positions)
                if winner[1]:
                    print(winner[0])
        #for row in range(6):
            #print(positions[row])


positions = [[" ", " ", " ", " ", " ", " ", " "],
             [" ", " ", " ", " ", " ", " ", " "],
             [" ", " ", " ", " ", " ", " ", " "],
             [" ", " ", " ", " ", " ", " ", " "],
             [" ", " ", " ", " ", " ", " ", " "],
             [" ", " ", " ", " ", " ", " ", " "]]
turn = "X"
color = 'red'
buttons = [[], [], [], [], [], []]
ai = True
depth = 5
