"""
Source:

1. Code & Debug (Concept + Explanation)
   https://codeanddebug.in/blog/find-largest-element-array/

2. Video Reference (Similar Logic)
   https://youtu.be/oz15y1jeJRg

Code:
https://codeanddebug.in/blog/find-largest-element-array/

Problem Link:
https://www.geeksforgeeks.org/problems/largest-element-in-array4009/1
https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/   # similar logic

Largest Element in Array Problem (GeeksforGeeks)

You are given an array arr of size N.
Your task is to return the largest element present in the array.

Example:
Input: arr = [1, 8, 7, 56, 90]
Output: 90
"""

# ------------------------------------------------------
# Brute Force → Optimal Solution
# ------------------------------------------------------

class Solution:

    # ------------------------------------------------------
    # 1. Brute Force (Sorting) -> Time O(n log n), Space O(1)
    # ------------------------------------------------------
    def largestBrute(self, arr):
        arr.sort()
        return arr[-1]

    # ------------------------------------------------------
    # 2. Better Solution (Single Pass Iteration) -> Time O(n), Space O(1)
    # ------------------------------------------------------
    def largestBetter(self, arr):
        max_num = arr[0]
        
        for num in arr:
            if num > max_num:
                max_num = num
        
        return max_num

    # ------------------------------------------------------
    # 3. Optimal Solution (Same as Better) -> Time O(n), Space O(1)
    # ------------------------------------------------------
    def largestOptimal(self, arr):
        max_num = arr[0]
        
        for num in arr:
            if num > max_num:
                max_num = num
        
        return max_num


# ------------------------------------------------------
# Driver Code
# ------------------------------------------------------
if __name__ == "__main__":
    arr = [1, 8, 7, 56, 90]
    ob = Solution()

    print("Brute Force:", ob.largestBrute(arr.copy()))
    print("Better Solution:", ob.largestBetter(arr.copy()))
    print("Optimal Solution:", ob.largestOptimal(arr.copy()))
