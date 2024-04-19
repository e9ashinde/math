def answer():
    n=100
    f1=sum([i**2 for i in range(n+1)])
    f2=(sum([i for i in range(n+1)]))**2
    return f2-f1
print(answer())

def solver(p,q):
    sum_of_square=(q*(q+1)*(2*q+1)-p*(p-1)*(2*p-1))//6
    square_sum=(((q*(q+1))//2)-((p*(p-1))//2))**2
    return square_sum-sum_of_square
print(solver(1,1000000))

                     
                      