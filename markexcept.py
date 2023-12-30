'''class failexception(exception):
    def__inti__(self,arg)
    self.msg=arg
marks=int(input("enter you total marks:"))
if marks>=50:
    raise passexception("congrats you clear the semster")
if marks<=50:
    raise failexception("better lunk next time")
else:
     print("please enter valid name")'''

'''class invaliddata(exception):
  pass
marks=int(input("enter marks for marks:"))
try:
    if marks<0 or marks>100:
      raise invaliddata
except invaliddata:
 print("marks should be in between 0&100")'''

class invaliddata(Exception):
  pass
class invalidpass(Exception):
  pass
class invalidfail(Exception):
  pass
marks=int(input("enter marks for students:"))
try:
    if marks<=35 or marks>=100:
      raise invaliddata
      raiseinvalidmarks
except invaliddata:
 print("marks should be in between 0&100")
