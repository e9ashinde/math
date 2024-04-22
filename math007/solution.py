primes=[]
def answer():
  n=10000000
  p=[True for i in range(n+1)]
  x=2
  while (x*x<=n):
    if (p[x]==True):
      for i in range(x*x,n+1,x):
        p[i]=False
    x+=1
  for t in range(2,n+1):
    if p[x]:
      primes.append(x)
if __name__=='__main__': 
  answer()
print(primes[10001])


def solver(n):
  x=10000
  lst=[]
  for i in range(1,x+1):
    c=0
    for j in range(2,i+1):
      if i%j==0:
        c+=1
    if c==1:
       lst.append(i)
  return lst[n]
print(solver(4))