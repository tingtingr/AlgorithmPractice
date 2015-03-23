// Same Tree
// Given two binary trees, write a function to check if they are equal or not.

// Two binary trees are considered equal if they are structurally identical and the nodes have the same value.

/**
 * Definition for binary tree
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */

// simple recursive programming
// if both nodes are null, return true;
// if either is null, return false;

// longer version

public class Solution {
    public boolean isSameTree(TreeNode p, TreeNode q) {
        if (p == null && q == null) {
            return true;
        }
        if ( p == null ||  q == null) return false;
        if(p != null && q != null) {
            if(p.val == q.val) {
                return isSameTree(p.left, q.left) && isSameTree(p.right, q.right);
            }
        }
        return false;
    }
}

// shorter version

// public class Solution {
//     public boolean isSameTree(TreeNode p, TreeNode q) {
//         if (p == null && q == null) return true;
//         if(p != null && q != null && p.val == q.val)
//             return isSameTree(p.left, q.left) && isSameTree(p.right, q.right);
//         return false;
//     }
// }
