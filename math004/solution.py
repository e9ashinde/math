def palindrome(n):
  return str(n)==str(n)[::-1]
def answer():
  my_list=[]
  for n1 in range(100,1000):
    for n2 in range(100,1000):
      nums=n1*n2
      if palindrome(nums):
        my_list.append(nums)
  return max(my_list)

answer()

def palindrome(n):
  return str(n)==str(n)[::-1]
def solver(n,p=None,q=None):
  if p is None:
    p = 10 ** (n - 1)
  if q is None:
    q = 10 ** n - 1
  my_lst=[]
  for n1 in range(p, q):
    for n2 in range(p, q):
      nums = n1 * n2
      if palindrome(nums):
        my_lst.append(nums)
  return max(my_lst)

solver(2,100,1000)