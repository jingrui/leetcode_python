/**
 * Definition for binary tree
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class Solution {
    public TreeNode sortedArrayToBST(int[] num) {
        if (num.length == 0){
            return null;
        }
        
        int mid = num.length/2;
        TreeNode root = new TreeNode(num[mid]);
        
        int lefts = 0;
        int lefte = mid-1;
        if (lefte >= lefts){
            int[] left = Arrays.copyOfRange(num,lefts,lefte+1);
            root.left = sortedArrayToBST(left);
        }else{
            root.left = null;
        }
        
        int rights = mid+1;
        int righte = num.length-1;
        if (righte >= rights){
            int[] right = Arrays.copyOfRange(num,rights,righte+1);
            root.right = sortedArrayToBST(right);
        }else{
            root.right = null;
        }
        return root;
    }
}
