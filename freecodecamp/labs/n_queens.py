"""
 Implement the N-Queens problem solver using the depth-first search approach
"""
def dfs_n_queens(n: int) -> list[list[int]]:
    if n < 1:
        return []

    result = []

    cols = set()
    main_diagonal = set()
    anti_diagonal = set()

    def backtrack(row, current_solution):
        if row == n:
            result.append(current_solution[:])

        for col in range(n):
            if col in cols or (row - col) in main_diagonal or (row + col) in anti_diagonal:
                continue
            cols.add(col)
            main_diagonal.add(row - col)
            anti_diagonal.add(row + col)
            current_solution.append(col)

            backtrack(row + 1, current_solution)

            cols.remove(col)
            main_diagonal.remove(row - col)
            anti_diagonal.remove(row + col)
            current_solution.pop()


    backtrack(0, [])
    return result

if __name__ == "__main__":
    print(dfs_n_queens(1))
    print(dfs_n_queens(2))
    print(dfs_n_queens(3))
    print(dfs_n_queens(4))
    print(dfs_n_queens(5))
    print(len(dfs_n_queens(5)))
    print(len(dfs_n_queens(8)))