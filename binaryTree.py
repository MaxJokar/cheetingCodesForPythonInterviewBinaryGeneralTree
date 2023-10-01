class  Tree_node:
    def __init__(self, data) -> None: 
        self.data = data # our node/root  Electronic 
        self.children = []
        self.parent = None   # Laptops,  tv  ,  phones 
     
        
    def add_child(self, child):
        self.children.append(child)
        child.parent = self # everytie when a child is built it reference to its parent e.f laptops,tv,phone
        # child.level = child.parent.level+1
     
   # This is new function  :from this node count up to get to root
#    we get the root when its parent is None 
    def get_lvl(self):
        level = 0 
        p = self.parent
        while p : # while its parent is not None 
           level+=1 
           p = p.parent
        return level
       
   
    def print_tree(self):
        spaces = " "*self.get_lvl()
        prefix = spaces + "|--" if self.parent else "|--"
        print(prefix,self.data)  # prints parents 
        for child in self.children:
            # print(child) prints  object         
            child.print_tree() # recursion 
     
            
            
            
            
 
            
            
     
    def search_child(self, key):
        print("="*30)
        # print(self.data)
        # print(key)
        # print("true")
        # print("="*30)
        if self.data == key :
            return True
        for child in self.children:
            found = child.search_child(key) 
            if found:
                return True
        return False
     
     
        
def create_tree():     
    root = Tree_node(15)
    
   

    root.add_child(Tree_node(4))
    root.add_child(Tree_node(2))
    
    root.children[0].add_child(Tree_node(1))
    root.children[0].children[0].add_child(Tree_node(100))
  
     
    return root 
        
        
        
        
if __name__ == "__main__":
    root = create_tree()   
    # print(root.height())  # 3
    print(root.print_tree())