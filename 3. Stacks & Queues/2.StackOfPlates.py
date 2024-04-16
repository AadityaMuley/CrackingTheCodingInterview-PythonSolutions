# Imagine a (literal) stack of plates. 
# If the stack gets too high, it might topple. 
# Therefore, in real life, we would likely start a new stack when the previous stack exceeds some threshold. 
# Implement a data structure SetOfStacks that mimics this. 
# SetOfStacks should be composed of several stacks and should create a new stack once the previous one exceeds capacity. 
# SetOfStacks.push() and SetOfStacks.pop() should behave identically to a single stack 
# (that is, pop() should return the same values as it would if there were just a single stack).
# FOLLOW UP
# ImplementafunctionpopAt(int index)which performs a pop operation on a specific sub-stack


print("Enter threshold value for each sub-stack:")
threshold = int(input())
stack = [[]]
curr_stack = 0

while True:
    print("Enter 1 for push, 2 for pop, 3 for pop a specific stack, 4 for print, anything else for exit:")
    sel = int(input())
    if sel == 1:
        if len(stack[curr_stack]) < threshold:
            stack[curr_stack].append(input())
        else:
            stack.append([])
            curr_stack += 1
            stack[curr_stack].append(input())
    elif sel == 2:
        stack[curr_stack].pop()
        if not stack[curr_stack]:
            stack.pop()
            curr_stack -= 1
    elif sel == 3:
        print("Enter stack num at which to pop:")
        stack[int(input()) - 1].pop()
    elif sel == 4:
        for i in stack:
            print(i)
    else:
        break
