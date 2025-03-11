class myClass:
    __priveateVar = 27;
    def __priveMeth(self):
        print("I'm inside class myClass")

    def hello(self):
            print("Private Variable value: ",myClass.__privateVar)

foo = myClass()
foo.hello()
foo.__privMeth


 