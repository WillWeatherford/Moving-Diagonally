

# this grid starts at lower left
def main(inp):
    grid_map = make_grid_map(inp)
    print('Grid map: {}'.format(grid_map))
    waypoints = [pos for pos, value in grid_map.items() if value == 'X']
    waypoints.sort(key=sum)
    subpaths = make_subpaths(waypoints)
    print('Subpaths: {}'.format('\n'.join((str(s) for s in subpaths))))
    paths = [find_paths(orig, dest) for orig, dest in subpaths]
    total = 1
    for n in paths:
        total *= n
    return total


def make_grid_map(inp):
    print('Making grid map...')
    lines = [l for l in inp.split('\n') if l]
    size, rows = lines[0], lines[1:]
    grid_map = {(x, y): value
                for y, row in enumerate(rows[::-1])
                for x, value in enumerate(row)}
    return grid_map


def make_subpaths(waypoints):
    print('Making subpaths from {}'.format(waypoints))
    subpaths = []
    for i, pos in enumerate(waypoints):
        if i + 1 < len(waypoints):
            subpaths.append((pos, waypoints[i + 1]))
    return subpaths


def find_paths(orig, dest):
    if orig == dest:
        return 1
    if orig[0] > dest[0] or orig[1] > dest[1]:
        return 0
    paths = find_paths(up(orig), dest) + \
        find_paths(right(orig), dest) + \
        find_paths(diag(orig), dest)
    print('{} paths found from {} to {}'.format(paths, orig, dest))
    return paths


def up(pos):
    return pos[0], pos[1] + 1


def right(pos):
    return pos[0] + 1, pos[1]


def diag(pos):
    return pos[0] + 1, pos[1] + 1
