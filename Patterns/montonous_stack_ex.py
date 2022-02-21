class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        stack = []
        for x in nums:
            n = TreeNode(x)
            print(n)
            while stack and x > stack[-1].val:
                n.left = stack.pop()
            if stack:
                stack[-1].right = n
            stack.append(n)
        return stack[0]
