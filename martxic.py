'''l=[[1,2,3],[4,5,6],[7,8,9]]
for r in l:
 for j in r:
   print(j,end='')
   print()'''
l=[[1,2,3],[4,5,6],[7,8,9]]
for r in range(len(l)):
 for j in range(len(l[r])):
   print(l[r][j],end= " ")
   print()