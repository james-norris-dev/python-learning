"""
Build an Adjacency List to Matrix Converter
* In this lab, you will build a function that converts an adjacency list
representation of a graph into an adjacency matrix
"""
def adjacency_list_to_matrix(graph):
    num_nodes = len(graph)
    matrix = []

    for node in range(num_nodes):
        connections = graph[node]
        row = []
        for destination in range(num_nodes):
            if destination in connections:
                row.append(1)
            else:
                row.append(0)
        print(row)
        matrix.append(row)
    return matrix

if __name__ == "__main__":
    print(adjacency_list_to_matrix({0: [1, 2], 1: [2], 2: [0, 3], 3: [2]}))
    print(adjacency_list_to_matrix({0: [1], 1: [0]}))
    print(adjacency_list_to_matrix({0: [], 1: [], 2: []}))