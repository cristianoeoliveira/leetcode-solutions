# 2429. Minimize XOR
# Given two positive integers num1 and num2, find the positive integer x such that:
# x has the same number of set bits as num2, and
# The value x XOR num1 is minimal.
# Note that XOR is the bitwise XOR operation.
# Return the integer x. The test cases are generated such that x is uniquely determined.
# The number of set bits of an integer is the number of 1's in its binary representation.

class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        num_bits = bin(num2).count('1')

        x = 0

        for i in range(31, -1, -1): 
            if num_bits == 0:
                break
            if (num1 & (1 << i)) != 0: 
                x |= (1 << i) 
                num_bits -= 1
              
        for i in range(32):
            if num_bits == 0:
                break
            if (x & (1 << i)) == 0:  
                x |= (1 << i)  
                num_bits -= 1
        
        return x
