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
        Node prev = null;
        Node next = null;
        
        while (curr!=null){
            next = curr.next;
            curr.next = prev;
            prev = curr;
            curr = next;
        }
        head = prev;
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
        ll.display();
    }
}