"""
Source:

1. Article & Explanation
   https://www.geeksforgeeks.org/dsa/find-second-largest-element-array/

2. Video Reference (Similar Logic)
   https://youtu.be/37E9ckMDdTk

3. Additional Logic (Java Version Converted to Python)
   Based on the provided Java implementation using max replacement.

Code:
https://www.geeksforgeeks.org/dsa/find-second-largest-element-array/

Problem Link:
https://www.geeksforgeeks.org/dsa/find-second-largest-element-array/

Second Largest Element in an Array

Given an array of positive integers arr[] of size n, find
the second largest distinct element in the array.

Note:
If the second largest element does not exist, return -1.

Example:

Input: arr = [12, 35, 1, 10, 34, 1]
Output: 34

Input: arr = [10, 5, 10]
Output: 5

Input: arr = [10, 10, 10]
Output: -1
"""

# ------------------------------------------------------
# Brute Force → Optimal Solution
# ------------------------------------------------------

class Solution:

    # ------------------------------------------------------
    # 1. Brute Force (Sorting)
    #
    # Approach:
    # - Sort the array.
    # - Traverse from second last index.
    # - Return first element different from largest.
    #
    # Time Complexity: O(n log n)
    # Space Complexity: O(1)
    # ------------------------------------------------------
    def secondLargestBrute(self, arr):
        n = len(arr)

        arr.sort() 

        for i in range(n - 2, -1, -1):
            if arr[i] != arr[n - 1]:
                return arr[i]

        return -1


    # ------------------------------------------------------
    # 2. Better Solution (Two Pass Search)
    #
    # Approach:
    # - First pass → find largest element
    # - Second pass → find largest element
    #   excluding the largest
    #
    # Time Complexity: O(2n) → O(n)
    # Space Complexity: O(1)
    # ------------------------------------------------------
    def secondLargestBetter(self, arr):
        largest = -1
        secondLargest = -1

        for num in arr:
            if num > largest:
                largest = num

        for num in arr:
            if num > secondLargest and num != largest:
                secondLargest = num

        return secondLargest


    # ------------------------------------------------------
    # 3. Optimal Solution (One Pass Search)
    #
    # Approach:
    # - Maintain two variables:
    #     largest
    #     secondLargest
    #
    # Update rules:
    # If num > largest:
    #     secondLargest = largest
    #     largest = num
    #
    # If num < largest and num > secondLargest:
    #     update secondLargest
    #
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    # ------------------------------------------------------
    def secondLargestOptimal(self, arr):

        largest = -1
        secondLargest = -1

        for num in arr:

            if num > largest:
                secondLargest = largest
                largest = num

            elif num < largest and num > secondLargest:
                secondLargest = num

        return secondLargest


    # ------------------------------------------------------
    # 4. Alternative Approach (Replace Largest With -∞)
    #
    # Approach:
    # - Find the largest element.
    # - Replace all occurrences of largest with -infinity.
    # - Find the largest element again.
    #
    # Why it works:
    # Removing the largest value ensures the next maximum
    # becomes the second largest.
    #
    # Time Complexity: O(2n) → O(n)
    # Space Complexity: O(1)
    # ------------------------------------------------------
    def secondLargestReplaceMethod(self, arr):

        def findMax(a):
            mx = float('-inf')
            for num in a:
                if num > mx:
                    mx = num
            return mx

        mx = findMax(arr)

        for i in range(len(arr)):
            if arr[i] == mx:
                arr[i] = float('-inf')

        secondMax = findMax(arr)

        if secondMax == float('-inf'):
            return -1

        return secondMax


# ------------------------------------------------------
# Driver Code
# ------------------------------------------------------
if __name__ == "__main__":

    arr = [12, 35, 1, 10, 34, 1]

    ob = Solution()

    print("Brute Force:", ob.secondLargestBrute(arr.copy()))
    print("Better Solution:", ob.secondLargestBetter(arr.copy()))
    print("Optimal Solution:", ob.secondLargestOptimal(arr.copy()))
    print("Replace Largest Method:", ob.secondLargestReplaceMethod(arr.copy()))