import math 

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class linkedlist:
    def __init__(self):
        self.head = None 
        self.len = 0
    
    def insert_into_head(self, data):
        self.len +=1
        newnode = Node(data)
        newnode.next = self.head
        self.head=newnode
    
    def insert_into_tail(self, data):
        self.len +=1
        newnode = Node(data)
        if self.head is None:
            self.head = newnode 
            return
        temp = self.head
        while temp.next is not None:
            temp = temp.next 
        temp.next = newnode       
    
    def print(self):
        temp = self.head
        while(temp):
            print(temp.data,end="->")
            temp=temp.next 
        print("None")
    
    def insert_into_position(self, pos, data):
        newnode = Node(data)
        cal = 0
        temp = self.head
        while(cal+1<pos):
            cal+=1
            temp=temp.next 
        newnode.next = temp.next 
        temp.next = newnode
        self.len += 1 
    
    def Head(self):
        if self.head is not None:
            return self.head.data
        return -1
    
    def Tail(self):
        if self.head is not None:
            temp = self.head 
            while(temp.next):
                temp = temp.next 
            return temp.data 
        return -1
    
    def Index(self,data):
        temp = self.head
        cal = 0
        while(temp is not None and temp.data!=data):
            cal+=1
            temp = temp.next 
        if temp is not None:
            return cal 
        return -1 
    
    def Of(self, pos):
        temp = self.head 
        cal = 0
        while(temp is not None and cal<pos):
            cal+=1
            temp = temp.next
        if temp is not None:
            return temp.data
        return -1        
    
    def deleteHead(self):
        if self.head is not None:
            self.head = self.head.next 
            self.len -= 1
    
    def deleteTail(self):
        if self.head is None:
            return 
        if self.head.next is None:
            self.head = None
            self.len -= 1
            return 
        temp = self.head 
        while(temp.next.next is not None):
            temp = temp.next 
        temp.next = None 
        self.len -= 1
    
    def deletePos(self,Pos):
        if self.len == 0:
            return
        temp = self.head
        cal = 0
        while(temp is not None and cal+1<Pos):
            cal+=1
            temp=temp.next
        if temp.next.next is not None:
            temp.next=temp.next.next 
        else:
            temp.next=None
        self.len -= 1
    
    def middleElement(self):
        cal=0
        temp = self.head
        while(temp and cal<math.floor(self.len/2)):
            cal += 1
            temp = temp.next 
        return temp.data
    

if __name__ == "__main__":
    ll = linkedlist()
    l = list(map(int, input().split()))
    for i in range(len(l)-1,-1,-1):
        ll.insert_into_head(l[i])
    print(ll.middleElement())
    
    
    
    