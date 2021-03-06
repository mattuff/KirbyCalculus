from kirbyClass import *
from crossingClass import *
from joinClass import *
from componentClass import *

class strand:
    
    def __init__(self,component,pred=None,succ=None,pred_con=None,succ_con=None,i=None):
        self.name=i
        self.component=component
        self.pred=pred
        self.succ=succ
        self.pred_con=pred_con
        self.succ_con=succ_con
        
    def __str__(self): #check if this helps
        return(str(self.name))

    def set_name(i):
        self.name=i
        
    def set_succ(self,succ): #set the successor of this strand to be the strand succ
        self.succ=succ
        
    def set_pred(self,pred): #set the predecessor of this strand to be the strand succ
        self.pred=pred

    def set_pred_con(self,pred_con): #set the successor of this strand to be the strand succ
        self.pred_con=pred_con

    def set_succ_con(self,succ_con): #set the successor of this strand to be the strand succ
        self.succ_con=succ_con
        
    def set_component(self,component): #set the component to which this strand belongs to be the component comp
        self.component=component
    
    def get_component(self): #return the component to which this strand belongs
        return(self.component)
