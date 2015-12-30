

# this grid starts at lower left
def main(inp):
    rows = inp.split('\n')
    xpoints = [(x, y)
               for y, row in enumerate(rows[::-1])
               for x, value in enumerate(row)
               if value == 'X']
    xpoints.sort(key=sum)
    subpaths = [(pos, xpoints[i + 1])
                for i, pos in enumerate(xpoints)
                if i < len(xpoints) - 1]
    print('Subpaths: {}'.format('\n'.join((str(s) for s in subpaths))))
    paths = [find_paths(orig, dest) for orig, dest in subpaths]
    total = 1
    for n in paths:
        total *= n
    return total


def find_paths(orig, dest):
    if orig == dest:
        return 1
    if orig[0] > dest[0] or orig[1] > dest[1]:
        return 0
    paths = sum((find_paths(up(orig), dest),
                find_paths(right(orig), dest),
                find_paths(diag(orig), dest)))
    print('{} paths found from {} to {}'.format(paths, orig, dest))
    return paths


def up(pos):
    return pos[0], pos[1] + 1


def right(pos):
    return pos[0] + 1, pos[1]


def diag(pos):
    return pos[0] + 1, pos[1] + 1
