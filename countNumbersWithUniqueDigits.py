class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        res = []
        se			lf.helper(n,0,[],res)
        return len(res)

    def helper(n,index,sub,res):
        if len(sub) > 2:
            s = "".join([str(y) for y in sub]
            res.append(s)
        else:
            self.helper(n,,
    
    def
            
n = 2        
Solution().countNumbersWithUniqueDigits(n)


public class Solution {
    int res = 0;
    boolean[] used = new boolean[10];
    public int countNumbersWithUniqueDigits(int n) {
        helper(n, false);
        return res;
    }
    public void helper(int n, boolean includeZero){//the first digit can't be zero, so includeZero is initialized with false
        ++res;
        if(n==0) return;
        for(int i = includeZero? 0: 1;i<=9;++i){
            if(used[i]) continue;
            used[i] = true;
            helper(n-1, true);
            used[i] = false;
        }
    }
}