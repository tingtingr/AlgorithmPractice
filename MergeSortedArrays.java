public class Solution {
    public void merge(int A[], int m, int B[], int n) {
        for(int i = m - 1, j = n -1; i >= 0 || j >= 0; ) {
            if(i < 0 ){
                //check first make sure no outof bound
                A[i+j+1] = B[j];
                j--;
            } else if (j < 0 ) {
                A[i+j+1] = A[i];
                i--;
            } else if (A[i] > B[j]) {
                A[i+j+1] = A[i];
                i--;
            } else {
                A[i+j+1] = B[j];
                j--;
            }
        }
    }
}
