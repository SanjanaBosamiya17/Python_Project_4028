# Write a program to make use of inner class

class Outer:
    def __init__(self):
        print("Outer class created")

    class Inner:
        def display(self):
            print("This is inner class")


o = Outer()
i = o.Inner()
i.display()
