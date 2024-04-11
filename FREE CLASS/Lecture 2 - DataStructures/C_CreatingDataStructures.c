# include <stdio.h>
# include "CDataStructures.c"
# pragma warning(suppress: 4996)

int main(){
    // Lets create a stack 
    printf("......Creating a Stack.......\n");
    Stack *stack = createStack();
    push(stack, 5);
    printf("After pushing elements into the stack: \n");
    displayStack(stack);
    
    pop(stack, 2);
    printf("\nAfter popping elements from the stack: \n");
    displayStack(stack);
    
    // Creating queue of size 100
    printf("\n......Creating a Queue.......\n");
    Queue *queue = createQueue(100);
    enqueue(queue, 5);
    printf("After enqueue: \n");
    displayQueue(queue);
    
    printf("\nAfter dequeue: \n");
    dequeue(queue, 2);
    displayQueue(queue);

    // Creating a LinkedList of 5 nodes
    printf("\n......Creating a Linked list.......\n");
    Node *linkedlist = createlinkedList(5);
    displayLinkedlist(linkedlist);
}