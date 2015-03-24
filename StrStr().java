// Implement strStr()

// Returns the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

// Update (2014-11-02):
// The signature of the function had been updated to return the index instead of the pointer. If you still see your function signature returns a char * or String, please click the reload button  to reset your code definition.


public class Solution {
        public static int strStr(String haystack, String needle) {
        int result =0;
        if (needle.length() == 0 ||needle == null) return result;
        if (needle == haystack) return result;
        if (haystack.length() < needle.length()) return -1;
        int lenNeedle = needle.length();
        int lenHaystack = haystack.length();
        // outside loop for haystack
        // inner loop for needle
        for (int i = 0; i < lenHaystack; ) {
            //the chars matches, then go inside the inner loop;
            //if not, then proceed i;
            if (haystack.charAt(i) != needle.charAt(0)) {
                i++;
            } else {
                int j;
                for (j = 0; j < lenNeedle && i+j < lenHaystack; ) {
                    //if the char matches, then check the next one untill reached the end
                    if (haystack.charAt(i+j) == needle.charAt(j)){
                        j++;
                    } else break;
                }
                if (j == lenNeedle)
                    return i;
                else ++i;
            }
        }
        return -1;
    }
