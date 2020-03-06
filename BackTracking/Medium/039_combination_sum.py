from copy import deepcopy


class Solution:
    def combinationSum(self, candidates, target):
        self.results = []
        self.backtracking(candidates, target, 0, [])
        return self.results

    def backtracking(self, candidates, target, start, solution):
        if target < 0:
            return
        # print('target, ', target)
        if target == 0:
            # print('0,', solution)
            self.results.append(deepcopy(solution))
            # print('self.results,', self.results)
            return

        for i in range(start, len(candidates)):
            solution.append(candidates[i])
            self.backtracking(candidates, target - candidates[i], i, solution)
            solution.pop()


c = [2, 3, 6, 7]
t = 7
s = Solution()
print(s.combinationSum(c, t))
