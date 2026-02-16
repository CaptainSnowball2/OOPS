
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
    def PassworD(self):
        Paass=int(input("Enter username: "))
        if Paass==self.username:
            paass=input("Enter password: ")
            if paass==self.password:
                print("Id : "+str(self.id))
                print("Type : "+self.type)
                print("Name : "+self.name)
                print("Battery : "+str(self.battery))    
            else:
                print("Wrong Password")
        else:
            print("Wrong Username")

         


    
phone1=phone(1,"Apple","E1",10,1111,"Apple174")
phone2=phone(2,"Apple","A10",90,2222,"Apple283")
phone3=phone(3,"Apple","G11",100,3333,"Apple392")
phone4=phone(4,"Samsung","F22",100,4444,"Samsung109")
phone5=phone(5,"Samsung","G2",99,5555,"Samsung316")
phone6=phone(6,"Samsung","A1G2",100,6666,"Samsung854")
phone7=phone(7,"Nokia","3310",10000,7777,"Nokia14789")
phone8=phone(8,"Nokia","3623",1000,8888,"Nokia159654")
phone9=phone(9,"Nokia","ultra 33109999 extra strong",100000000000,9999,"Nokia1459632")
phone9.PassworD()
phone8.PassworD()
phone7.PassworD()  
phone6.PassworD()  
phone5.PassworD()  
phone4.PassworD()  
phone3.PassworD()  
phone2.PassworD()  
phone1.PassworD()  
