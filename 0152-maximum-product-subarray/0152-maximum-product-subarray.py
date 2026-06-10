from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        pre, post, ans = 1, 1, float('-inf')
        n = len(nums)
        
        for i in range(n):
            # If the product becomes 0, reset it to 1
            pre = nums[i] if pre == 0 else pre * nums[i]
            post = nums[n - i - 1] if post == 0 else post * nums[n - i - 1]
            
            ans = max(pre, post, ans)
            
        return ans