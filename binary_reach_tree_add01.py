"""
  binary search is a  Binary tree with rule inserting data in it 
  it has two types : with repeated/not repeated datas in it 
  in duplicated , the equal number goes to the right side of  Tree
  Design a  class of  Binary search , add a function to add
  nodes and child and use all in , pre post order 
  
  in this code we do not  apply duplicated numbers !
"""
  
class Binary_search_tree:
    def __init__(self, data) -> None: 
        self.data = data 
        self.left = None
        self.right = None   
   
    def add(self, val):
        if self.data == val:
            return
        elif self.data > val:
            if self.left == None:
                self.left = Binary_search_tree(val)
            else:
                self.left.add(val)

        else:
            if self.right == None:
                self.right = Binary_search_tree(val)
            else:
                self.right.add(val)
    
    # to return a  in order list [L-N-R]
    def inorder_traversal(self):
        elements = []
        if self.left:
            elements+=self.left.inorder_traversal()
        elements.append(self.data) # node
        
        if self.right:
            elements+=self.right.inorder_traversal()
        return elements
    # [N-L-R]
    def pre_traversal(self):
        elements = []
        elements.append(self.data) # node
        if self.left:
            elements += self.left.pre_traversal()
        if self.right:
            elements += self.right.pre_traversal()

        return elements
    # [L-R-N]
    def postorder_traversal(self):
        elements = []
        if self.left:
            elements += self.left.postorder_traversal()
        if self.right:
            elements += self.right.postorder_traversal()

        elements.append(self.data) # node
        return elements  
        
        
  
elements = [15,9,20,3,99,12,123]
root = Binary_search_tree(elements[0]) # instantiate the root by 5
for  i in elements[1:]:
    root.add(i)
    
print(root.data)
print(root.left.data)
# print(root.left.left.data)
# print(root.left.right.data)
# print(root.right.left.data)
# 15
# 9
# 5
# 10
# 5

print(root.inorder_traversal())
# 15
# 9
# [3, 9, 12, 15, 20, 99, 123]

print(root.pre_traversal())
print(root.postorder_traversal())
# 15, 9, 3, 12, 20, 99, 123]
# [3, 12, 9, 123, 99, 20, 15]
