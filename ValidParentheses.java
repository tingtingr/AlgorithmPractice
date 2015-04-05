public class Solution {
    public boolean isValid(String s) {
        if (s.length()% 2 != 0) return false;
        Stack stack = new Stack();
        for (int i = 0 ; i < s.length(); i ++) {
            if(stack.empty() || s.charAt(i) == '(' || s.charAt(i) == '{' || s.charAt(i)=='['){
                stack.push(s.charAt(i));
            }
            if(s.charAt(i) == ')' && (char)stack.pop() != '(') return false;
            if(s.charAt(i) == '}' && (char)stack.pop() != '{') return false;
            if(s.charAt(i) == ']' && (char)stack.pop() != '[') return false;
        }
        if (stack.empty()) return true;
        return false;
    }
}
