from AB.B import B
from AB import AB
class AClass():
    def __init__(self):
        pass
    def print_a(self,name):
        print("A.print_a()",name)
if __name__=="__main__":
    obi_AClass=AClass()
    obi_AClass.print_a(" from A.A.py")
    obj_BClass=B.BClass()
    obj_BClass.print_b(" from A.A.py")
    obj_ABClass=AB.ABClass()
    obj_ABClass.print_ab(" from A.A.py")