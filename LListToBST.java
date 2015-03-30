tion for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; next = null; }
 * }
 */
/**
 * Definition for binary tree
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
// note: the most important trick is the mid-1, which triggers the default case.
// remember to move the pointer before doing the right side.
public class Solution {
        
    static ListNode currentHead = null;
    TreeNode buildTree(int start, int end) {
        if(start>end) {
            return null;
        }
        int mid = (end + start) / 2;
        TreeNode left = buildTree(start,mid-1);
        TreeNode root = new TreeNode(currentHead.val);
        root.left = left;
        currentHead = currentHead.next;
        root.right = buildTree(mid+1,end);
        return root;
    }
        public TreeNode sortedListToBST(ListNode head) {

        if(head == null) return null;
        currentHead = head;
        ListNode copy1 = head;
        int len = 1;
        while(copy1.next != null) {
            len++;
            copy1 = copy1.next;
        }
        return buildTree(0,len-1);
    }
}

