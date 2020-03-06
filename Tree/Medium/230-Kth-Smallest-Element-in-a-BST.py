# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:

        # faster
        stack = []

        while True:
            if root:  # 没有到叶子节点,找左子树
                stack.append(root)
                root = root.left
            elif stack:    # root为None,即遍历到叶子,到stack中找父节点
                root = stack.pop()
                k -= 1

                if k == 0:
                    return root.val
                root = root.right
            else:   # root和stack都为空,即遍历完成
                break

        # inorder traversal (iteratively)

        # stack = []
        # curr = root
        #
        # while True:
        #     while curr is not None:
        #         stack.append(curr)
        #         curr = curr.left
        #
        #     node = stack.pop()
        #     k -= 1
        #     if k == 0:
        #         return node.val
        #     curr = node.right

        # slowest
        # self._i = 0
        # self.ans = 0
        #
        # def dfs(root):
        #     if not root:
        #         return;
        #     dfs(root.left)
        #     self._i += 1
        #     if self._i == k:
        #         self.ans = root.val
        #         return;
        #     dfs(root.right)
        #
        # dfs(root)
        # return self.ans
