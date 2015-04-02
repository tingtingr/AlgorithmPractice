
public class Solution {
    public int reverseBits(int n) {

    }
    public int swapBits(int n, int i, int j) {

      int a = (n >> i ) & 1;
      int b = (n >> j ) & 1;

      if ((a ^ b) != 0;) {
        return n ^ (1 << i)
      }
    }
}
