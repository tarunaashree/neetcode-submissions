class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s=[]
        for i in range(len(nums)):
            for j in range(i):
                if nums[i]+nums[j]==target and i!=j :
                    s.append(j)
                    s.append(i)
        return s


        
        