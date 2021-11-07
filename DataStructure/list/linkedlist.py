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
         
if __name__ == "__main__":
    print("Started....")
    ll = linkedlist()
    ll.insert_into_head(30)
    ll.insert_into_head(40)
    ll.insert_into_head(50)
    ll.insert_into_head(60)        
    ll.insert_into_tail(30)
    ll.insert_into_tail(40)
    ll.insert_into_tail(50)
    ll.insert_into_tail(1000)
    
    ll.insert_into_position(5,23)
    ll.insert_into_position(3,23)
    ll.insert_into_position(5,23)
    ll.insert_into_position(7,23)
    ll.print()
    
    ll.deleteHead()
    ll.print()

    ll.deletePos(5)
    ll.print()
    ll.deletePos(9)
    ll.print()
    
    print(ll.Head())
    print(ll.Tail())
    print(ll.Index(999))
    print(ll.Of(999)) 