"""
 To calculate the height of Tree in General tree , its harder cuz we dont have 
 constant length
 
 2.To see if it is  a Binary Tree or  General Tree :
 we must see each node max has only 2 node
"""
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


    # we need to know the maximum length to determine its height
    # if it doesnt have any node look at max_height , add one and return 
    def height(self):
      if len(self.children) == 0: # if you dont have any chilren return 0
        return 0
      max_height = -1
      for child in self.children:
        max_height = max(max_height, child.height())
      return max_height+1
        
        
    # To see if it is  a Binary Tree or  General Tree 
    def isbinary(self):
      if len(self.children)>2:
        return False
      if len(self.children) == 0 : #means reached to a leaf
        return True
      for child in self.children:
        if not child.isbinary():
          return False
      return True    # if we have less than 2 
    
    
# # To see if its full, complete or perfect 
# def isstric(root):
#   if root is None:
#     return True
#   if root.left == None and root.right==None:
#     return True
#   if root.left is None and root.right is not None:
#     return isstric(root.left) and isstric(root.right)
#   return False

# def countNodes(root):
#   if root is None: 
#     return 0
#   return (1+countNodes(root.left) + countNodes(root.right))

# def iscompelete(root, index, number_nodes):
#   if root is None:
#     return True
#   if index>=number_nodes:
#     return(iscompelete(root.left, 2*index+1, number_nodes))


  
def create_tree():     
    root = Tree_node(100)
    # print(root.data)
    root.add_child(Tree_node(3))
    root.add_child(Tree_node(8))
    
    # root.add_child(5) gives our above Error 
    # To check if its binary or now we do following 
    root.children[0].add_child(Tree_node(1))
    root.children[0].add_child(Tree_node(200))
    root.children[0].add_child(Tree_node(500))
    root.children[0].children[0].add_child(Tree_node(20))
    # root.right.data

    # laptops = Tree_node("laptops")
    # root.add_child(laptops)   # means => add subgroup
    # laptops.add_child(Tree_node("Dell"))
    # laptops.add_child(Tree_node("samsung"))
    # laptops.add_child(Tree_node("Mac"))
    
    # televisions = Tree_node("televisions")
    # root.add_child(televisions)
    # televisions.add_child(Tree_node("Daaaa"))
    # televisions.add_child(Tree_node("sbbbb"))
    # televisions.add_child(Tree_node("tttt"))
    
    
    # phones = Tree_node("phones")  
    # root.add_child(phones)
    # phones.add_child(Tree_node("Iphone"))
    # phones.add_child(Tree_node("Huawei"))
    
    
    
    return root 
  
  
  
root = create_tree()
# print(root.height()) #2
print(root.print_tree()) #2 To see if its binary or not 
print(root.isbinary())
