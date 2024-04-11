package com.aycodez;

import com.aycodez.JavaDataStructures.*;

public class JavaCreatingDataStructures {
    public static void main(String[] args){
        // Let's create a stack
        System.out.println("......Creating a Stack.......");
        Stack stack = new Stack();
        stack.push(5);  //Pushing 5 elements into the stack
        System.out.println("After pushing elements into the stack: ");
        stack.display_stack();

        stack.pop(2); // popping 2 elements from the stack
        System.out.println("After popping elements from the stack: ");
        stack.display_stack();

        // Let's create a queue
        System.out.println(".......Creating a Queue .......");
        Queue q = new Queue(10);
        q.enqueue(5);  // Adding 5 elements into the stack
        System.out.println("\nAfter enqueue: ");
        q.display_queue();

        q.dequeue(2);  // removing 2 elements from the stack
        System.out.println("\nAfter dequeue: ");
        q.display_queue();

        // Creating a linked list
        System.out.println(".......Creating a linked list.......");
        LinkedList l = new LinkedList();
        l.addNodes(3);  // # creating 3 nodes
        l.displayList();
    }
}
