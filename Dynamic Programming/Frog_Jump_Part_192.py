"""
Source:

1.Manvi_Maam (Concept + Dry Run) https://youtu.be/ueIlh_cmVOc?si=BjZj7b_6J_ldVcI-
2.Code and Debug https://youtu.be/oz15y1jeJRg?si=MfGZ6q6iKGft7Zov

Code:

https://codeanddebug.in/blog/frog-jump/

Problem Link:

https://www.geeksforgeeks.org/problems/geek-jump/1
https://leetcode.com/problems/frog-jump/

Frog Jump Problem (GeeksforGeeks)

There is a frog on the 1st step of an N stairs long staircase. 
The frog wants to reach the Nth stair. 

The frog can jump either 1 step or 2 steps at a time. 
A height Heightay is given, where height[i] is the height of the i-th stair.

Whenever the frog jumps from stair i to stair j, 
the energy lost is abs(height[i] - height[j]).

The task is to find the minimum total energy used by the frog to reach the Nth stair.

---------------------------------------------------
Example 1:
Input: height = [30, 10, 60, 10, 60, 50]
Output: 40
Explanation: 
- Jump from 1st to 2nd stair: cost = |30-10| = 20
- Jump from 2nd to 4th stair: cost = |10-10| = 0
- Jump from 4th to 6th stair: cost = |10-50| = 40
Total cost = 20 + 0 + 20 = 40

---------------------------------------------------
Constraints:
1 <= N <= 10^5
0 <= height[i] <= 10^4
---------------------------------------------------
"""

# ------------------------------------------------------
# 1. Recursive Approach (Brute Force) -> Exponential Time 
# ------------------------------------------------------
class Solution:

    # ------------------------------------------------------
    # 1. Recursive Approach (Brute Force) -> Exponential Time O(2^n) Space O(n)
    # ------------------------------------------------------
    def solveRecursive(self, height, index):
        if index == 0:
            return 0
        
        jump1 = self.solveRecursive(height, index - 1) + abs(height[index] - height[index - 1])
        
        
        if index > 1:
            jump2 = self.solveRecursive(height, index - 2) + abs(height[index] - height[index - 2])
        
        else:
            jump2 = float("inf")

        return min(jump1, jump2)

    # ------------------------------------------------------
    # 2. Memoization Approach (Top-Down DP) -> Time O(N) , Space O(N) Stack + O(N) dp 
    # ------------------------------------------------------
    def solveMemo(self, height, index, dp):
        if index == 0:
            return 0
        if dp[index] != -1:
            return dp[index]
        
        jump1 = self.solveMemo(height, index - 1, dp) + abs(height[index] - height[index - 1])
        
        if index > 1:
            jump2 = self.solveMemo(height, index - 2, dp) + abs(height[index] - height[index - 2])
        
        else:
            jump2 = float("inf")

        dp[index] = min(jump1, jump2)
        return dp[index]

    # ------------------------------------------------------
    # 3. Tabulation Approach (Bottom-Up DP) ->Time O(N) , Space O(N) dp only
    # ------------------------------------------------------
    def solveTabulation(self, height):
        n = len(height)
        dp = [0] * n
        dp[0] = 0
        
        for i in range(1, n):
            jump1 = dp[i - 1] + abs(height[i] - height[i - 1])
            
            if i > 1:
                jump2 = dp[i - 2] + abs(height[i] - height[i - 2])
            
            else:
                jump2 = float("inf")

            dp[i] = min(jump1, jump2)
        
        return dp[n - 1]

    # ------------------------------------------------------
    # 4. Tabulation (Space Optimization) -> O(N) Time, O(1) Space (Optimal)
    # ------------------------------------------------------
    def solveSpaceOptimized(self, height):
        n = len(height)
        prev = 0   # dp[i-1]
        prev2 = 0   # dp[i-2]
        
        for i in range(1, n):
            jump1 = prev + abs(height[i] - height[i - 1])
            
            if i > 1:
                jump2 = prev2 + abs(height[i] - height[i - 2])
            
            else:
                jump2 = float("inf")

            curr = min(jump1, jump2)
            prev2 = prev
            prev = curr
        
        return prev


# ------------------------------------------------------
# Driver Code
# ------------------------------------------------------
if __name__ == "__main__":
    Height = [30, 10, 60, 10, 60, 50]
    n = len(Height)
    ob = Solution()

    print("Recursive:", ob.solveRecursive(Height, n - 1))

    dp = [-1] * n
    print("Memoization:", ob.solveMemo(Height, n - 1, dp))

    print("Tabulation:", ob.solveTabulation(Height))

    print("Space Optimized:", ob.solveSpaceOptimized(Height))