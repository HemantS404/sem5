graph = {
    "A":["B", "C"],
    "B":["D", "E"],
    "C":["F", "G"],
    "D":[],
    "E":[],
    "F":[],
    "G":[]
}

def dfs():
    stack = ["A"]
    vis = []
    while len(stack) != 0:
        node = stack.pop()
        if node not in vis:
            print(node, end='-')
            for next_node in graph[node]:
                stack.append(next_node)

dfs()
print('\b ')