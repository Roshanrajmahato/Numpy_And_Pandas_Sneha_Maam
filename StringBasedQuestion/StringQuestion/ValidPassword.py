"""
Source:

1. Code & Debug (Concept + Explanation)
   https://www.geeksforgeeks.org/python/password-validation-in-python/

2. Video Reference (Similar Logic)
   (Add if available)

Code:
https://www.geeksforgeeks.org/python/password-validation-in-python/

Problem Link:
https://www.geeksforgeeks.org/python/password-validation-in-python/

Password Validation in Python

A valid password must:
- Have at least one number
- Have at least one uppercase letter
- Have at least one lowercase letter
- Have at least one special character ($, @, #, %)
- Be between 6 and 20 characters in length

Example:
Input:  "Geek12#"
Output: Valid

Input:  "asd123"
Output: Invalid
"""

# ------------------------------------------------------
# Brute Force → Optimal Solution
# ------------------------------------------------------

import re

class Solution:

    # ------------------------------------------------------
    # 1. Method 1 (Using Regex)
    # Approach:
    # - Use a single regular expression pattern.
    # - Positive lookaheads ensure:
    #     ✔ at least one lowercase
    #     ✔ at least one uppercase
    #     ✔ at least one digit
    #     ✔ at least one special character
    # - Final part ensures length between 6 and 20.
    #
    # Why it works:
    # - Regex checks all constraints in one scan.
    #
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    # ------------------------------------------------------
    def validateRegex(self, password: str) -> bool:
        pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$#%])[A-Za-z\d@$#%]{6,20}$"
        return bool(re.search(pattern, password))


    # ------------------------------------------------------
    # 2. Method 2 (ASCII + Single Loop)
    # Approach:
    # - First check length constraint.
    # - Traverse password only once.
    # - Use ASCII ranges:
    #     48-57  → digits
    #     65-90  → uppercase
    #     97-122 → lowercase
    # - Check special symbols using membership test.
    # - Maintain boolean flags.
    #
    # Why it works:
    # - Single pass ensures all constraints checked efficiently.
    #
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    # ------------------------------------------------------
    def validateASCII(self, password: str) -> bool:
        if len(password) < 6 or len(password) > 20:
            return False

        has_digit = has_upper = has_lower = has_symbol = False
        special_symbols = ['$', '@', '#', '%']

        for char in password:
            if 48 <= ord(char) <= 57:
                has_digit = True
            elif 65 <= ord(char) <= 90:
                has_upper = True
            elif 97 <= ord(char) <= 122:
                has_lower = True
            elif char in special_symbols:
                has_symbol = True

        return has_digit and has_upper and has_lower and has_symbol


    # ------------------------------------------------------
    # 3. Method 3 (Naive - Built-in Functions)
    # Approach:
    # - Check length first.
    # - Use Python built-in functions:
    #     isdigit() → digit check
    #     isupper() → uppercase check
    #     islower() → lowercase check
    # - Use any() to scan password separately for each rule.
    #
    # Why it works:
    # - Built-in functions are optimized and readable.
    # - Slightly less efficient due to multiple scans.
    #
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    # ------------------------------------------------------
    def validateNaive(self, password: str) -> bool:
        if len(password) < 6 or len(password) > 20:
            return False

        special_symbols = ['$', '@', '#', '%']

        has_digit = any(ch.isdigit() for ch in password)
        has_upper = any(ch.isupper() for ch in password)
        has_lower = any(ch.islower() for ch in password)
        has_symbol = any(ch in special_symbols for ch in password)

        return has_digit and has_upper and has_lower and has_symbol


# ------------------------------------------------------
# Driver Code
# ------------------------------------------------------
if __name__ == "__main__":
    password = "Geek12@"
    ob = Solution()

    print("Regex Method:", ob.validateRegex(password))
    print("ASCII Method:", ob.validateASCII(password))
    print("Naive Method:", ob.validateNaive(password))