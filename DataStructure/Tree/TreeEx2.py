class treenode:
    def __init__(self,data):
        self.data = data 
        self.children = []
        self.parent = None 

    def addchild(self,child):
        self.children.append(child)  
        
    def printTree(self,level):
        if level:
            print(" "*(level*4),"|---",self.data,sep="")
        else:
            print(self.data)
        for child in self.children:
            child.printTree(level+1)

    def printTreeLevel(self,level,levelneed):
        if level>levelneed:
            return
        if level:
            print(" "*(level*4),"|---",self.data,sep="")
        else:
            print(self.data)
        for child in self.children:
            child.printTreeLevel(level+1,levelneed)

def createplace():
    Global = treenode("Global")
    
    india = treenode("India")
    gujarat = treenode("Guajarat")
    gujarat.addchild(treenode("Ahmedabad"))
    gujarat.addchild(treenode("Baroda"))
    karnataka = treenode("Karnataka")
    karnataka.addchild(treenode("Bangaluru"))
    karnataka.addchild(treenode("Mysore"))
    india.addchild(gujarat)
    india.addchild(karnataka)
    
    usa = treenode("USA")
    newjersey = treenode("New Jersey")
    newjersey.addchild(treenode("Princeton"))
    newjersey.addchild(treenode("Trenton"))
    california = treenode("California")
    california.addchild(treenode("San Francisco"))
    california.addchild(treenode("Mountain View"))
    california.addchild(treenode("Palo Alto"))
    usa.addchild(newjersey)
    usa.addchild(california)
    
    Global.addchild(india)
    Global.addchild(usa)
    
    return Global 

if __name__ == "__main__":
    print("...............Running tree problem 2..........")
    globalstates = createplace()
    print("\n\n\n")
    globalstates.printTree(0)
    print("\n\n\n")
    globalstates.printTreeLevel(0,0)
    print("\n\n\n")
    globalstates.printTreeLevel(0,1)
    print("\n\n\n")
    globalstates.printTreeLevel(0,2)
    print("\n\n\n")
    globalstates.printTreeLevel(0,3)
    print("\n\n\n")