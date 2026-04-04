class A:
    def show(self):
        print("I am class A")

class B(A):
    def show(self):
        print("I am class B")

class C(A):
    def show(self):
        print("I am class C")

class D(B, C):
    def show(self):
        print("I am class D")


d = D()
d.show()

print("\nMRO of class D:")
print(D.__mro__)

# or we can also use this
print("\nUsing mro() method:")
print(D.mro())
