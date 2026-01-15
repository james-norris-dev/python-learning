"""
Build an Adjacency List to Matrix Converter
* In this lab, you will build a function that converts an adjacency list
representation of a graph into an adjacency matrix
"""
# def adjacency_list_to_matrix(graph):
#     num_nodes = len(graph)
#     matrix = []
#
#     for node in range(num_nodes):
#         connections = graph[node]
#         row = []
#         for destination in range(num_nodes):
#             if destination in connections:
#                 row.append(1)
#             else:
#                 row.append(0)
#         print(row)
#         matrix.append(row)
#     return matrix

# Converted the inner loop to list comprehension
# def adjacency_list_to_matrix(graph):
#     num_nodes = len(graph)
#     matrix = []
#
#     for node in range(num_nodes):
#         connections = graph[node]
#         row = [1 if destination in connections else 0 for destination in range(num_nodes)]
#         print(row)
#         matrix.append(row)
#     return matrix

# More Pythonic - Converted the outer loop into a list comprehension
def adjacency_list_to_matrix(graph: list):
    matrix = [[1 if destination in graph[node] else 0 for destination in range(len(graph))] for node in range(len(graph))]
    for row in matrix:
        print(row)

    return matrix
# if __name__ == "__main__":
#     print(adjacency_list_to_matrix({0: [1, 2], 1: [2], 2: [0, 3], 3: [2]}))
#     print(adjacency_list_to_matrix({0: [1], 1: [0]}))
#     print(adjacency_list_to_matrix({0: [], 1: [], 2: []}))