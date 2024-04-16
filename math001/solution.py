def sum_of_multiples():
  return sum([i for i in range(1,1000) if i%3==0 or i%5==0])

print(sum_of_multiples())

def sum_of_multiples(lst,start,end):
  l=0
  for i in range(start,end+1):
    for j in lst:
      if i%j==0:
        l+=i
        break
  return l

print(sum_of_multiples([3,5,12],400,1842))
