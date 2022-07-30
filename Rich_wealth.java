import java.util.stream.IntStream;

public class Rich_wealth {
    public static void main(String[] args) {
        Solution sol = new Solution();

        int[][] accounts = {{1,2,3},{3,2,1}};

        System.out.println(sol.maximumWealth(accounts));
    }
    
}

class Solution {
    public int maximumWealth(int[][] accounts) {
        int max_wealth = 0;

        for (var i : accounts) {
            max_wealth = Math.max(max_wealth, IntStream.of(i).sum());
        }
        return max_wealth;
    }
}