// Add Binary
// Given two binary strings, return their sum (also a binary string).

// For example,
// a = "11"
// b = "1"
// Return "100".

public class Solution {
    public String addBinary(String a, String b) {
        StringBuilder result = new StringBuilder();
        int aIdx = a.length() -1;
        int bIdx = b.length() -1;
        int carry = 0;
        while(aIdx >= 0 && bIdx >= 0){
            int aBit = a.charAt(aIdx) -'0';
            int bBit = b.charAt(bIdx)- '0';
            int sum = (aBit + bBit + carry) % 2;
            carry = (aBit + bBit+carry) / 2;
            result.insert(0, (char)('0' + sum));
            aIdx--;
            bIdx--;
        }

        while(aIdx >= 0){
            int aBit = a.charAt(aIdx) - '0';
            int sum = (aBit + carry ) % 2;
            carry = (aBit+carry) / 2;
            result.insert(0,(char)('0' + sum));
            aIdx--;
        }
        while(bIdx >= 0){
            int bBit = b.charAt(bIdx) - '0';
            int sum = (bBit + carry) % 2;
            carry = (bBit + carry) / 2;
            result.insert(0,(char)('0' + sum));
            bIdx--;
        }
        if(carry == 1){
            result.insert(0,(char)('0' + 1));
        }
        return result.toString();
    }
}
