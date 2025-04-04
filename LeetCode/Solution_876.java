// 876. Middle of the Linked List

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode middleNode(ListNode head) {
        ListNode mid = head;
        ListNode end = head;
        while(end.next!=null){
            mid = mid.next;
            end = end.next;
            if(end.next!=null){
                end = end.next;
            }
        }
        return mid;
    }                                                                                           
}