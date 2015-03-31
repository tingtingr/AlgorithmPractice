//use the fact that A XOR A = A
//A XOR B XOR A = B

public class Solution {
    public int singleNumber(int[] A) {
        int result = A[0];
        for (int i = 1; i < A.length; i++) {
            result ^= A[i];
        }
        return result;
    }
}
