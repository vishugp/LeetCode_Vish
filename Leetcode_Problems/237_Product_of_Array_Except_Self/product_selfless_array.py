class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        prod = 1
        zero = 0
        for n in nums: 
            if n==0: 
                zero+=1
                if zero>1: break
                continue
            prod = prod * n

        if zero>1:
           return [0 for _ in nums]
        elif zero==1:
            return [prod//1 if n==0 else 0 for n in nums]
        else:
           return [prod//n for n in nums]
    

a = Solution()
print(a.productExceptSelf([1,2,3,4,0]))
           