// Number of Steps to Reduce a Number to Zero

#include <iostream>

using namespace std;

class Solution{
    public:
        int numberOfSteps(int num){
            int steps = 0;

            while (num > 0){
                if (num % 2 == 0){
                    num = num / 2;
                    steps++;
                }
                else{
                    num--;
                    steps++;
                }
            }

            return steps;
        }
};

int main(){
    Solution sol = Solution();

    int num = 14;
    int ans = sol.numberOfSteps(num);

    cout << ans << endl;

    return 0;
}
