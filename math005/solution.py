def answer():
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    def lcm(a, b):
        return a * b // gcd(a, b)
    result = 1
    for i in range(1, 20):
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
print(solver(3,30))