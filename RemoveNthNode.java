tion for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */

//solution:
//  have two pointers, one goes to the end of the linked list
//  another one was delay by n, then once the first one reached the end
// node.next = node.next.next to remove.
// becarefull about the special cases.

public class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        ListNode copy1 = head;
        ListNode copy2 = head;
        ListNode result = head;
        if(copy1.next == null){
            return null;
        }
        int counter = 0;
        while (copy1.next != null) {
            copy1 = copy1.next;
            counter ++;
            if(counter > n) {
                copy2=copy2.next;
            }
        }
        if(counter < n) return result.next;
        else copy2.next= copy2.next.next;
        return result;
    }
}
