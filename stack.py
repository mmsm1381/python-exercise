
from typing import Optional


class node :

    def __init__(self,data) -> None:
        self.past = None # under in layer
        self.data = data 


class stack : 

    def __init__(self) -> None:
        self.tob : Optional[node] = None

#add on tob
    def push(self,node:node)->None:
        if not self.isfull():
            if self.tob == None:
                self.tob = node
            else :
                node.past = self.tob
                self.tob = node
        else :
            raise Exception("stack is full")

#check if the node is in stack or not 
    def isin(self,node:node)->bool:
        temp = self.tob
        while temp:
            if temp == node:
                return True
            else :
                temp = temp.past
        return False
#remove a node from tob of stack
    def pop(self):
        if not self.isempty():
            self.tob = self.tob.past
        else : 
            raise Exception("can't pop from empty stacl")

#checks whether a stack is at maximum capacity 
    def isfull(self)->bool:
        temp = self.tob
        count = 0
        while temp:
            count+=1
            temp = temp.past
        if count>=100:
            return True
        else: 
            return False

#checks whether a stack is empty
    def isempty(self)->bool:
        if self.tob == None:
            return True
        else : 
            return False
        