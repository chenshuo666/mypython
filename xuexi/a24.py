class Student(object):
    def __init__(self,first='',last='',id=0):
        self.firstNameStr=first
        self.lastNameStr=last
        self.idInt=id

    def __str__(self):
        print('{} {},ID:{}'.format(self.firstNameStr,self.lastNameStr,self.idInt))

stu=Student('Chen','Shuo',1716087)
print(stu)