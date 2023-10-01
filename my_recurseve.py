# def mrec(n):
#     if n ==0:
#         print("stop") 
#     else:
        
#         result =  mrec(n-1)
#         print(result)


# mrec(5)
# print(x)


"""
 it is a process in which a function calls itself directly or indirectly. 
"""


def tri_recursion(k):
  if(k>0):
    print(k)
    result = k+tri_recursion(k-1)
    print("hello")
    print("result :",result)
  else:
    result = 0
#   print(k)  
  return result

print("\n\nRecursion Example Results")
tri_recursion(2)







