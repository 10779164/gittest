import sys

class student:
    name=''
    age=''
    def __init__(self,name,age):
	self.name= name
	self.age= age
b=sys.argv[1]
c=sys.argv[2]
a=student(b,c)
print a.name,a.age
