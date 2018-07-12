class strand:
    
    def __init__(self,comp,succ=None,pred=None,name="strand"):
        self.name=name
        self.comp=comp
        self.succ=succ
        self.pred=pred
        
    def set_succ(self,succ): #set the successor of this strand to be the strand succ
        self.succ=succ
        
    def get_succ(self): #return the successor of this strand
        return(self.succ)
        
    def set_pred(self,pred): #set the predecessor of this strand to be the strand succ
        self.pred=pred
        
    def get_pred(self): #return the successor of this strand
        return(self.pred)
    
    def set_component(self,comp): #set the component to which this strand belongs to be the component comp
        self.comp=comp
    
    def get_component(self): #return the component to which this strand belongs
        return(self.comp)
