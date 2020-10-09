from functools import lru_cache


@lru_cache(maxsize=None)
def robot_grid(r: int, c: int) -> int:
    if r == 1 and c == 1:
        return 1
    if r == 1:
        return robot_grid(r, c-1)
    if c == 1:
        return robot_grid(r-1, c)
    return robot_grid(r-1, c) + robot_grid(r, c-1)


if __name__ == '__main__':
    print(robot_grid(10, 10))

