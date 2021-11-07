class TreeNode:
    def __init__(self, data):
        self.data = data 
        self.children = []
        self.parent = None  
        
    def add_child(self, child):
        # child.parent = self
        self.children.append(child)
        
    def print_tree(self,level):
        print(" "*(level*4),"|___",self.data,sep="")
        if self.children:
            for child in self.children:
                child.print_tree(level+1)

def build_product_tree():
    root = TreeNode("Electronics")
    
    laptop = TreeNode("Laptop")
    laptop.add_child(TreeNode("Mac"))
    laptop.add_child(TreeNode("Surface"))
    laptop.add_child(TreeNode("Thinkpad"))
    
    cellphone = TreeNode("Cell phone")
    cellphone.add_child(TreeNode("iPhone"))
    cellphone.add_child(TreeNode("Google Pixel"))
    cellphone.add_child(TreeNode("vivo"))
    
    tv = TreeNode("TV")
    tv.add_child(TreeNode("Samsung"))
    tv.add_child(TreeNode("LG"))
    
    root.add_child(laptop)
    root.add_child(cellphone)
    root.add_child(tv)
    
    return root 

if __name__ == "__main__":
    print('..................Tree........................')
    Electronics_root = build_product_tree()
    print("\n\n\n")
    Electronics_root.print_tree(0)
    print("\n\n\n")
