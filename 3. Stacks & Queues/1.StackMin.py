# How would you design a stack which, in addition to push and pop, 
# has a function min which returns the minimum element? 
# Push, pop and min should all operate in 0(1) time.

stack = []
currMin = 0
temp = False
while True:
    print("Enter any num to put on stack or # to stop:")
    inp = input()
    if inp == "#":
        break

    inp = int(inp)
    if currMin > inp or temp == False:
        currMin = inp
        temp = True
    
    stack.append([inp, currMin])

print("Final Stack with its min at every stage")
for i in stack:
    print(i)


# One solution is to have just a single int value, minValue, that's a member of the Stack class. 
# When minValue is popped from the stack, we search through the stack to find the new minimum. 
# Unfortunately, this would break the constraint that push and pop operate in 0(1) time.
# To further understand this question, let's walk through it with a short example:
# push(5); // stack is {5}, min is 5
# push(6); // stack is {6, 5}, min is 5
# push(3); // stack is {3, 6, 5}, min is 3
# push(7); // stack is {7, 3, 6, 5}, min is 3
# pop(); // pops 7. stack is {3, 6, 5}, min is 3
# pop(); // pops 3. stack is {6, 5}. min is 5.
# Observe how once the stack goes back to a prior state ({ 6, 5}), the minimum also goes back to its prior state (5). 
# This leads us to our second solution.
# If we kept track of the minimum at each state, we would be able to easily know the minimum. 
# We can do this by having each node record what the minimum beneath itself is. 
# Then, to find the min, you just look at what the top element thinks is the min.