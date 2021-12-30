
from typing import Optional


class node :

    def __init__(self,data) -> None:
        self.past : Optional[node] = None
        self.data = data 


class qeue : 

    def __init__(self) -> None:
        self.rear : Optional[node] = None
        self.front : Optional[node] = self.rear

#add a node 
    def push(self,node):
        if self.isempty():
            self.rear = node
        else :
            node.past = self.front
            self.front = node

#pop node from qeue
    def pop(self)-> node:
        if not self.isempty():
            temp1 = self.front.past
            temp = self.front
            while temp1:
                temp = temp.past
                temp1 = temp.past
            temp1.past = None
            self.rear = temp
            return temp
        else : 
            raise Exception("cant pop from empty list")


#check if the node is in qeue
    def isin(self,node)->bool:
        temp = self.front
        while temp:
            if temp == node:
                return True
            else :
                temp = temp.past
        return False

# check if qeue is empty
    def isempty(self):
        if not self.rear :
            return True
        else:
            False


    