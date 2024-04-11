package com.aycodez;

import java.util.Scanner;

public class JavaDataStructures {
    static class Stack{
        int MAXSIZE = 100;
        int top = -1;
        int[] items = new int[MAXSIZE]; // setting size of stack
        Scanner sc = new Scanner(System.in);

        public boolean isFull(){
            return this.top == this.MAXSIZE - 1;
        }
        public boolean isempty(){
            return this.top == -1;
        }


        public void push(int num_push){
            for(int i = 0; i < num_push; i ++){
                if (this.isFull()){
                    System.out.println("Stack overflow"); // checking to see if stack is full
                    return;
                }
                this.top += 1;
                System.out.print("Enter element to add to stack: ");
                int number_push = this.sc.nextInt();
                this.items[this.top] = number_push;
//                return f"{num_push} elements added to the stack"
            }
        }

        public void pop(int num_pop){
            for(int i = 0; i < num_pop; i ++){
                if (this.isempty()){
                    System.out.println("Stack Underflow");
                    return;
                }
                this.top -= 1;
            }
        }
        public void display_stack(){
            System.out.println("Stack: ");
            int head = this.top;
            while (head >= 0){
                System.out.println("|  " + this.items[head] + "  | ");
                head -= 1;
            }
        }
    }


   //Creating a queue data structure
    public static class Queue{
        int front;
        int rear;
        int[] array;
        int max;
        int size;
        Scanner sc = new Scanner(System.in);
        public Queue(int capacity)
        {
            this.front = 0;
            this.rear = - 1;
            this.array = new int[capacity]; // creating an empty queue of size capacity
            this.max = capacity;
            this.size = 0;
        }
        public boolean isFull(){
            return this.rear == this.max - 1;
        }
       public boolean isEmpty(){
           return this.size == 0;
       }
       public void enqueue(int num_times){
           for (int i = 0; i < num_times; i++) {
               if (this.isFull()){
                   System.out.println("Queue Overflow");
                   return;
               }
               System.out.print("Enter element to add to queue: ");
               int data = this.sc.nextInt();
               this.rear += 1;
               this.array[this.rear] = data;
               this.size += 1;
           }
       }
       public void dequeue(int num_times){
           for (int i = 0; i < num_times; i++) {
               if (this.isEmpty()){
                   System.out.println("Empty Queue");
                   return;
               }
               this.front += 1;
               this.size -= 1;
           }
       }
       public void display_queue(){
           int front = this.front;
           int size = this.size;
           System.out.print("Queue: ");
        // checking to see if the queue is empty
           while (size > 0){
               System.out.print("| " + this.array[front] + " | ");
               front += 1;
               size -= 1;
           }
       }


    }
    public static class LinkedList{
        Node head;
        Node tail;
        public LinkedList(){
            this.head = null;
            this.tail = null;
        }
        public class Node{
            int value;
            Node next;

            public Node(int value){
                this.value = value;
                this.next = null;
            }
        }
        public void addNodes(int numNodes){
//            Node ctrPtr = this.head== null ?null:this.head;
            Scanner sc = new Scanner(System.in);
            for (int i = 0; i < numNodes; i++) {
                System.out.print("Enter value for "+ (i + 1) + " node: " );
                int value = sc.nextInt();
                Node newNode = new Node(value);
                if (this.head == null){
                    this.head = newNode;
                    this.tail = this.head;
//                    ctrPtr = this.head;
                }
                else {
                    this.tail.next = newNode;
                    this.tail = newNode;
                }
            }
        }
        public void displayList(){
            if (this.head == null){
                System.out.println("Empty list!!!");
                return;
            }
            Node ptr = this.head;
            System.out.print("Linked list: ");
            while (ptr != null){
                System.out.print(ptr.value + " ");
                ptr = ptr.next;
            }
            return;
        }
    }
//    public static void main(String[] args){
////        Queue queue = new Queue(10);
////        queue.enqueue(5);
////        System.out.println("after enqueue");
////        queue.display_queue();
////        queue.dequeue(2);
////        System.out.println("after dequeue");
////        queue.display_queue();
//        Stack stack = new Stack();
//
//        stack.push(5);
//        System.out.println("after push");
//        stack.display_stack();
//        stack.pop(2);
//        System.out.println("after pop");
//        stack.display_stack();
//    }
//
}
