#question7

class Vector:
    def __init__(self,l):
        self.l = l

    def __len__(self):
        return len(self.l)

v1 = Vector([0.9,6,7,8])
print(len(v1))

