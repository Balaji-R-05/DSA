// 412. Fizz Buzz

import java.util.ArrayList;
import java.util.List;

class Solution {
    public List<String> fizzBuzz(int n) {
        List<String> res = new ArrayList<>(n);
        for(int i=1;i<=n;i++){
            if(i%3==0 && i%5==0){
                res.add("FizzBuzz");
            }else if(i%3==0){
                res.add("Fizz");
            }else if(i%5==0){
                res.add("Buzz");
            }else{
                res.add(String.valueOf(i));
            }
        }
        return res;
    }
}

// Time Complexity: O(n)
// Space Complexity: O(n)

