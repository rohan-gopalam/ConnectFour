from nextTurn import nextturn
from checkWin import checkwin


def buttonclick(col):
    global positions, turn, color, buttons
    place = False
    for k in range(6):
        if positions[5 - k][col] == " " and place == False:
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
