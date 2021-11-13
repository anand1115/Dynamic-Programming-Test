class Solution:
    def maxAverage(self, root):
        if not root or not root.components:
            return None
        self.res = [float('-inf'), root]
        self.dfs(root)

        return self.res[1]

    def dfs(self, root):
        if not root.components:
            return [root.value, 1]
        
        cur_val, cur_count = root.value, 1

        for node in root.components:
            child_val, child_count = self.dfs(node)
            cur_val += child_val
            cur_count += child_count

        cur_average = cur_val / float(cur_count)

        if cur_average > self.res[0]:
            self.res = [cur_average, root]

        return [cur_val, cur_count]


solution=Solution()
print(solution.maxAverage(rootComponent).val)

