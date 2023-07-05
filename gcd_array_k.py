import itertools
import math

class Solution:
    def gcdArray(self, L, k):
        return math.gcd(*L) == k

    def allSubArrays(self, L, k):
        # 82/87 test cases passed 
        n = len(L)
        count = 0
        indices = list(range(n+1))
        for w in range(1, len(L)+1):
            for i in range(len(L)-w+1):
                if self.gcdArray(L[i:i+w], k) == 1:
                    count += 1
        return count

    def approach1(self, nums: List[int], k: int) -> int:
        return self.allSubArrays(nums, k)

    def subarrayGCD(self, nums: List[int], k: int) -> int:
        return self.approach1(nums, k)