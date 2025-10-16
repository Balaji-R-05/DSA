class Solution_169 {
    public int majorityElement(int[] nums) {
        int count = 0, candidate = 0;
        for(int num: nums){
            if(candidate==num){
                count += 1;
            }else if(count==0){
                candidate = num;
            }else{
                count -= 1;
            }
        }
        return candidate;
    }
}

// Time Complexity - O(N)
// Space Complexity - O(1)