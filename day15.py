#Constructor
class Test():

#Construtor
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c   
        print("I am a constructor") 
        print(a,b,c)

    def display(self):
        return self.a,self.b,self.c

obj=Test(12,13,14)
print(obj.display())
