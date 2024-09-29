class qq:
    
    def __init__(self) -> None:
        self.a = 10
        self.b = 100
        
        
    def test0(self):
        self.a = 20
        return 200    
    
    
    def test1(self):
        print(self.a)
        print(self.b)
        self.b = self.test0()
        print(self.a)
        print(self.b)



qq1 = qq()

qq1.test1()