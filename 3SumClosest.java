// 3Sum Closest
// Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

//     For example, given array S = {-1 2 1 -4}, and target = 1.

//     The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

public class Solution {
    public int threeSumClosest(int[] num, int target) {
        Arrays.sort(num);
    //set the min to the max value,
    int min = Integer.MAX_VALUE;
    //set result to zero
    int result = 0;
    //iterate the array
    for(int i = 0; i < num.length -2; ++i){
        //lower pointer
        int l = i+1;
        //upper pointer
        int r = num.length -1;
        while(l<r){
            //the current sum of three
            int temp = num[i] + num[l] + num[r];
            //the diff
            int diff = Math.abs(target - temp);
            //compare the diff with the max_value
                //if diff == 0, i.e: target = sum
            if(diff == 0) return temp;
                //since min starts at max_value, when diff is small, decrease min to diff
            if(diff < min){
                min = diff;
                result = temp;
            }
            if(target > temp){
                l++;
            } else r--;
        }
    }
    return result;
    }
}
