class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans=dict()
        for i,k in enumerate(nums):
            a=target-k
            if a in ans:
                return [ans[a],i]
            else :
                ans[k]=i
        return 0
