tion for binary tree
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
// Solution 1: Recursive:
 
// public class Solution {
//     public boolean isSymmetric(TreeNode root) {
//         if (root == null) return true;
//         return isSymmetricTree(root.left, root.right);
//     }
//     public boolean isSymmetricTree (TreeNode left, TreeNode right) {
//         if(left == null && right == null) return true;
//         if(left == null || right == null) return false;
//         boolean leftT = false, rightT = false;
//         if(left.val == right.val) {
//             leftT = isSymmetricTree(left.right, right.left);
//             rightT = isSymmetricTree(left.left, right.right);
//         }
//         return leftT && rightT;
//     }
// }

// Solution 2: Iterative, utilizing stack. stack could be implemented using LinkedList, and stack
// public class Solution {
//     public boolean isSymmetric(TreeNode root) {
//         //if the root is null, it is still symmetrical
//         if(root==null) return true;
//         // create two stacks to keep track of the elements, put in in left-right reveresed order.
//         LinkedList<TreeNode> left = new LinkedList<TreeNode>(),
//                             right = new LinkedList<TreeNode>();
//         //initialize the value;
//         left.add(root.left);
//         right.add(root.right);
//         //while()
//         while(!left.isEmpty() && !right.isEmpty()) {
//             // let the temp1 hold the first element of left, and vice versa
//             TreeNode temp1 = left.poll(),
//                      temp2 = right.poll();
//             //case 1: one branch is shorter
//             if(temp1 == null && temp2 != null || temp1 != null && temp2 == null) return false;
//             if(temp1 != null && temp2 != null) {
//                 // if values are the same then add the values (left-right reversely)
//                 if(temp1.val != temp2.val) return false;
//                     left.add(temp1.left);
//                     left.add(temp1.right);
//                     right.add(temp2.right);
//                     right.add(temp2.left);
//             }
//         }
//         return true;
//     }
// }

// Solution 2: using stack (rewrite)
public class Solution {
    public boolean isSymmetric(TreeNode root) {
        //corner case
        if (root == null) return true;
        //initializing two stacks
        Stack<TreeNode> left = new Stack<TreeNode>();
        Stack<TreeNode> right = new Stack<TreeNode>();
        left.push(root.left);
        right.push(root.right);
        while(!left.isEmpty() && !right.isEmpty()) {
            //similar
            TreeNode temp1 = left.pop();
            TreeNode temp2 = right.pop();
            //uneven branch case
            if (temp1 == null && temp2 != null || temp1 != null && temp2 == null ) return false;
            if (temp1 != null && temp1 != null) {
                if (temp1.val != temp2.val) return false;
                left.push(temp1.left);
                left.push(temp1.right);
                right.push(temp2.right);
                right.push(temp2.left);
            }
        }
        return true;
    }
}


