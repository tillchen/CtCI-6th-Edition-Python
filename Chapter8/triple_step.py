from functools import lru_cache


@lru_cache(maxsize=None)
def triple_step(n: int) -> int:
    if n < 0:
        return 0
    if n in (0, 1):
        return 1
    return triple_step(n-1) + triple_step(n-2) + triple_step(n-3)


memo = {
    -1: 0,
    0: 1,
    1: 1,
}


def triple_step_memo(n: int) -> int:
    if n not in memo:
        memo[n] = triple_step_memo(n-1) + triple_step_memo(n-2) + triple_step_memo(n-3)
    return memo[n]


def triple_step_memo_iterative(n: int) -> int:
    for i in range(n+1):
        if i not in memo:
            memo[i] = memo[i-1] + memo[i-2] + memo[i-3]
    return memo[n]


if __name__ == '__main__':
    print(triple_step(50))
    print(triple_step_memo(50))
    print(triple_step_memo_iterative(50))
