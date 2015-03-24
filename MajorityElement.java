/*Majority Element
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

Code 2 is works for a more general case : find the element that has the most occurance.
since we could make use of the key fact that this element occures more than 2/n, thus there is only one.
*/
public class Solution {
    public int majorityElement(int[] num) {
        HashMap<Integer, Integer> result = new HashMap<Integer, Integer>();
        for ( int i = 0 ; i < num.length; i ++) {
            if (result.containsKey(num[i]) == false) {
                result.put(num[i], 1);
            } else {
                result.put(num[i], result.get(num[i]) + 1);
            }
            //becareful where you put the ifs, it may have a totally different effects
            if (result.get(num[i]) > num.length/2) {
                return num[i];
            }
        }
        return -1;
    }
}
/*
code 2
public int majorityElement(int[] num) {
        HashMap<Integer, Integer> result = new HashMap<Integer, Integer>();
        int count = 1;
        int max =0;
        int index = num[0];
        for ( int i = 0 ; i < num.length; i ++) {
            if (result.containsKey(num[i]) == false) {
                result.put(num[i], count);
            } else {
                result.put(num[i], result.get(num[i]) + 1);
            }
            if (result.get(num[i]) > max) {
                max = result.get(num[i]);
                index = i;
            }
        }
        return num[index];
    }
*/
