from math import factorial
def nth_perms(n, digs):
    lst=[]
    digs=list(digs)
    sum_digs= len(digs)  
    for i in range(sum_digs, 0, -1):
        index = (n - 1) // factorial(i - 1)
        lst.append(digs.pop(index))
        n -= index * factorial(i - 1)
    return ''.join(lst)

def answer():
    return nth_perms(1000000, '0123456789')
print(answer())

def solver(n):
    chars="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    return nth_perms(n, chars)
print(solver(100)) 

