class box:
    def __init__(self,x,y,z):
        self.length = x
        self.br = y
        self.ht = z

    def vol(self):
        v = self.length * self.br * self.ht
        return v

b1 = box(2,4,2)
v1 = b1.vol()
print(v1)