class join:
    
    def __init__(self,strand0,strand1):
        self.strands=[strand0,strand1]

    def __getitem__(self,key):
        return(self.strands[key])

    def __contains__(self,item):
        return(item in self.strands)

    def setStrands(self,strand0,strand1):
        self.strands=[strand0,strand1]

    def getStrands(self):
        return(self.strands)
