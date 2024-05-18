class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:

        if nums==[]: return []

        numlen = len(nums)
        ans = [0]*numlen

        # zeros = []
        prod = 1

        for i in range(numlen):
            # if nums[i] == 0: zeros.append(i)
            # else: prod*=nums[i]

            # if len(zeros)>1: return [0]*numlen
            
            if i==0:
                ans[0] = nums[0]
            else:
                ans[i] = ans[i-1]*nums[i]

        # if len(zeros)==1:
        #     ans = [0] * numlen
        #     ans[zeros[0]] = prod
        #     return ans
            # print(ans)

        # print("\n")
        # prod = 1
        for i in range(numlen-1,0,-1):
            ans[i] = ans[i-1] * prod
            prod = prod * nums[i]

            # print(ans, prod)


        ans[0] = prod
        # print("\n")

        return ans
        
    


a = Solution()
print(a.productExceptSelf([1,2,3,4,0,5,6,6]))