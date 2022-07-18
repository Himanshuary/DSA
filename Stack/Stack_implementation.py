# Creating Stack

def Creating_stack():
    stack = []
    return stack

# check Stack empty or not 

def check_empty(stack):
    if len(stack) == 0:
        return "Stack is empty"

# Adding a element in the stack
# or Push operation

def push(stack, value):
    stack.append(value)
    
# Removing a element in the stack
# Or pop operation

def pop(stack):
    stack.pop()
   
stack = Creating_stack()
push(stack, 1) 
push(stack, 2) 
push(stack, 3) 
push(stack, 4)
print("The element is pop from the stack is: ", pop(stack))
print("Stack is: ", stack) 