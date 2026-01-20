"""
 Implement a graph traversal algorithm called depth-first search
"""

def dfs(matrix, node_label):
    stack = [node_label]
    visited = []

    while stack:
        current_node = stack.pop()
        if current_node in visited:
            continue
        visited.append(current_node)
        for i, connected in enumerate(matrix[current_node]):
            if connected == 1:
                stack.append(i)

    return visited

if __name__ == "__main__":
    print(dfs([[0, 1, 0, 0], [1, 0, 1, 0], [0, 1, 0, 1], [0, 0, 1, 0]], 1))
    print(dfs([[0, 1, 0, 0], [1, 0, 1, 0], [0, 1, 0, 1], [0, 0, 1, 0]], 3))
    print(dfs([[0, 1, 0, 0], [1, 0, 1, 0], [0, 1, 0, 0], [0, 0, 0, 0]], 3))
    print(dfs([[0, 1, 0, 0], [1, 0, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]], 3))
    print(dfs([[0, 1, 0, 0], [1, 0, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]], 0))