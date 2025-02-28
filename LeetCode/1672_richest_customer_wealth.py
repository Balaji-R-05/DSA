# 1672. Richest Customer Wealth

from typing import List

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        richest = 0
        for account in accounts:
            balance = 0
            for amt in account:
                balance += amt
            richest = max(richest, balance)

        return richest