# Made by Ethan O'Connor
# Spire ID: 34445111



#class Stack - the main class for Stack seen in lecture 5. 
# Reminder: stack is a private variable
# To complete: *  __str__ method must be included that displays the stack in reverse
# order from the bottom to the top (with index 0 at the bottom)
#             * swap method: two swap the top with top-1 item
#             * copy method: duplicate the top item
#             * flush method: to empty the stack


class Stack:
    #constructor
    def __init__(self):
        self.__stack = []  # create private stack
    
    def __str__(self):
        theStack = ""
        i=0
        for indexY in self.__stack:
            theStack = theStack + str(i) + "\t" + str(indexY) + "\n"
            i+=1
        return theStack

    #methods
    def swap(self):
        endOfStack = len(self.__stack)-1
        swapItem = self.__stack[endOfStack]
        self.__stack[endOfStack] = self.__stack[endOfStack-1]
        self.__stack[endOfStack-1] = swapItem
        return "swap"
    
    def copy(self):
        endOfStack = len(self.__stack)-1
        self.__stack.append(self.__stack[endOfStack])
        return "copy"
    
    def flush(self):
        self.__stack = []
        return "flushed"
    
    def pop(self):  #pop the item
        if self.isEmpty(): return None
        return self.__stack.pop()

    def peek(self): #peek the item (no removal)
        if self.isEmpty(): return None
        return self.__stack[len(self.__stack)-1]

    def push(self, item): #push the item
        self.__stack.append(item)

    def getSize(self):           #return stack size
        return len(self.__stack)

    def isEmpty(self): #check if stack empty
        return self.getSize()==0
    
################################
################################

def main():
    mystack=Stack()
    for i in range(1,4): mystack.push(i*10)
    
    print("test __str__")
    print(mystack)

    print("test swap")
    mystack.swap()
    print(mystack)

    print("test copy")
    mystack.copy()
    print(mystack)

    print("test flush")
    mystack.flush()
    mystack.push(11)
    print(mystack)
    
## call the main function if this file is directly executed
if __name__=="__main__":
    main()