graph ={
    "S":[("A",1),("G",10)],
    "A":[("B", 2),("C",1)],
    "B":[("D",5)],
    "C":[("D", 3),("G", 4)],
    "D":[("G", 2)],
    "G":[]
}

hueristic = {
    "S":5,
    "A":3,
    "B":4,
    "C":2,
    "D":6,
    "G":0
}

def Astar(start, goal):
    open_list = [(hueristic[start], start)]
    closed_list = []
    while len(open_list) != 0:
        open_list.sort(key = lambda x: x[0])
        val, node = open_list.pop(0)
        closed_list.append((val, node))
        for next_node, value in graph[node[-1]]:
            open_list.append((val+value+hueristic[next_node]-hueristic[node[-1]], node+next_node))
    closed_list.sort(key = lambda x: x[0])
    for val, p in closed_list:
        if goal == p[-1]:
            path = ''
            for node in p:
                path += node+'->'
            print(f"Path : {path}\b\b, Cost : {val}")
            break

start = "S"
goal = "G"
Astar(start, goal)