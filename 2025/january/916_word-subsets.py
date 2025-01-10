# 916. Word Subsets
# You are given two string arrays words1 and words2.
# A string b is a subset of string a if every letter in b occurs in a including multiplicity.
# For example, "wrr" is a subset of "warrior" but is not a subset of "world".
# A string a from words1 is universal if for every string b in words2, b is a subset of a.
# Return an array of all the universal strings in words1. You may return the answer in any order.

class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        max_count = Counter()
        for word in words2:
            word_count = Counter(word)
            for char, count in word_count.items():
                max_count[char] = max(max_count[char], count)

        result = []
        for word in words1:
            word_count = Counter(word)
            if all(word_count[char] >= max_count[char] for char in max_count):
                result.append(word)

        return result