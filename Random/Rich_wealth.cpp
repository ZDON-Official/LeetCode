#include <vector>
#include <numeric>
#include <iostream>

using namespace std;


class Solution{
    public:
        int maximumWealth(vector<vector<int>> &accounts){
            int max_wealth = 0;

            for(auto &i : accounts){
                int tot_wealth = accumulate(i.begin(), i.end(), 0);
                max_wealth = max(max_wealth, tot_wealth);
            }
            
            return max_wealth;
        }
};

int main(){
    Solution sol = Solution();

    vector<vector<int>> acc {{1,2,3},{3,2,1}};

    int ans = sol.maximumWealth(acc);

    cout << ans << endl;

    return 0;
}


