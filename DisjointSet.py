## Class for Disjoint Set

class DISJOINSET:
    def __init__(self,n):
        self.Par=[-1 for i in range(n)]
        self.NumberOfSets=n
    def Parent(self,p):
        if self.Par[p]==-1:
            return p
        self.Par[p]=self.Parent(self.Par[p])
        return self.Par[p]
    def Join(self,a,b):
        if self.Parent(a)!=self.Parent(b):
            self.Par[self.Parent(a)]=self.Parent(b)
            self.NumberOfSets-=1
    def NumOfSets(self):
        return self.NumberOfSets
