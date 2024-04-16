# Write a program to sort a stack such that the smallest items are on the top. 
# You can use an additional temporary stack, 
# but you may not copy the elements into any other data structure (such as an array). 
# The stack supports the following operations: push, pop, peek, and isEmpty.

def peek(stack):
    return stack[-1]

def pop(stack):
    return stack.pop()

def push(stack, item):
    if not stack:
        stack.append(item)
        return
    temp = []
    while True:
        if not stack:
            stack.append(item)
            while temp:
                stack.append(pop(temp))
            break
        if item > peek(stack):
            temp.append(pop(stack))
        else:
            stack.append(item)
            while temp:
                stack.append(pop(temp))
            break

def printStack(stack):
    for i in reversed(stack):
        print(i)


stack = []
while True:
    print("Enter 1 for push, 2 for pop, 3 for print, anything else for exit:")
    sel = int(input())
    if sel == 1:
        push(stack, int(input()))
    elif sel == 2:
        temp = pop(stack)
    elif sel == 3:
        printStack(stack)
    else:
        break
