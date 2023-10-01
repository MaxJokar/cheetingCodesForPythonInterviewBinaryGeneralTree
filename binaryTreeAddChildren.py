class  Binary_tree:
  def __init__(self, data) -> None: 
      self.data = data 
      self.left = None
      self.right = None   
   
      
  def add_child(self, data):
      if  type(data)!= Binary_tree: # To see if its a number or a data
        data = Binary_tree(data)
      if self.left is None:
        self.left = data
      elif self.right is None:
        self.right = data
      else:
        # print("No more child can be added  ")
        self.left.add_child(data)
        
      
      
      
root = Binary_tree(9)
print(root.data)
root.add_child(3)
root.add_child(4)
# root.add_child(5) gives our above Error 
root.add_child(5) 
print(root.left.data)
print(root.right.data)
print(root.left.left.data)