# 3042. Count Prefix and Suffix Pairs I
# You are given a 0-indexed string array words.
# Let's define a boolean function isPrefixAndSuffix that takes two strings, str1 and str2:
# - isPrefixAndSuffix(str1, str2) returns true if str1 is both a prefix and a suffix of str2, and false otherwise.
# For example, isPrefixAndSuffix("aba", "ababa") is true because "aba" is a prefix of "ababa" and also a suffix, but isPrefixAndSuffix("abc", "abcd") is false.
# Return an integer denoting the number of index pairs (i, j) such that i < j, and isPrefixAndSuffix(words[i], words[j]) is true.

class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        def isPrefixAndSuffix(str1: str, str2: str) -> bool:
            """
            Check if str1 is both a prefix and a suffix of str2.
            """
            return str2.startswith(str1) and str2.endswith(str1)

        count = 0

        n = len(words)
        for i in range(n):
            for j in range(i + 1, n):
                if isPrefixAndSuffix(words[i], words[j]):
                    count += 1

        return count