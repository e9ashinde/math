def lcm(a, b):
    while b:
        a, b = b, a % b
    return a

def answer():
    result = 1
    for i in range(2, 21):
        result = lcm(result, i)
    return result

print(answer())


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

def solver(p, q):
    p, q = min(p, q), max(p, q)
    result = p
    for i in range(p + 1, q + 1):
        result = lcm(result, i)
    return result
print(solver(4,9))