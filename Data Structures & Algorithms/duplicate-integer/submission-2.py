class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n=[]
        for i in nums:
            if i in n:
                return True
            n.append(i)    
        else:
            return False
if __name__=="__main__":
    sol = Solution()
    print(sol.hasDuplicate([1,2,3,3])) 



                 