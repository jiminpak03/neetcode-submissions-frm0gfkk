class Solution {
    public int maxProfit(int[] prices) {
        int profit = 0;
        int min = 101;

        for (int price : prices) {
            profit = Math.max(profit, price - min);
            if (price < min) {
                min = price;
            }

        }
        return profit;
    }
}
