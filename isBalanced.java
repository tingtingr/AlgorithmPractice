// Balanced Binary Tree
// Given a binary tree, determine if it is height-balanced.

// For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

/**
 * Definition for binary tree
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */

public class Solution{
    public boolean isBalanced(TreeNode root) {
        if(root == null)
            return true;
        if(getHeight(root) == -1)
            return false;

        return true;
    }

    public int getHeight(TreeNode root){
        //reach the end of the tree, the node has no children then the height is zero
        if(root == null)
            return 0;
        //recursively calling the left and right children,will return when reached the end
        int left = getHeight(root.left);
        int right = getHeight(root.right);
        //if the difference between two nodes are bigger than 1, return -1;
        if(Math.abs(left-right)> 1)
            return -1;
        //if the left or right is unbalanced. the tree is unbalanced.
        if(left == -1 || right == -1)
            return -1;
        return Math.max(left,right) +1;
    }
}
