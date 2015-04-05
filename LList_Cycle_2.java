public class Solution {
    public ListNode detectCycle(ListNode head) {
        ListNode turtle = head;
        ListNode bunny = head;
        while(true) {
                if(bunny == null || bunny.next== null) {
                    return null;
                }
            turtle = turtle.next;
            bunny = bunny.next.next;
            if(turtle == bunny) {
                break;
            }
        }
        turtle = head;
        while(turtle != bunny) {
                bunny = bunny.next;
                turtle = turtle.next;
            }
            return turtle;
    }
}
