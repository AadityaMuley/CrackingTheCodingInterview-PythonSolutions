# An animal shelter, which holds only dogs and cats, operates on a strictly"first in, first out" basis. 
# People must adopt either the"oldest" (based on arrival time) of all animals at the shelter, 
# or they can select whether they would prefer a dog or a cat (and will receive the oldest animal of that type). 
# They cannot select which specific animal they would like. 
# Create the data structures to maintain this system and implement operations such as 
# enqueue, dequeueAny, dequeueDog, and dequeueCat. 
# You may use the built-in Linked list data structure.

def enqueue(queue, animal):
    queue.append(animal)

def dequeueAny(queue):
    if not queue:
        return "No Animals available"
    return queue.pop(0)

def dequeueDog(queue):
    for a in queue:
        if a[0] == "D":
            animal = a
            queue.remove(a)
            return animal
    return "No Dogs available"

def dequeueCat(queue):
    for a in queue:
        if a[0] == "C":
            animal = a
            queue.remove(a)
            return animal
    return "No Cats available"


queue = []
dogCount = 0
catCount = 0
while True:
    print("Enter 1 for new animal, 2 for adopting any animal, 3 for adopting any Dog, 4 for adopting Cat, 5 for viewing all animals, anything else for exit:")
    sel = int(input())
    if sel == 1:
        animal = input()
        if animal == "D":
            dogCount += 1
            animal += str(dogCount)
            enqueue(queue, animal)
        elif animal == "C":
            catCount += 1
            animal += str(catCount)
            enqueue(queue, animal)
        else:
            print("Invalid entry")
    elif sel == 2:
        print("Congratulations you just adopted: ", dequeueAny(queue))
    elif sel == 3:
        print("Congratulations you just adopted: ", dequeueDog(queue))
    elif sel == 4:
        print("Congratulations you just adopted: ", dequeueCat(queue))
    elif sel == 5:
        for i in queue:
            print(i)
    else:
        break
