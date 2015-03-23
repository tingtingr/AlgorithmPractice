// Climbing Stairs
// You are climbing a stair case. It takes n steps to reach to the top.

// Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

//Note: I think this is the super awesome way to write Fibonaaci question. Pretty happy about it.
public class Solution {
    public int climbStairs(int n) {
        if(n <= 3){
            return n;
        }
     int a = 2;
     int b = 3;
     int c = 5;
     for(int i = 4; i < n; i++) {
         a = b;
         b = c;
         c = a + b;
     }
     return c;
    }
}
