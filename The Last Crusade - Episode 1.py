types = { 'D': [1, 3, 7, 8, 9, 12, 13],
          'LD': [4],
          'RD': [5],
          'RL': [2, 6],
          'L': [10],
          'R': [11]
          }
# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# w: number of columns.
# h: number of rows.
w, h = [int(i) for i in input().split()]
grid = []
for i in range(h):
    line = input()  # represents a line in the grid and contains W integers. Each integer represents one room of a given type.
    grid.append(line.split())
ex = int(input())  # the coordinate along the X axis of the exit (not useful for this first mission, but must be read).
# game loop
while True:
    xi, yi, pos = input().split()
    xi = int(xi)
    yi = int(yi)
    p = int(grid[yi][xi])
    x=xi
    y=yi
    if p in types['D']:
        y = yi+1

    elif p in types['LD']:
        if pos == 'TOP':
            x = xi - 1
        else:
            y = yi+1

    elif p in types['RD']:
        if pos == 'TOP':
            x = xi + 1
        else:
            y = yi+1

    elif p in types['RL']:
        if pos == 'LEFT':
            x = xi +1
        else:
            x = xi -1

    elif p in types['L']:
        x = xi-1

    elif p in types['R']:
        x = xi+1
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)


    # One line containing the X Y coordinates of the room in which you believe Indy will be on the next turn.
    print(x, y)