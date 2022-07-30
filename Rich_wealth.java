public static void main(String[] args) {
    
}


class Solution {
    public int maximumWealth(int[][] accounts) {
        int max_wealth = 0;
        
        for(var i : accounts){
            max_wealth = Math.max(max_wealth, IntStream.of(i).sum());
        }
        return max_wealth;
    }
}