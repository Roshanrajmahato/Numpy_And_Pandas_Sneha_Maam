"""

Source:

Code and Debug https://youtu.be/eyRPBmmUAc4?si=W83VhPdmxvS5zMu_

Code:

https://codeanddebug.in/blog/house-robber-ii/

House Robber II | Leetcode 213 | All 4 Solutions
------------------------------------------------
Problem Link: 

https://leetcode.com/problems/house-robber-ii/

You are a professional robber planning to rob houses along a street. 
Each house has a certain amount of money stashed. All houses are arranged in a circle, 
meaning the first house is the neighbor of the last. 
Adjacent houses have security systems that alert the police if both are robbed.

Given an integer array nums representing the money in each house, 
return the maximum amount of money you can rob tonight without alerting the police.

Example 1:
Input: nums = [2,3,2]
Output: 3

Example 2:
Input: nums = [1,2,3,1]
Output: 4

Constraints:
1 <= nums.length <= 100
0 <= nums[i] <= 1000
"""

from typing import List

class Solution:
    # ------------------------------------------------------------
    # Solution 1: Brute Force (Recursion)
    # ------------------------------------------------------------
    # Intuition:
    #   - At each step, you can either pick the current house or skip it.
    #   - Because houses are in a circle, you handle two cases separately:
    #       1. Rob from house 0 to n-2 (exclude last)
    #       2. Rob from house 1 to n-1 (exclude first)
    #
    # TC: O(2^n)
    # SC: O(n)  (recursion stack)
    # ------------------------------------------------------------
    def solve_recursive(self, index: int, nums: List[int]) -> int:
        # Base cases
        if index == 0:
            return nums[index]
        if index == -1:
            return 0

        # Option 1: Rob this house and skip the previous one
        pick = nums[index] + self.solve_recursive(index - 2, nums)
        # Option 2: Skip this house
        notpick = self.solve_recursive(index - 1, nums)

        return max(pick, notpick)

    def rob_recursive(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        # Scenario 1: Exclude last house
        ans1 = self.solve_recursive(n - 2, nums[0:n - 1])
        # Scenario 2: Exclude first house
        ans2 = self.solve_recursive(n - 2, nums[1:n])
        return max(ans1, ans2)

    # ------------------------------------------------------------
    # Solution 2: Memoization (Top-Down DP)
    # ------------------------------------------------------------
    # Intuition:
    #   - Avoid recalculating overlapping subproblems using dp array.
    #
    # TC: O(n)
    # SC: O(n) (dp array + recursion stack)
    # ------------------------------------------------------------
    def solve_memo(self, index: int, nums: List[int], dp: List[int]) -> int:
        if index == 0:
            return nums[index]
        if index == -1:
            return 0
        if dp[index] != -1:
            return dp[index]

        pick = nums[index] + self.solve_memo(index - 2, nums, dp)
        notpick = self.solve_memo(index - 1, nums, dp)

        dp[index] = max(pick, notpick)
        return dp[index]

    def rob_memo(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        # Case 1: Exclude last
        dp1 = [-1] * (n - 1)
        ans1 = self.solve_memo(n - 2, nums[0:n - 1], dp1)
        # Case 2: Exclude first
        dp2 = [-1] * (n - 1)
        ans2 = self.solve_memo(n - 2, nums[1:n], dp2)
        return max(ans1, ans2)

    # ------------------------------------------------------------
    # Solution 3: Tabulation (Bottom-Up DP)
    # ------------------------------------------------------------
    # Intuition:
    #   - Build DP array iteratively.
    #   - dp[i] = max(pick, not_pick)
    #
    # TC: O(n)
    # SC: O(n)
    # ------------------------------------------------------------
    def solve_tabulation(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [-1] * n
        dp[0] = nums[0]

        for index in range(1, n):
            if index > 1:
                pick = nums[index] + dp[index - 2]
            else:
                pick = nums[index]
            not_pick = dp[index - 1]
            dp[index] = max(pick, not_pick)

        return dp[n - 1]

    def rob_tabulation(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        ans1 = self.solve_tabulation(nums[0:n - 1])
        ans2 = self.solve_tabulation(nums[1:n])
        return max(ans1, ans2)

    # ------------------------------------------------------------
    # Solution 4: Space-Optimized Tabulation (Best Practice)
    # ------------------------------------------------------------
    # Intuition:
    #   - Only need the last two results → use two variables.
    #
    # TC: O(n)
    # SC: O(1)
    # ------------------------------------------------------------
    def solve_space_optimized(self, nums: List[int]) -> int:
        n = len(nums)
        prev = nums[0]   # DP[i - 1]
        prev2 = 0        # DP[i - 2]

        for index in range(1, n):
            if index > 1:
                pick = nums[index] + prev2
            else:
                pick = nums[index]
            not_pick = prev
            curr = max(pick, not_pick)
            prev2 = prev
            prev = curr

        return prev

    def rob_space_optimized(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        ans1 = self.solve_space_optimized(nums[0:n - 1])
        ans2 = self.solve_space_optimized(nums[1:n])
        return max(ans1, ans2)


# ------------------------------------------------------------
# Driver Code / Example Usage
# ------------------------------------------------------------
if __name__ == "__main__":
    obj = Solution()

    nums1 = [2, 3, 2]
    
    print("Recursive:", obj.rob_recursive(nums1))
    print("Memoization:", obj.rob_memo(nums1))
    print("Tabulation:", obj.rob_tabulation(nums1))
    print("Space Optimized:", obj.rob_space_optimized(nums1))

  
