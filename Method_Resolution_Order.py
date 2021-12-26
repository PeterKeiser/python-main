

class A:
    def do_something(self):
        print("Method Defined in: A")

class B(A):
    def do_something(self):
        print("Method Defined in: B")
        super().do_something()

class C(A):
    def do_something(self):
        print("Method Defined in: C")   
        super().do_something()  
        
class D(B,C):
    def do_something(self):
        print("Method Defined in: D")
        super().do_something()

# print(D.__mro__)
# print(D.mro())
# help(D)
thing = D()
print(thing.do_something())

 

