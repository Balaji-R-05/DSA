// 169. Majority Element

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

// Time Complexity: O(n) - We traverse the list once
// Space Complexity: O(1) - We use a constant amount of space