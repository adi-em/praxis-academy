class Adi: 
    def punya(self): 
        print(" punya adi") 

class Ida(Adi): 
    def punya(self): 
        print(" punya ida") 

class Dia(Adi): 
    def punya(self): 
        print("punya dia") 
  
 
class A(Ida, Dia): 
    pass
#A.mro()     
b = A() 
b.punya() 