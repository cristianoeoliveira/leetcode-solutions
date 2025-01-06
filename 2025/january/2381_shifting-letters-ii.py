# 2381. Shifting Letters II
# You are given a string s of lowercase English letters and a 2D integer array shifts where shifts[i] = [starti, endi, directioni]. For every i, shift the characters in s from the index starti to the index endi (inclusive) forward if directioni = 1, or shift the characters backward if directioni = 0.
# Shifting a character forward means replacing it with the next letter in the alphabet (wrapping around so that 'z' becomes 'a'). Similarly, shifting a character backward means replacing it with the previous letter in the alphabet (wrapping around so that 'a' becomes 'z').
# Return the final string after all such shifts to s are applied.

class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        diff = [0] * (n + 1)

        for start, end, direction in shifts:
            if direction == 1:
                diff[start] += 1 
                diff[end + 1] -= 1 
            else:
                diff[start] -= 1 
                diff[end + 1] += 1

        shift = 0
        shifts_cumulative = [0] * n
        for i in range(n):
            shift += diff[i]  
            shifts_cumulative[i] = shift

        result = []
        for i in range(n):
            new_char = chr((ord(s[i]) - ord('a') + shifts_cumulative[i]) % 26 + ord('a'))
            result.append(new_char)

        return ''.join(result)
