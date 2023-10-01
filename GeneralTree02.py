from re import T


class  Tree_node:
    def __init__(self, data) -> None: 
        self.data = data # our node/root  Electronic 
        self.children = []
        self.parent = None   # Laptops,  tv  ,  phones 
        self.level = 1 # to make lavels in each height 
        
    def add_child(self, child):
        self.children.append(child)
        child.parent = self # everytie when a child is built it reference to its parent e.f laptops,tv,phone
        child.level = child.parent.level+1
     
    def print_tree(self):
        spaces = " spcs "*self.level
        prefix = spaces + " prfix " if self.parent else "|--"
        print(prefix,self.data)  # prints parents 
        for child in self.children:
            # print(child) prints  object 
            print(" chldlvl "*child.level, end= "")
            child.print_tree() # recursion 
     
     
     
        
def create_tree():     
    root = Tree_node("Electronics")
    
    laptops = Tree_node("laptops")
    root.add_child(laptops)   # means => add subgroup
    laptops.add_child(Tree_node("Dell"))
    laptops.add_child(Tree_node("samsung"))
    laptops.add_child(Tree_node("Mac"))
    
    televisions = Tree_node("televisions")
    root.add_child(televisions)
    televisions.add_child(Tree_node("Daaaa"))
    televisions.add_child(Tree_node("sbbbb"))
    televisions.add_child(Tree_node("tttt"))
    
    
    phones = Tree_node("phones")  
    root.add_child(phones)
    phones.add_child(Tree_node("Iphone"))
    phones.add_child(Tree_node("Huawei"))
    
    

    
    
  

    
    return root 
        
if __name__ == "__main__":
    root = create_tree()
    # print(root)
    root.print_tree() 
    # print("root level :",root.level)   # root level : 1
    # print("root children  :",root.children[0].level)  # root children  : 2
    # print("root children children :",root.children[0].children[0].level)  # root children  : 2
    # print("root level :",root.level)