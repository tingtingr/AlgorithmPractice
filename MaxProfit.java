/*Best Time to Buy and Sell Stock
*
*Say you have an array for which the ith element is the price of a given stock on day i.
*If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.
*/
public class Solution {
    public int maxProfit(int[] A) {
        int profit = 0;
        if(A.length <= 1){
          return profit;
        }
        int min = A[0];
        for(int i = 0; i < A.length; ++i) {
          int currentProfit = A[i] - min;
          if(currentProfit < 0) {
            min = A[i];
          }
          profit = Math.max(profit, currentProfit);
        }
        return profit;
        }
}
