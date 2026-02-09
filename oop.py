People={"phone1":"E1","phone2":"A10","phone3":"G11","phone4":"F22"}
A=input("Username: ")
if A in People:
    B=input("Password: ")
    if B==People[A]:
        print("Logged In Successfully")
    else:
        print("incorrect Password")
else:
    print("Incorrect Username")

class phone():
    def __init__(self,id,type,name,battery,username,password):
        self.id=id
        self.type=type
        self.name=name
        self.battery=battery
        self.username=username
        self.password=password
    def d(self):
        print("Id :"+str(self.id))
        print("Type :"+self.type)
        print("Name :"+self.name)
        print("Battery :"+str(self.battery))
phone1=phone(1,"Appel","E1",10,1111)
phone2=phone(2,"Appel","A10",90,2222)
phone3=phone(3,"Appel","G11",100,3333)
phone4=phone(4,"Samsung","F22",100,4444)
phone5=phone(5,"Samsung","G2",99,5555)
phone6=phone(6,"Samsung","A1G2",100,6666)
phone7=phone(7,"Nokia","3310",10000,7777)
phone8=phone(8,"Nokia","3623",1000,8888)
phone9=phone(9,"Nokia","ultra 33109999 extra strong",100000000000,9999)
phone9.d()
print(phone6.name)
                