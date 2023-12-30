def add(*args):
    sum=0
    for i in args:
        sum+= i
    return sum
result=add(1,2,3)
print('sum',result)  
result=add(-29,-100,90) 
print('sum',result)
def add(*args):
    count=0
    for i in args:
     count+= i
    return count
result=add(1,2,3)
print('count',result)
result=add(-29,-100,90) 
print('count',result)  