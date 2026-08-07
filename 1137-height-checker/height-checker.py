import numpy as np
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
       expected = sorted(heights)
       a1=np.array(heights)
       a2=np.array(expected)

       a=int(np.sum(a1!=a2))

       return a