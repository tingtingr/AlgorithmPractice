public class Solution {
    // public int trailingZeroes(int n) {
    //     if ( n<0 ) return -1;
    //     int count = 0;
    //     for (long i=5; n/i>=1; i*=5) {
    //         count += n / i;
    //     }        
    //     return count;
    // }
    public int trailingZeroes(int n) {
        int result = 0;
        int i = 1;
        while(n >= Math.pow(5,i)) {
          result = result + (int)(n /Math.pow(5,i));
          i++;
        }
        return result;
    }
}
