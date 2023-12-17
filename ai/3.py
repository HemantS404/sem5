graph = {
    "A":["B", "C"],
    "B":["D", "E"],
    "C":["F", "G"],
    "D":[],
    "E":[],
    "F":[],
    "G":[]
}

def dfs_dfid(node, vis, depth, max_depth):
    if depth<=max_depth:
        if node not in vis:
            print(node, end='-')
            vis.append(node)
        for next_node in graph[node]:
            if next_node not in vis:
                dfs_dfid(next_node, vis, depth+1, max_depth)

def dfid(max_depth):
    for depth in range(max_depth+1):
        dfs_dfid("A", [], 0, depth)
        print('\b ')

dfid(2)