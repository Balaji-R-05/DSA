// The task is to reverse the linked list. We need to reverse the list by changing the links between nodes.

// To explain it further, you need to start printing the data from the tail and move towards the head of the list, printing the head data at the end.

// image

// image

// Input Format

// One line makes up the input.
// Every input is an integer, separated by whitespace.

// Constraints

// The number of nodes in the list is the range [0, 5000].
// -5000 <= Node.val <= 5000

// Output Format

// After reversing, print the connected list.
// You can use recursive or iterative methods to reverse the linked list.
// Can you put both into practise?

import java.io.*;
import java.util.*;

class Node{
    int value;
    Node next;
    Node (int data){
        this.value = data;
    }
}

class Linkedlist{
    static Node head = null;
    static Node last = null;
    static HashSet<Integer> elements = new HashSet<>();
    Linkedlist(){
    }
    static void insert(int data){
        if (elements.contains(data)){
            return;
        }
        elements.add(data);
        Node newNode = new Node(data);
        if (head==null){
            head = newNode;
            last = newNode;
        }
        else{
            last.next = newNode;
            last = last.next;
        }
    }
    
    static void display(){
        Node current = head;
        while(current!=null){
            System.out.print(current.value + " ");
            current = current.next;
        }
    }
    
    static void reverse(){
        Node curr = head;
        int count=0;
        ArrayList<Integer> arr = new ArrayList<>();
        while(curr!=null){
            arr.add(curr.value);
            count += 1;
            curr = curr.next;
        }
        for(count = count-1;count>=0;count--){
            System.out.print(arr.get(count) + " ");
        }
    }
}
public class Solution {

    public static void main(String[] args) {
        Linkedlist ll = new Linkedlist();
        Scanner sc = new Scanner(System.in);
        String s = sc.nextLine();
        String[] inputArray = s.split(" ");
        for(String e: inputArray){
            ll.insert(Integer.parseInt(e));
        }
        ll.reverse();
    }
}