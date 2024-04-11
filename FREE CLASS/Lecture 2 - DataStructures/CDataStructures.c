# include <stdlib.h>
# include <stdio.h>
# include <stdbool.h>

// initializing a global variable for the maximun size of the stack
# define MAXSIZE 100

// Creating a new data structure to implement a stack using an array
typedef struct Stack{
    int items[MAXSIZE];
    int top;
}Stack;

Stack *createStack(){
    struct Stack *stack = (struct Stack*)malloc(sizeof(struct Stack));
    stack -> top = -1;
    return stack;

}

bool stackIsFull(Stack* stack){
    
    return (stack ->top == MAXSIZE - 1);

}
bool stackisEmpty(Stack *stack){
    return stack->top == -1;
}

int push(Stack *stack, int num_push){
    for(int i=0; i < num_push; i ++){
        if (stackIsFull(stack)){
            printf("Stack Overflow");
            return -1;
        }
        stack -> top = stack->top + 1;
        printf("Enter number to push into stack: ");
        int number_to_push;
        scanf("%i", &number_to_push);
        stack ->items[stack -> top] = number_to_push;

    }

}

int pop(Stack *stack, int num_pop){
    for(int i=0; i < num_pop; i ++){
        if (stackisEmpty(stack)){
            printf("Stack Underflow");
            return -1;
        }
        
        
        stack ->top = stack ->top -1;
    }

}

void displayStack(Stack *stack){
    printf("Stack: \n");
    int head = stack ->top;
    while (head >=0)
    {
        printf("| %i | \n", stack->items[head]);
        head -=1;
    }
    

}
typedef struct Queue{
    int front;
    int rear;
    int max;
    int *array;
    int size;
}Queue;

// Creating a queue data structure
Queue *createQueue(int capacity){
    struct Queue *queue = (Queue*)malloc(sizeof(Queue));
    queue -> front = 0;
    queue -> rear = -1;
    queue->array = (int*)malloc(capacity * sizeof(int));
    queue->max = capacity;
    queue ->size = 0;
    return queue;

}

bool queueisFull(Queue* queue){
    
    return (queue ->rear == queue->max - 1);

}
bool queueisEmpty(Queue *queue){
    return queue->size == 0;
}

int enqueue(Queue *queue, int num_times){
    for(int i=0; i < num_times; i ++){
        if (queueisFull(queue)){
            printf("Queue Overflow");
            return -1;
        }
        
        printf("Enter element to add to queue: ");
        int data;
        scanf("%i", &data);
        queue -> rear =  queue -> rear + 1;
        queue ->array[queue -> rear] = data;
        queue ->size = queue ->size + 1;


    }

}

int dequeue(Queue *queue, int num_times){
    for(int i=0; i < num_times; i ++){
        if (queueisEmpty(queue)){
            printf("Empty Queue");
            return -1;
        }
        queue -> front = queue ->front + 1;
        queue ->size = queue->size -1;
    }

}

void displayQueue(Queue *queue){
    printf("Queue: ");
    int front = queue ->front;
    int size = queue ->size;
    
    while (size > 0)
    {
        printf("| %i | ", queue->array[front]);
        front +=1;
        size -=1;
        
    }
    

}

// Ctreating a new data structure for the node
typedef struct Node
{
    int value;
    struct Node *next;
    
}Node;


Node *createlinkedList(int numNodes)
{
    Node *head = NULL;
    Node *tail = NULL;
    
    for (int i =0; i < numNodes; i ++)
    {
        printf("Enter value for %d node: ", i+1);
        int value;
        scanf("%i", &value);
        
        Node *newNode = malloc(sizeof(Node));
        newNode->value = value;
        if (head == NULL)
        {
            
            head = newNode;
            tail = head;
        }
       
        tail->next = newNode;
        tail = newNode;
        
        
    }
    tail -> next = NULL;
    return head;
}

void displayLinkedlist(Node *head){
    Node *pointer = head;
    printf("Linked list: ");
    while (pointer !=NULL)
    {
        printf("%i ", pointer->value);
        Node * temp = pointer->next;
        free(pointer);
        pointer = temp;
        
    }
    
    
}
