# 1408. String Matching in an Array
# Given an array of string words, return all strings in words that is a substring of another word. You can return the answer in any order.
# A substring is a contiguous sequence of characters within a string

class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        result = []
        for i, word in enumerate(words):
            for j, other_word in enumerate(words):
                if i != j and word in other_word:
                    result.append(word)
                    break
        return result