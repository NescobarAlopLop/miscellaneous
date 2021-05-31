def reachTheEnd(grid, maxTime):
    if reachEndHelper(
        grid=grid,
        max_time=maxTime,
        start_x=0,
        start_y=0,
    ):
        return 'Yes'

    return 'No'


def reachEndHelper(grid, max_time, start_x, start_y) -> bool:
    if max_time < 0:
        return False

    if start_x == len(grid[0]) - 1 and start_y == len(grid) - 1:
        return True

    if start_y + 1 < len(grid):
        if grid[start_y + 1][start_x] == '.':
            can_reach1 = reachEndHelper(
                grid=grid,
                max_time=max_time - 1,
                start_x=start_x,
                start_y=start_y + 1,
            )
            if can_reach1:
                return True
    elif start_x + 1 < len(grid[0]):
        if grid[start_y][start_x + 1] == '.':
            can_reach2 = reachEndHelper(
                grid=grid,
                max_time=max_time - 1,
                start_x=start_x + 1,
                start_y=start_y,
            )
            if can_reach2:
                return True

    return False


def next_steps(
    grid,
    location,
):
    for possible_edge in [
        (0, 1),
        (1, 0),
    ]:
        next_step = [sum(x) for x in zip(location, possible_edge)]
        if next_step[0] < len(grid[0]) and next_step[1] < len(grid):
            yield next_step[0], next_step[1]

    return


def reachTheEndBFS(
    grid,
    max_time,
    finish_x,
    finish_y,
):
    root = (0, 0)
    discovered = {root}
    q = [(root, 0)]

    while q:
        v, time_took = q.pop(0)
        if time_took > max_time:
            continue

        if v == (finish_x - 1, finish_y - 1):
            return 'Yes'

        for next_step in next_steps(grid=grid, location=v):
            if grid[next_step[1]][next_step[0]] == '.':
                if next_step not in discovered:
                    discovered.add(next_step)
                    q.append((next_step, time_took + 1))
            else:
                discovered.add(next_step)

    return 'No'


if __name__ == '__main__':
    grid = [
        '.#.',
        '.#.',
        '...'
    ]
    grid = [
        '..#.......',
        '#.........',
        '..........',
        '..........',
        '..........',
        '..........',
        '..........',
        '.........#',
        '.....##...',
        '........#.',
    ]

    steps = len(grid) * 2 - 2
    print(
        reachTheEnd(
            grid=grid,
            maxTime=steps,
        )
    )

    print(
        reachTheEndBFS(
            grid=grid,
            max_time=steps,
            finish_x=len(grid[0]),
            finish_y=len(grid),
        )
    )

    side = 499
    grid = [
        [
            '.'
            for i in range(side)
        ] for j in range(side)
    ]
    steps = side * 2 - 2
    print(
        reachTheEnd(
            grid=grid,
            maxTime=steps,
        )
    )

    print(
        reachTheEndBFS(
            grid=grid,
            max_time=steps,
            finish_x=len(grid[0]),
            finish_y=len(grid),
        )
    )
