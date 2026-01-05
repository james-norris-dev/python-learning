def hanoi_solver(n):
    rod_one = list(range(n, 0, -1))
    rod_two = []
    rod_three = []

    moves = [f"{rod_one} {rod_two} {rod_three}"]

    def move_disks(num_disks, source, target, auxiliary):
        if num_disks == 1:
            disk = source.pop()
            target.append(disk)
            moves.append(f"{rod_one} {rod_two} {rod_three}")
        else:
            move_disks(num_disks - 1, source, auxiliary, target)
            disk = source.pop()
            target.append(disk)
            moves.append(f"{rod_one} {rod_two} {rod_three}")
            move_disks(num_disks - 1, auxiliary, target, source)

    move_disks(n, rod_one, rod_two, rod_three)

    return '\n'.join(moves)