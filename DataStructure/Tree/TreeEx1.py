class TreeNode:
    def __init__(self, name, designation):
        self.name = name 
        self.children = []
        self.designation = designation 
        self.parent = None  
        # self.level = level 
        
    def add_child(self, child):
        # child.parent = self
        self.children.append(child)
        
    def print_tree(self,need,level):
        if need=="name":
            if level!=0:
                print(" "*(level*4),"|___",self.name,sep="")
            else:
                print(self.name)
            if self.children:
                for child in self.children:
                    child.print_tree(need,level+1)
        elif need=="designation":
            if level!=0:
                print(" "*(level*4),"|___",self.designation,sep="")
            else:
                print(self.designation)
            if self.children:
                for child in self.children:
                    child.print_tree(need,level+1)
        elif need=="both":
            if level!=0:
                print(" "*(level*4),"|___",self.name," (",self.designation,")",sep="")
            else:
                print(self.name," (", self.designation,")",sep="")
            if self.children:
                for child in self.children:
                    child.print_tree(need,level+1)
        else:
            print("Give proper info... on what you need.")

        
def build_product_tree():
    root = TreeNode("NILPUL","CE0")
    
    CHINMAY = TreeNode("CHINMAY","CTO")
    VISHWA = TreeNode("VISHWA","INFRASTRUCTURE LEAD")
    VISHWA.add_child(TreeNode("DHAVAL","CLOUD MANAGER"))
    VISHWA.add_child(TreeNode("ABHIJIT", "APP MANAGER"))
    CHINMAY.add_child(VISHWA)
    CHINMAY.add_child(TreeNode("AAMIR","APPLICATION HEAD"))

    GELS = TreeNode("GELS","HR HEAD")
    GELS.add_child(TreeNode("PETER","RECRUITMENT MANAGER"))    
    GELS.add_child(TreeNode("WAQAS","POLICY MANAGER"))    
    
    root.add_child(CHINMAY)
    root.add_child(GELS)
    
    return root 

if __name__ == "__main__":
    print('..................Tree........................')
    Employee = build_product_tree()
    Employee.print_tree("designation",0)
    print("\n\n\n")
    print("\n\n\n")
    Employee.print_tree("name",0)
    print("\n\n\n")
    Employee.print_tree("both",0)
    print("\n\n\n")