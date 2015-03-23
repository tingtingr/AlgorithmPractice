// Unique Paths II
//my thoughts:
// if the entry is 1, the paths to that cell is 0;
// then for the first row and col, if the entry is 0, set it to 1; if the entry is 1, set the rest to zero.
// then do the rest as the path I solution.
// trick：
// 针对initialization， value of the cell = min (previous cell, (1-grid[i][j]))，
// 后来发现，其实不用这样。

//There is a trick**: use Math.min / Math.max to reduce the lines of code

//Shorter version:

public class Solution {
    public int uniquePathsWithObstacles(int[][] grid) {
        int row = grid.length;
        int col = grid[0].length;
        if( row == 0 || col == 0 ||grid[0][0] == 1 ||grid[row-1][col-1]==1) return 0;
        int[][] result = new int[row][col];
        result[0][0] = 1;
        for ( int i = 1; i < col; i++) {
            result[0][i] = Math.min(result[0][i-1],(1-grid[0][i]));
        }
        for (int i = 1; i < row; i++) {
            result[i][0] = Math.min(result[i-1][0], (1-grid[i][0]));
        }
        for( int i = 1; i < row; i++) {
            for (int j = 1; j < col; j++ ) {
              result[i][j] = (grid[i][j] == 1)?0:result[i-1][j]+result[i][j-1];
            }
        }
        return result[row-1][col-1];
    }
}

//Longer version:

// public class Solution {
//     public int uniquePathsWithObstacles(int[][] grid) {
//         int row = grid.length;
//         int col = grid[0].length;
//         //如果没有matrix，或者开头或则结尾就是block，就return 0 path
//         if( row == 0 || col == 0 ||grid[0][0] == 1 ||grid[row-1][col-1]==1) return 0;
//         //做一个等大的grid
//         int[][] result = new int[row][col];
//         //如果只有一个cell，那么path ＝ 1；
//         result[0][0] = 1;
//         //in the first row, once see a 1(block), jump to the end.
//         for ( int i = 1; i < col; i++) {
//             // result[0][i] = Math.min(result[0][i-1],(1-grid[0][i]));
//             if(grid[0][i] == 1) {
//                 result[0][i] = 0;
//             } else {
//                 result[0][i] = result[0][i-1];
//             }
//         }
//         //do the first col;
//         for (int i = 1; i < row; i++) {
//             // result[i][0] = Math.min(result[i-1][0], (1-grid[i][0]));
//             或者这么写，是一样的。
//             if (grid[i][0] == 1) {
//                 result[i][0] = 0;
//             } else {
//                 result[i][0] = result[i-1][0];
//             }
//         }
//         for( int i = 1; i < row; i++) {
//             for (int j = 1; j < col; j++ ) {
//               // result[i][j] = (grid[i][j] == 1)?0:result[i-1][j]+result[i][j-1];
//                 if(grid[i][j] == 1) {
//                     result[i][j] = 0;
//                 } else {
//                     result[i][j] = result[i-1][j]+result[i][j-1];
//                 }
//             }
//         }
//         return result[row-1][col-1];
//     }
// }

