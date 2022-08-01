### Richest Customer Wealth

# @param {Integer[][]} accounts
# @return {Integer}
def maximum_wealth(accounts)
    max_wealth = 0
    
    accounts.each do |sub|
        max_wealth =  [sub.sum, max_wealth].max
    end
    
    return max_wealth
end

accounts = [[1,2,3],[3,2,1]]
puts maximum_wealth(accounts)