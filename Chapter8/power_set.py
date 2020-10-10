from itertools import chain
from itertools import combinations


def power_set(iterable) -> list:
    s = list(iterable)
    return list(chain.from_iterable(combinations(s, r) for r in range(len(s)+1)))


if __name__ == '__main__':
    print(power_set('abcde'))
