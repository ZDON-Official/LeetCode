class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        max_Wealth = 0
        for i in accounts:
            tot_Wealth = sum(i)
            max_Wealth = max(max_Wealth, tot_Wealth)

        return max_Wealth



sol = Solution()

accounts = [[1,2,3],[3,2,1]]
p = sol.maximumWealth(accounts)

print(p)