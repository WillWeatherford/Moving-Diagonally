
def main(inp):
    '''
    Take multi-line string of problem grid; return total number of paths
    between positions of Xs, starting from lower left.
    '''
    rows = inp.splitlines()

    # find all positions of "X" characters within the multi line string input.
    # reverse iterate on rows with [::-1] slice, so we start from bottom row.
    xpoints = [(x, y)
               for y, row in enumerate(rows[::-1])
               for x, value in enumerate(row)
               if value == 'X']

    # Make sure we start at lowest-leftest possible of all "X" positions.
    xpoints.sort(key=sum)

    # Get the sequence of pairs of X position waypoints, e.g.
    # ((0, 0), (1, 1)), ((1, 1), (2, 2)) ...
    subpaths = [(pos, xpoints[i + 1])
                for i, pos in enumerate(xpoints)
                if i < len(xpoints) - 1]

    # Call the recursive sum_paths function to find the number of possible
    # paths between each pair of waypoints along the way.
    subpath_sums = [sum_paths(orig, dest) for orig, dest in subpaths]

    # Python has no product function;
    # use lambda to find paths1 * paths2 * paths3 ... all possible paths.
    return reduce(lambda n, m: n * m, subpath_sums)


def sum_paths(orig, dest):
    '''
    Take two positions and return the total number of paths between them, by
    recursively finding each branching path possibility between the positions.
    '''
    # If given origin is the same as the destination, we've finished a complete
    # path.
    if orig == dest:
        return 1

    # If the origin is somehow above or to the right of the destination, we've
    # gone out of bounds onto an invalid path.
    if orig[0] > dest[0] or orig[1] > dest[1]:
        return 0

    return sum((sum_paths(up(orig), dest),
                sum_paths(right(orig), dest),
                sum_paths(diag(orig), dest)))

# 3 helper functions to identify positions up, to the right and diagonally
# up-right from a given pos


def up(pos):
    return pos[0], pos[1] + 1


def right(pos):
    return pos[0] + 1, pos[1]


def diag(pos):
    return pos[0] + 1, pos[1] + 1
