'''def factorial(n):
    if n==1 :
      result 
    else:
      result =n*factorial(n-1)
      return result
print(factorial(5))'''

def recursion(k):
   if(k>0):
      result=k+recursion(k-1)
      print(result)
   else:
      result=0
      return result
print("\n\nrecursion")
recursion(6)   