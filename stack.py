print("stack implementation")
stack=[]
while True:
    print("what operation would you like to perform? \n 1.Insert an element,2.Delete an element an element,3.check size of stack,4.Emptiness of stack,5.EXIT")
    n=int(input())
    if n==1:
        print("enter the element to be inserted:")
        l=input()
        stack.append(l)
        print("the element in the stack are:",stack)
    elif n==2:
        if stack==[]:
            print("the stack is empty")
        else:
            stack.pop(0)
            print("the element in the in the stack are :",stack)
    elif n==3:                   
            print("the size of the stack is:",len(stack))
                   
    elif n==4:
        if stack==[]:
            print("your stack is empty!")    
        else:
            print("you have ",len(stack),"elements in tour stack")
    elif n==5:
        print("Exit")
        break
         
