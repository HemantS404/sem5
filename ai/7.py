graph = [
    [5, 5, 5, 5, 5, 5,5],
    [5,10,10,10,10,10,5],
    [5,10,15,10,15,10,5],
    [5,10,15,20,25,10,5],
    [5,10,55,15,15,10,5],
    [5,10,10,10,10,40,5],
    [5, 5, 5, 5, 5, 5,5]]

def score(x, y):
    return graph[x][y]

def hillClimbing():
    px, py = 0,0
    i_val = score(px, py)
    while True:
        print(px, py, i_val)
        moves = [[px-1,py],[px-1,py-1],[px,py-1],[px+1,py],[px+1,py+1],[px,py+1],[px-1,py+1],[px+1,py-1]]
        mx, my = 0, 0
        max_val = i_val
        for x, y in moves:
            if score(x, y) > max_val:
                mx, my = x, y
                max_val = score(x, y)
        if max_val > i_val:
            px, py = mx, my
            i_val = max_val
        else:
            break

hillClimbing()