# 1400. Construct K Palindrome Strings
# Given a string s and an integer k, return true if you can use all the characters in s to construct k palindrome strings or false otherwise.

class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if k > len(s):
            return False
        
        char_count = Counter(s)

        odd_count = sum(1 for count in char_count.values() if count % 2 != 0)

        return odd_count <= k
