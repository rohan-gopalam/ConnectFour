def nextturn(t, c):
    if t == "O":
        t = "X"
        c = 'red'
    else:
        t = "O"
        c = 'yellow'
    return [t, c]
