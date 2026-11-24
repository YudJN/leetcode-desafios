# 104. Maximum Depth of Binary Tree (Profundidade Máxima da Árvore Binária)
# https://leetcode.com/problems/maximum-depth-of-binary-tree/
#
# Definition for a binary tree node (fornecida pelo LeetCode).
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        # Caso base: um nó vazio (None) não tem nenhum nó no caminho.
        if root is None:
            return 0

        # Pergunto aos dois filhos: "qual a profundidade da árvore que começa em você?"
        E = self.maxDepth(root.left)   # resposta do lado esquerdo
        R = self.maxDepth(root.right)  # resposta do lado direito

        # Fico com o maior dos dois lados e somo 1 (o próprio nó).
        return max(E, R) + 1
