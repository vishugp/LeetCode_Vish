class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:

        nums2 = [target-num for num in nums]
        print(nums,"\n",nums2)

        for i,num in enumerate(nums):
            if num in nums2:

                j = nums2.index(num)
                if i==j: continue
                return  sorted([i,j])
        

a = Solution()
print(a.twoSum([3,3],6))