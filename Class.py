
class classs():
    def __init__(self,math,spelling,English,PE):
        self.math=math
        self.spelling=spelling
        self.English=English
        self.PE=PE
    def d(self):
        print("math: "+str(self.math))
        print("spelling: "+str(self.spelling))
        print("English: "+str(self.English))
        print("PE: "+str(self.PE))
    def t(self):
        A=(self.math+self.spelling+self.English+self.PE)/4
        print(A)

student1=classs(7.8,5.2,10,9.6)
student1.d()
student1.t()