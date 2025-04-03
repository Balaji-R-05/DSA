import java.io.*;
import java.util.*;

class Node{
    int value;
    Node next;
    Node (int data){
        this.value = data;
    }
}

class Linkedlist {
    Node head;
    Node tail;
    Linkedlist(){
    }
    static void insert_at_end(int data){
        Node newNode = new Node(data);
        last.next = newNode;
        last = last.next;
    }
    static void insert_at_start(int data){
        Node newNode = new Node(data);
        newNode.next = head;
        head = newNode;
    }
    static void insert_at_pos(int data, int pos){
        
    }
}

public class Solution {

    public static void main(String[] args) {
        
    }
}