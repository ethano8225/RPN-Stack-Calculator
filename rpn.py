# Made by Ethan O'Connor
# Spire ID: 34445111



from StackCalc import *
from Queue import *
from numpy import *  # if you need sin, just do sin, etc.
import matplotlib.pyplot as plt

# Menu
print()
print("===============================================")
print("================= Project 1 ===================")
print("===============================================")
print("|                                             |")
print("|         1-Simple  RPN calculator            |")
print("|         2-Fancy   RPN calculator            |")
print("|         3-Fancier RPN calculator            |")
print("|                                             |")
print("===============================================")
print()
choice=input("Your choice: ")

mystack=StackCalc()
myqueue=Queue()

if choice=="1": #////////////// Simple RPN calculator

    print("Welcome to the simple RPN calculator (enter 'quit' to quit)")
    while True:
        print("----------------------------------------------------------")
        print(mystack)
        prompt=input(">")    
        if prompt=="quit": break
        mystack.rpnCommand(prompt)

if choice=="2": #////////////// Fancy RPN calculator
    print("Welcome to the fancy RPN calculator (enter 'quit' to quit)")
    while True:
        print("----------------------------------------------------------")
        print(mystack)
        if not myqueue.isEmpty(): #Display both postfix and infix
            print("Postfix: "+str(myqueue))
            print("Infix: ",StackCalc.postfix2infix(myqueue))

        prompt=input(">")
        if prompt=="":continue            #<-Prevents accidental blank-input from being processed (not required)
        if prompt=="^":prompt="**"        #<-This is more for eval(), as ^ isnt supported, but I figured
        if prompt=="quit": break          #adding it here makes it act more consistently across modes
        mystack.rpnCommand(prompt)

        if prompt!="flush":
            myqueue.enqueue(prompt)
        else:
            myqueue.flush()


if choice=="3": #////////////// Fancier RPN calculator
    print("Welcome to the fancier RPN calculator (enter ’quit’ to quit)")
    userInputX=""               #userInputX is always replaced before
                                #running again, so it can be set once here
    while True:        
        print("----------------------------------------------------------")
        if not myqueue.isEmpty(): # Display both postfix and infix
            print("Postfix: "+str(myqueue))
            print("Infix: "+StackCalc.postfix2infix(myqueue))
        prompt=input(">")
        if prompt=="":continue    
        if prompt=="^":prompt="**"        # Same as optn. 2
        if prompt=="quit": break 

        if prompt=="run":
            if myqueue.find("x") is True:                   # If run, get x value from user, set post2in to the 
                userInputX=input("Enter x value: ")         #result of postfix2infix except replace the x with userinput
            post2in=StackCalc.postfix2infix(myqueue).replace("x",userInputX)
            print("Solution using infix:",eval(post2in))    #then evaluate it
            print("Solution using postfix:",StackCalc.evaluate_postfix(myqueue,userInputX))
            continue #skip to next iteration, as "run" shouldnt be pushed to queue

        if prompt=="plot":
            post2in=StackCalc.postfix2infix(myqueue) # x 1 -  x-1
            usrInp=input("Enter values of xmin, xmax, nbp: ").strip(" ") #strips any leading or ending spaces if needed
            usrInp=usrInp.split()                       # Make it a list,
            xmin,xmax,nbp=usrInp[0],usrInp[1],usrInp[2] #set xmin/max/nbp to input

            x=np.linspace(float(xmin),float(xmax),int(nbp)) # Gets all values of x to be plotted
            plt.plot(x,eval(post2in))                       # eval(post2in) allows post2in to be 
            plt.ylabel("f(x)")                              #interpreted by plt.plot() correctly
            plt.xlabel("x")
            plt.title("f(x)="+str(post2in))                 # Add labels, then show to user
            plt.show()
            continue

        if prompt!="flush":
            myqueue.enqueue(prompt)     # same code as optn. 2
        else:
            myqueue.flush()

print("Thanks for using the RPN calculator")
