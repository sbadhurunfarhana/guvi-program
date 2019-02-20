print("queue implementation")
queue=[]
while True:
    print("what operation would you like to perform? \n 1.Enqueue an element,2.Dequeue an element,3.check size of stack,4.Emptiness of stack,5.EXIT")
    n=int(input())
    if n==1:
        print("enter the element to be inserted:")
        l=input()
        queue.append(l)
        print("the element in the queue are:",queue)
    elif n==2:
        if queue==[]:
            print("the queue is empty")
        else:
            queue.pop(0)
            print("the element in the in the queue are :",queue)
    elif n==3:                   
            print("the size of the queue is:",len(queue))
                   
    elif n==4:
        if queue==[]:
            print("your queue is empty!")    
        else:
            print("you have ",len(queue),"elements in tour queue")
    elif n==5:
        print("Exit")
        break
