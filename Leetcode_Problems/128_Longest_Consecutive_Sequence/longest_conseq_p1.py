class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if nums == []: return 0
        nums = sorted(set(nums))
        print(nums)
        max_len = 0
        c = 0
        for i,n in enumerate(nums):
            if i==len(nums)-1:break
            if nums[i+1]== n + 1: 
                c+=1
                    
            else:
                if max_len<c:
                    max_len = c
                c = 0

        if max_len<c:
            max_len = c

        return max_len + 1
    
a = Solution()
print(a.longestConsecutive([0,3,7,2,5,8,4,6,0,1]))
