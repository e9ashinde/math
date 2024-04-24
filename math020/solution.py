def answer():
  n=100
  prod=1
  for i in range(1,n+1):
    prod*=i
  s=str(prod)
  l=[int(i) for i in s]
  return sum(l)
print(answer())


def solver(n):
  prod=1
  for i in range(1,n+1):
    prod*=i
  s=str(prod)
  l=[int(i) for i in s]
  return sum(l)
print(solver(100))