"""
🧮 Problem: Add Digits

Given an integer `num`, repeatedly add all its digits until the result has only one digit.
Return that final single-digit result.

Examples:
---------
Input: num = 38
Output: 2
Explanation:
    38 --> 3 + 8 = 11
    11 --> 1 + 1 = 2
    Since 2 has only one digit, return it.

Input: num = 0
Output: 0

Constraints:
------------
- 0 <= num <= 2^31 - 1
"""

#Solution:

class Solution:
    def addDigits(self,num:int) -> int:
        return 0 if num==0 else 1+ (num-1)%9 