// two pointers, i =0; j = s.length()-1;
// iterate through the array, if charAt is not a number or alpha, then increase / decrease,
// return false or return true at the end.

public class Solution {
    public boolean isPalindrome(String s) {
        if(s == null) return false;
        // if (s.length() < 2) return true;--no need
        s = s.replaceAll("[^a-z0-9A-Z]","").toLowerCase();
        int i = 0;
        int j = s.length()-1;
        while(i<j) {
            if(s.charAt(i) == s.charAt(j)) {
                i++;
                j--;
            } else return false;
        }
        return true;
    }
}
