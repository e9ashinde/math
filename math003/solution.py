Part A:
def answer():
  x=600,851,475,143
  l=[]
  for i in range(1,max(x)+1):
    c=0
    for j in range(2,i+1):
      if i%j==0:
        c+=1
    if c==1:
      l.append(i)
  c={}
  for i in x:
    for j in l:
      if i%j==0:
        c[i]=j
  return c
print(answer())

def solver(n):
  ls=[i for i in range(1,n) if n%i==0]
  lst=[]
  for i in ls:
    c=0
    for j in range(2,i+1):
      if i%j==0:
        c+=1
    if c==1:
       lst.append(i)
  return max(lst)

print(solver(200))
