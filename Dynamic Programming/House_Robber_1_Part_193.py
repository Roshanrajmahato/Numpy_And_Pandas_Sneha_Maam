"""

Source:

Code and Debug https://youtu.be/eyRPBmmUAc4?si=W83VhPdmxvS5zMu_

Code:

https://codeanddebug.in/blog/house-robber/

House Robber II | Leetcode 213 | All 4 Solutions
------------------------------------------------
Problem Link:

https://leetcode.com/problems/house-robber-ii/

You are a professional robber planning to rob houses arranged in a circle.  
Each house has some money; you cannot rob two adjacent houses (including first & last because of the circle).  
Return the maximum amount of money you can rob without alerting the police.

Example:
    nums = [2,3,2] → Output: 3
    nums = [1,2,3,1] → Output: 4

Constraints:
    1 ≤ nums.length ≤ 100
    0 ≤ nums[i] ≤ 1000
"""

from typing import List

class Solution:

    # --------------------------------------------------
    # Recursive Approach (Brute Force)
    # --------------------------------------------------
    # TC: O(2^n)
    # SC: O(n) → recursion stack
    def rob_recursive(self, nums: List[int]) -> int:
        def solve(index: int, arr: List[int]) -> int:
            if index == 0:
                return arr[0]
            if index < 0:
                return 0
            pick = arr[index] + solve(index - 2, arr)
            not_pick = solve(index - 1, arr)
            return max(pick, not_pick)

        n = len(nums)
        if n == 1:
            return nums[0]
        # Since houses are circular, exclude first and last house separately
        return max(solve(n - 2, nums[1:]), solve(n - 2, nums[:-1]))

    # --------------------------------------------------
    # Memoization Approach (Top-Down DP)
    # --------------------------------------------------
    # TC: O(n)
    # SC: O(n) (recursion + dp array)
    def rob_memo(self, nums: List[int]) -> int:
        def solve(index: int, arr: List[int], dp: List[int]) -> int:
            if index == 0:
                return arr[0]
            if index < 0:
                return 0
            if dp[index] != -1:
                return dp[index]
            pick = arr[index] + solve(index - 2, arr, dp)
            not_pick = solve(index - 1, arr, dp)
            dp[index] = max(pick, not_pick)
            return dp[index]

        def helper(arr: List[int]) -> int:
            n = len(arr)
            dp = [-1] * n
            return solve(n - 1, arr, dp)

        n = len(nums)
        if n == 1:
            return nums[0]
        return max(helper(nums[1:]), helper(nums[:-1]))

    # --------------------------------------------------
    # Tabulation Approach (Bottom-Up DP)
    # --------------------------------------------------
    # TC: O(n)
    # SC: O(n)
    def rob_tabulation(self, nums: List[int]) -> int:
        def solve(arr: List[int]) -> int:
            n = len(arr)
            dp = [0] * n
            dp[0] = arr[0]
            for i in range(1, n):
                pick = arr[i]
                if i > 1:
                    pick += dp[i - 2]
                not_pick = dp[i - 1]
                dp[i] = max(pick, not_pick)
            return dp[n - 1]

        n = len(nums)
        if n == 1:
            return nums[0]
        return max(solve(nums[1:]), solve(nums[:-1]))

    # --------------------------------------------------
    # Tabulation (Space Optimization) Approach (Optimal)
    # --------------------------------------------------
    # TC: O(n)
    # SC: O(1)
    def rob_space_optimized(self, nums: List[int]) -> int:
        def solve(arr: List[int]) -> int:
            prev = arr[0]
            prev2 = 0
            for i in range(1, len(arr)):
                pick = arr[i]
                if i > 1:
                    pick += prev2
                not_pick = prev
                curr = max(pick, not_pick)
                prev2 = prev
                prev = curr
            return prev

        n = len(nums)
        if n == 1:
            return nums[0]
        return max(solve(nums[1:]), solve(nums[:-1]))


# --------------------------------------------------
# Example Usage / Driver Code
# --------------------------------------------------
if __name__ == "__main__":
    arr1 = [2, 3, 2]
    obj = Solution()

    print("Recursive:", obj.rob_recursive(arr1))          # Output: 3
    print("Memoization:", obj.rob_memo(arr1))             # Output: 3
    print("Tabulation:", obj.rob_tabulation(arr1))         # Output: 3
    print("Space Optimized:", obj.rob_space_optimized(arr1))  # Output: 3

    
