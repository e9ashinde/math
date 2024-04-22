def collatz_length(n, cache={1: 1}):
    if n not in cache:
        cache[n] = 1 + collatz_length(n // 2 if n % 2 == 0 else 3 * n + 1)
    return cache[n]

def answer():
    return max(range(1, 1000000), key=collatz_length)
print(answer())


def solver(p=None, q=None):
    if p is None and q is None:
        return None
    return max(range(1 if p is None else p, q + 1 if q is not None else p + 1), key=collatz_length)


print(solver(1))
print(solver(1, 100)) 