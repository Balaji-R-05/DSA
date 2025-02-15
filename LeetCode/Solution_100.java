// 100. Same Tree

class Solution {
    public boolean isSameTree(TreeNode p, TreeNode q) {
        if(p==null && q==null){
            return true;
        }
        if(p==null || q==null || p.val!=q.val){
            return false;
        }
        return (isSameTree(p.left,q.left) && isSameTree(p.right,q.right));
    }
}

// Time Complexity: O(n)
// Space Complexity: O(n)

