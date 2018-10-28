class myclass():
    def method1(self):
        print("my class method1")
    def method2(self,string):
        print("my class method2"+ string)
class anotherclass(myclass):
    def method1(self):
        myclass .method1(self)
        print("another class method")
    def method2(self,string):
        myclass.method2(self,string)
        print("another class method2")

def main():
    c=myclass()
    c.method1()
    c.method2("hi iam luna")
    c2=anotherclass()
    c2.method1()
    c2.method2("hi")
main()

