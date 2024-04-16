def answer():
   a,b=1,1
   total = 0
   while a <= 4000000:
      if a % 2 == 0:
        total += a
      a, b = b, a+b 
   return total

print(answer())

def solver(start, end, even=False,odd=False):
    fibs= [0, 1]
    while True:
        nxt_val = fibs[-1] + fibs[-2]
        if nxt_val > end:
            break
        if nxt_val >= start:
            print(nxt_val)
        fibs.append(nxt_val)
    even=[i for i in fibs if i%2==0 and i>=start]
    odd=[i for i in fibs if i%2!=0 and i>=start]
    return f'Even :{even}, Odd:{odd}'

print(solver(100,800))