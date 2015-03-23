// 3Sum
// Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

// Note:
// Elements in a triplet (a,b,c) must be in non-descending order. (ie, a ≤ b ≤ c)
// The solution set must not contain duplicate triplets.
//     For example, given array S = {-1 0 1 2 -1 -4},

//     A solution set is:
//     (-1, 0, 1)
//     (-1, -1, 2)


public class Solution {
    public ArrayList<ArrayList<Integer>> threeSum(int[] num) {
        ArrayList<ArrayList<Integer>> result = new ArrayList<ArrayList<Integer>>();
        if(num.length < 3) return result;
        Arrays.sort(num);
        for (int i = 0; i < num.length - 2; i++){
            if(i == 0 || num[i] > num[i-1]){
                int negate = - num[i];
                int l = i+1;
                int r = num.length-1;

                while(l<r){
                //case 1, find result
                    if (num[r] + num[l] == negate) {
                        ArrayList<Integer> triple = new ArrayList<Integer>();
                        triple.add(num[i]);
                        triple.add(num[l]);
                        triple.add(num[r]);
                        result.add(triple);
                        r--;
                        l++;
                        //remove duplicates
                        while(l < r && num[r] == num[r+1]) r--;
                        while(l < r && num[l] == num[l-1]) l++;
                        //case 2
                    } else if (num[r] + num[l] > negate){
                        r--;
                        //case 3
                    } else {l++;}
                }
            }
        }
        return result;
    }
}
