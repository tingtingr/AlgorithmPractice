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
public class Solution {
    public ListNode swapPairs(ListNode head) {
        if(head == null || head.next == null) return head;
        ListNode fakehead = new ListNode(0);
        ListNode res = fakehead;
        fakehead.next = head;
        while(fakehead.next != null && fakehead.next.next != null) {
            swap(fakehead);
            fakehead = fakehead.next.next;
        }
        return res.next;
    }
    public void swap(ListNode head) {
        ListNode a = head.next;
        ListNode b = a.next;
        // Since we have the while loop, the following could be taken out.
        // if (a == null) return;
        // if (b == null) return;
        ListNode c = b.next;  // If c is NULL that is OK.
        a.next = c;
        b.next = a;
        head.next = b;
    }
}
