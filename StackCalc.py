# Made by Ethan O'Connor
# Spire ID: 34445111



#class StackCalc: a class that extends (inherit) the functionalities
# of the class Stack 

from Stack import *                 # Got rid of import copy as it is unnecessary with the
import numpy as np                  #createList function in Queue.py (it is simply more efficient)

class StackCalc(Stack):             
    def __init__(self):        
      super().__init__()
      self.infix="" 
    
    def rpnCommand(self,operator):
      if (StackCalc.isOperator(operator)) == False:
        if operator == "pi":operator=np.pi   #quick way to swap pi and e to real numbers
        if operator == "e":operator=np.e
        self.push(float(operator))        #pushes numbers to stack quickly
        return "push number/e/pi"

      if operator == "+":
        if self.getSize() < 2:
           return "Not enough inputs"
        scnd,frst=self.pop(),self.pop()
        self.push(frst+scnd)
        return "+"

      if operator == "-":
        if self.getSize() < 2:
           return "Not enough inputs"       #"+ - * / **" functions are extremely similar and 
        scnd,frst=self.pop(),self.pop()     #pretty self explanatory. the return statement
        self.push(frst-scnd)                #with what it is doing (ie return "-") is unnecessary
        return "-"                          #but not bad for debugging (although a return is needed)

      if operator == "*":
        if self.getSize() < 2:
           return "Not enough inputs"       # As a quick explanation anyway, scnd (2nd) is set before 
        scnd,frst=self.pop(),self.pop()     #frst (1st) as pop() returns the last and then 2nd to last
        self.push(frst*scnd)                #input, essentially flipping the order (for example,
        return "*"                          #"1 2 -" stack input should do 1-2, not 2-1)

      if operator == "**":
        if self.getSize() < 2:
           return "Not enough inputs"
        PowerOfx,xToThe = self.pop(),self.pop()
        self.push(xToThe**PowerOfx)
        return "**"
      
      if operator == "/":
        if self.getSize() < 2:
           return "Not enough inputs"
        scnd,frst=self.pop(),self.pop()
        self.push(frst/scnd)
        return "/"
      
      if operator == "exp":
        if self.isEmpty():
           return "Not enough inputs"
        self.push(np.e**self.pop())
        return "exp" 
      
      if operator == "cos":
        if self.isEmpty():
           return "Not enough inputs"
        self.push(np.cos(self.pop()))
        return "cos"   

      if operator == "sin":               # sin, cos, sqrt, abs, exp are all similar,
        if self.isEmpty():                #they only effect the last value given
           return "Not enough inputs"     # Essentially, just pop the last number and
        self.push(np.sin(self.pop()))     #then do whatever is requested to it (sin() it for ex.)
        return "sin"
      
      if operator == "log":
        if self.isEmpty():
           return "Not enough inputs"
        self.push(np.log(self.pop()))
        return "log"
      
      if operator == "abs":
        if self.isEmpty():
           return "Not enough inputs"
        self.push(abs(self.pop()))
        return "abs"
      
      if operator == "sqrt":
        if self.isEmpty():
           return "Not enough inputs"
        self.push(np.sqrt(self.pop()))
        return "sqrt"
      
      if operator == "copy":
        if self.isEmpty():
          print("Nothing to copy.")
          return "error"
        self.copy()                 
        return "copy"
      
      if operator == "swap":
        if self.getSize() < 2:
          print("Can't swap, not enough inputs.")
          return "error"
        self.swap()
        return "swap"
      
      if operator == "flush":
        self.flush()
        return "flushed"
    
      if operator == "x": #prevents error as float(x) doesnt work (below)
        self.push("x")
        return "x"
      else:
         print("Invalid input") #if none of the other if's run, it is an invalid input
         return "error"
      

    @staticmethod

    def isOperator(currentChar):
      lstofNormOperators = {"swap","copy","sqrt","abs","log","**","sin","cos","/","*","-","+","exp"}
      if currentChar in lstofNormOperators:
        return True           #essentially, if input is not operator ^, it will return false.
      return False
    
    def evaluate_postfix(queue,userInputX):       # For postfix print, prints last created/modified
        listqueue=queue.createList()    # createList is explained at the bottom of Queue.py
        mystack=StackCalc()
        for prompt in listqueue:        # Go through all commands to evaluate answer
            if prompt=="x":           #if run was never inputted
                prompt = userInputX
            mystack.rpnCommand(prompt)
        return str(mystack.peek())+"\n"        #__stack variable to match infix

    def postfix2infix(queue):
      listqueue = queue.createList()           # create the list.
      infix = []
      onepop={"sqrt","cos","sin","abs","log"}  # special ones, only modify last value, not 2
      basic={"+","-","*","**","/"}
      for currentChar in listqueue:                         #sidenote: flush can be ignored as it 
          if (StackCalc.isOperator(currentChar)) == False:  #never gets sent into postfix2infix()
              infix.insert(0, currentChar) 
          else:
              if currentChar in basic:     # I decided to insert things into "infix"
                op1 = infix.pop(0)         #similar to how queue's enqueue() function works
                op2 = infix.pop(0) 
                infix.insert(0, "(" + op2 + currentChar + op1 + ")") 
              elif currentChar in onepop:  # these only require 1 previous input, not 2
                op1 = infix.pop(0)
                infix.insert(0, currentChar + "(" + op1 + ")") 
              elif currentChar=="exp":     # special case to ensure it gets eval()'d correctly
                op1 = infix.pop(0)
                infix.insert(0, "e**" + op1) 
              elif currentChar == "copy":     
                infix.insert(0, infix[0])  # adds a copy to start of stack
              elif currentChar == "swap":
                swap=infix[0] 
                infix[0]=infix[1] 
                infix[1]=swap
              else:
                 print("Invalid input:", currentChar)
                 print("Quit and restart")
      return infix[0]