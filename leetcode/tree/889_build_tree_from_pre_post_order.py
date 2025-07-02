# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        """
        Tree looks like {N (L....) (R....)}
                        {(....L) (....R) N}
        """

        if not preorder:
            return None

        root = TreeNode(preorder[0])
        if len(preorder) ==1 :
            return root 

        leftNode = preorder[1]
        leftIndex = postorder.index(leftNode)

        leftPreOrder = preorder[1:leftIndex+2]
        rightPreOrder = preorder[leftIndex+2:]

        leftPostOrder = postorder[:leftIndex+1]
        rightPostOrder = postorder[leftIndex+1:-1]

        root.left = self.constructFromPrePost(leftPreOrder, leftPostOrder)
        root.right = self.constructFromPrePost(rightPreOrder, rightPostOrder)

        return root
