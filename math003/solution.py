# Part A  600,851,475,143
def answer():
  n=int(input())
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