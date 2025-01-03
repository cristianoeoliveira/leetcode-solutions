# 2559. Count Vowel Strings in Ranges
# You are given a 0-indexed array of strings words and a 2D array of integers queries.
# Each query queries[i] = [li, ri] asks us to find the number of strings present in the range li to ri (both inclusive) of words that start and end with a vowel.
# Return an array ans of size queries.length, where ans[i] is the answer to the ith query.
# Note that the vowel letters are 'a', 'e', 'i', 'o', and 'u'.

class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = set('aeiou')
        # Step 1: Preprocess the words array to create is_vowel_word
        is_vowel_word = []
        for word in words:
            if word[0] in vowels and word[-1] in vowels:
                is_vowel_word.append(1)
            else:
                is_vowel_word.append(0)
        
        # Step 2: Create the prefix sum array
        prefix = [0] * len(is_vowel_word)
        prefix[0] = is_vowel_word[0]
        for i in range(1, len(is_vowel_word)):
            prefix[i] = prefix[i-1] + is_vowel_word[i]
        
        # Step 3: Answer the queries
        ans = []
        for li, ri in queries:
            if li == 0:
                ans.append(prefix[ri])
            else:
                ans.append(prefix[ri] - prefix[li-1])
        
        return ans