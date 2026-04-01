"""
Source:

1. Official LeetCode Problem Description
   https://leetcode.com/problems/string-compression/description/

2. Video Reference (Similar Logic)
   https://youtu.be/D7y8W8X0ZW0

Code Explanation:
https://leetcode.com/problems/string-compression/

Problem Link:
https://leetcode.com/problems/string-compression/

String Compression

Given an array of characters chars, compress it using the following algorithm:

Begin with an empty string s. For each group of consecutive repeating characters in chars:
- If the group length is 1, append the character.
- Else append character + group length

You must modify the input array *in-place* with O(1) extra space
and return the new length of the array after compression.

Example:
Input: chars = ["a","a","b","b","c","c","c"]
Output: 6
Explanation: After modification: ["a","2","b","2","c","3"]

Example:
Input: chars = ["a"]
Output: 1
Explanation: ["a"]
"""

# ------------------------------------------------------
# Brute Force → Optimal Solution
# ------------------------------------------------------

class Solution:

    # ------------------------------------------------------
    # 1. Brute Force (Use Extra List & Then Write Back)
    # Approach:
    # - Track consecutive characters with a pointer.
    # - Build a new list with compressed string.
    # - Overwrite original array with new list.
    #
    # Why it works:
    # - Simulates compression but uses extra space.
    #
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    # ------------------------------------------------------
    def compressBrute(self, chars):
        compressed = []
        i = 0

        while i < len(chars):
            char = chars[i]
            count = 1
            while i + 1 < len(chars) and chars[i+1] == char:
                i += 1
                count += 1

            compressed.append(char)
            if count > 1:
                for digit in str(count):
                    compressed.append(digit)

            i += 1

        # Overwrite original
        for idx in range(len(compressed)):
            chars[idx] = compressed[idx]

        return len(compressed)


    # ------------------------------------------------------
    # 2. Better Solution (Two Pointers In-Place)
    # Approach:
    # - Use two pointers:
    #     read_ptr  → scan original array
    #     write_ptr → write compressed values
    # - Count repeated chars and write char + count.
    #
    # Why it works:
    # - Updates array *in-place* without extra list.
    #
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    # ------------------------------------------------------
    def compressBetter(self, chars):
        write = 0
        read = 0

        while read < len(chars):
            char = chars[read]
            count = 0

            # Count group length
            while read < len(chars) and chars[read] == char:
                read += 1
                count += 1

            # Write character
            chars[write] = char
            write += 1

            # Write count digits if >1
            if count > 1:
                for c in str(count):
                    chars[write] = c
                    write += 1

        return write


    # ------------------------------------------------------
    # 3. Optimal Solution (Same as Better)
    # Approach:
    # - This problem's optimal is same as better.
    #
    # Why it works:
    # - No extra optimization available due to in-place requirement.
    #
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    # ------------------------------------------------------
    def compressOptimal(self, chars):
        return self.compressBetter(chars)


# ------------------------------------------------------
# Driver Code
# ------------------------------------------------------
if __name__ == "__main__":
    chars1 = ["a","a","b","b","c","c","c"]
    chars2 = ["a"]
    ob = Solution()

    print("Brute Force:", ob.compressBrute(chars1.copy()), chars1)
    print("Better Solution:", ob.compressBetter(chars1.copy()), chars1)
    print("Optimal Solution:", ob.compressOptimal(chars2.copy()), chars2)