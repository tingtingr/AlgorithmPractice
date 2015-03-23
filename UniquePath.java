// Unique Paths
// A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

// The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

// How many possible unique paths are there?


// Above is a 3 x 7 grid. How many possible unique paths are there?

// Note: m and n will be at most 100.

public class Solution {
    public int uniquePaths(int m, int n) {
        int[] ways = new int[n];
        ways[0] = 1;
        for(int i = 0; i < m; ++i) {
            for(int j = 1; j < n; ++j){
                ways[j] = ways[j] + ways[j-1];
            }
        }
        return ways[n-1];
    }
}

//Or you can use Fibonacci, but I like this way more.
