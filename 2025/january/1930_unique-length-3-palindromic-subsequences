# 1930. Unique Length-3 Palindromic Subsquences
# Given a string s, return the number of unique palindromes of length three that are a subsequence of s.
# Note that even if there are multiple ways to obtain the same subsequence, it is still only counted once.
# A palindrome is a string that reads the same forwards and backwards.
# A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        # Create arrays to track first and last occurrences of each character
        first = [-1] * 26
        last = [-1] * 26
        n = len(s)
        
        # Record the first and last occurrence of each character
        for i in range(n):
            idx = ord(s[i]) - ord('a')
            if first[idx] == -1:
                first[idx] = i
            last[idx] = i
        
        # Set to store unique palindromes
        unique_palindromes = set()
        
        # Iterate over all possible characters ('a' to 'z')
        for i in range(26):
            if first[i] != -1 and first[i] < last[i]:
                # Valid range for the character
                middle_chars = set(s[first[i] + 1:last[i]])
                # Form palindromes
                for mid in middle_chars:
                    unique_palindromes.add(chr(i + ord('a')) + mid + chr(i + ord('a')))
        
        # Return the count of unique palindromes
        return len(unique_palindromes)
