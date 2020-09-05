# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Time: O(n), Space: O(n)
# Relevant Concepts: Inorder traversal, Merging sorted arrays, Binary search trees

# Since we know the two trees are binary search trees, every element in the left subtree of root
# will be < root.val and every element in right subtree of root will be > root.val

# An inorder traversal will return left, root, right in terms of the order of the nodes
# for every subtree. Inorder on both trees will then give us two sorted arrays of each tree

# We have two effective approaches from here: since we know the two arrays are sorted we
# can merge them (compare a arr1 pointer value against an arr2 pointer value) or we can collect
# all the values into a single array and then call 'sorted()' (or 'sort()' in Java) and return the
# result.

# IMPORTANT Note: Normally, calling a sort method would make the time complexity O(n log(n)), but
# in Python and Java they actually use a sorting method called 'timsort' which is O(n) given that
# the two arrays we are merging are sorted themselves--in this case, they are. 
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        nums = [] 
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            nums.append(root.val)
            inorder(root.right)
        inorder(root1)
        inorder(root2)
        return sorted(nums)
    
    # Merge method for two sorted arrays
    # def merge(arr1, arr2):
    #   res = []
    #   left, right = 0, 0
    #   while left < len(arr1) and right < len(arr2):
    #       if arr1[left] < arr2[right]:
    #           res.append(arr1[left])
    #           left += 1
    #       else:
    #           res.append(arr2[right])
    #           right += 1
    #   if left >= len(arr1) and right < len(arr2):
    #       res.extend(arr2[right:])
    #   elif left < len(arr1) and right >= len(arr2):
    #       res.extend(arr1[left:])
    #   return res
    #   
