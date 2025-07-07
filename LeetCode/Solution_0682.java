// 682. Baseball Game

import java.util.Stack;

class Solution {
    public int calPoints(String[] operations) {
        Stack<Integer> stk = new Stack<>();
        for (String s : operations) {
            if (!s.equals("C") && !s.equals("D") && !s.equals("+")) {
                stk.add(Integer.parseInt(s));
            } else if (s.equals("+")) {
                int num1 = stk.pop();
                int num2 = stk.pop();
                int num3 = num1 + num2;
                stk.add(num2); 
                stk.add(num1);
                stk.add(num3); 
            } else if (s.equals("C")) {
                stk.pop();
            } else {
                stk.add(stk.peek() * 2);
            }
        }

        int sum = 0;
        while (!stk.isEmpty()) {
            sum += stk.pop();
        }
        return sum;
    }
}