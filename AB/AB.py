from B import B
class ABClass():
    def __init__(self):
        pass
    def print_ab(self,name):
        print("AB.print_ab()",name)
if __name__=="__main__":
    obj_ABclass=ABClass()
    obj_ABclass.print_ab(" from AB.AB.py")
    obj_Bclass=B.BClass()
    obj_Bclass.print_b(" from AB.AB.py")