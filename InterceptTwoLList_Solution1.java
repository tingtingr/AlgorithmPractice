public class Solution {
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        if (headA == null || headB == null) {
            return null;
        }
        int lenA = length(headA);
        int lenB = length(headB);
        int diff = Math.abs(lenA-lenB);
        while(diff > 0) {
            if(headA == headB) {
                return headA;
            }
            if(lenA > lenB) {
                headA = headA.next;
                diff--;
            }
            if(lenA < lenB) {
                headB = headB.next;
                diff--;
            }
        }
        if(diff == 0) {
            while(headA != null) {
                if(headA == headB) {
                    return headA;
                }
                headA = headA.next;
                headB = headB.next;
            }
        }
        return null;
    }
    public int length (ListNode A ) {
        int count = 1;
        while (A.next != null ) {
            A = A.next;
            count++;
        }
        return count;
    }
}
