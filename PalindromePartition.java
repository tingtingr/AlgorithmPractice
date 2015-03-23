// Palindrome Partitioning
// Given a string s, partition s such that every substring of the partition is a palindrome.

// Return all possible palindrome partitioning of s.

// For example, given s = "aab",
// Return

//   [
//     ["aa","b"],
//     ["a","a","b"]
//   ]




public class Solution {
    List<List<String>> ret;
    public List<List<String>> partition(String s) {
        int n = s.length();
        boolean[][] isPalindrome = new boolean[n][n];
        for (int i = 0; i < n; i++)
            isPalindrome[i][i] = true;
        for (int i = n - 1; i >= 0; i--) {
            for (int j = i + 1; j < n; j++) {
                if (s.charAt(i) == s.charAt(j)) {
                    if (j - i < 2 || isPalindrome[i + 1][j - 1])
                        isPalindrome[i][j] = true;
                }
            }
        }
        ret = new LinkedList<>();
        List<String> list = new LinkedList<>();
        partition(s, 0, isPalindrome, list);
        return ret;
    }

    private void partition(String s, int start, boolean[][] isPalindrome, List<String> list) {
        if (start == s.length()) {
            List<String> newList = new LinkedList<>();
            newList.addAll(list);
            ret.add(newList);
            return;
        }
        for (int i = start; i < s.length(); i++) {
            if (isPalindrome[start][i]) {
                list.add(s.substring(start, i + 1));
                partition(s, i + 1, isPalindrome, list);
                list.remove(list.size() - 1);
            }
        }
    }
}
