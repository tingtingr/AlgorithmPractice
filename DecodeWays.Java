// Decode Ways
// A message containing letters from A-Z is being encoded to numbers using the following mapping:

// 'A' -> 1
// 'B' -> 2
// ...
// 'Z' -> 26
// Given an encoded message containing digits, determine the total number of ways to decode it.

// For example,
// Given encoded message "12", it could be decoded as "AB" (1 2) or "L" (12).

// The number of ways decoding "12" is 2.


public class Solution {
  public static int numDecodings (String s) {
    //check corner case.
    //string is empty, or is 0.
    if ( s == null || s.length() == 0 ||s == "0")
      return 0;
    //create an Integer array, that the length
    //is the original array + 1; ---> why?
    int[] res = new int[s.length() + 1];
    //set the first element equal to 1;
    res[0] = 1;
    //if the first number in s is valid,
    //then res[1] = 1;
    res[1] = (isValid(s.substring(0,1)))? 1 : 0;
    for (int i = 2; i <= s.length(); i++) {
      if (isValid(s.substring(i-1,i)))
        res[i] += res[i-1];
      if (isValid(s.substring(i-2,i)))
        res[i] += res[i-2];
    }
    return res[s.length()];
  }
  //if the string is within [1,26], return valid
  public static boolean isValid(String s) {
    if (s.charAt(0) == '0') return false;
    int code = Integer.parseInt(s); // turn in to a int
    return code <= 26 && code >= 1;
  }
}
