class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        path = []
        def bt(index):
            if sum(path) == target:
                res.append(path.copy())
                return
            if sum(path) > target:
                return
            for i in range(index, len(candidates)):
                path.append(candidates[i])
                bt(i)
                path.pop()
        bt(0)
        return res