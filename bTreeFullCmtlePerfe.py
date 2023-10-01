class  Binary_tree:
  def __init__(self, data) -> None: 
      self.data = data # our node / root : were filling a node 
      self.left = None
      self.right = None   
   
      
  def add_child(self, data):
      if  type(data)!= Binary_tree: # To see if its a number or a data:
        data = Binary_tree(data)  # means  root 
      if self.left is None:
        self.left = data
      elif self.right is None:
        self.right = data
      else:
        # print("No more child can be added  ")
        self.left.add_child(data)
        
# To see if its full, complete or perfect 
def isstric(root):
  if root is None:
    return True
  if root.left == None and root.right == None:  # == is used to compare 2 variables
    return True
  if root.left is not  None and root.right is not None:
    return isstric(root.left) and isstric(root.right)
  return False

# To see if  a  Tree is complete we should count the child of each node 
def countNodes(root):
  if root is None: # value to the object is used by   is 
    return 0
  return (1+countNodes(root.left) + countNodes(root.right))

# To check if our tree is complete Tree or not 
# index : each level/height 
def iscompelete(root, index, number_nodes):
  if root is None:
    return True
  if index>=number_nodes:
    return False
  return(iscompelete(root.left, 2*index+1, number_nodes) and iscompelete(root.right, 2*index+2,number_nodes))    
        
root = Binary_tree(9)
# print(root.data)
root.add_child(3)
root.add_child(4)
# root.right.add_child(8)
# root.add_child(5) gives our above Error 
root.add_child(5) 
# root.add_child(8) 
root.right.add_child(52) 
print(root.left.data)
# print(root.right.data)
# print(root.left.left.data)
print("isstrict is :",isstric(root)) # flase



node_count = countNodes(root)
index =0
if iscompelete(root, index, node_count):
  print("complete Binary")
else:
  print("Not complete binary")
  
  
