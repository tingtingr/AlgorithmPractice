// Two Sum
// Given an array of integers, find two numbers such that they add up to a specific target number.

// The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.
// You may assume that each input would have exactly one solution.
// Input: numbers={2, 7, 11, 15}, target=9
// Output: index1=1, index2=2


public class Solution {
    public int[] twoSum(int[] numbers, int target) {
        HashMap<Integer, Integer> hash = new HashMap<Integer, Integer>();
        int[] result = new int[2];
        for(int i = 0; i < numbers.length; i++){
            if(hash.containsKey(numbers[i])){
                int index = hash.get(numbers[i]);
                result[0] = index +1;
                result[1] = i +1;
            } else {
                hash.put(target-numbers[i], i);
            }
        }
        return result;
    }
}
//be careful about the index-value relations.
//can be done in 1 loop because hash is O(1);
