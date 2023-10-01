from re import T


class  Tree_node:
    def __init__(self, data) -> None:
        self.data = data # our node
        self.children = []
        self.parent = None   
        
    def add_child(self, child):
        self.children.append(child)
        self.parent = self # everytie when a cild is built it reference to its parent 
        
        
        
if __name__ == "__main__":
    root = Tree_node("Electronics")
    
    laptops = Tree_node("laptops")

    
    televisions = Tree_node("televisions")

    
    
    phones = Tree_node("phones")

    
    root.add_child(laptops)   # means => add subgroup
    root.add_child(televisions)
    root.add_child(phones)
    
    # print(root.data)  # Electronics
    # print(laptops.data)  # laptops
    # print(root.children) # gives 3 objects 
    # print(root.children[0].data) # laptops  
    # print(root.children[1].parent.data) ???????????watch again video