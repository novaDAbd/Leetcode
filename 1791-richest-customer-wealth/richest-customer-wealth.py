class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        a = [sum(row) for row in accounts]
        richest_customer = max(a)

        return richest_customer