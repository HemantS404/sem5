graph = {
    "A":["B", "C"],
    "B":["D", "E"],
    "C":["F", "G"],
    "D":[],
    "E":[],
    "F":[],
    "G":[]
}

def bfs():
    queue = ["A"]
    vis = []
    while len(queue) != 0:
        node = queue.pop(0)
        if node not in vis:
            print(node,end="-")
        for next_node in graph[node]:
            if next_node not in vis:
                queue.append(next_node)

bfs()
print('\b ')