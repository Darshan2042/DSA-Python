#Implement a queue using two stacks.


class QueueUsingStacks:
    def __init__(self):
        self.stack1 = [] 
        self.stack2 = []  

    def enqueue(self, item):
        self.stack1.append(item)

    def dequeue(self):
        if not self.stack1 and not self.stack2:
            return "Queue is empty"
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()

    def display(self):
        if not self.stack1 and not self.stack2:
            print("Queue is empty")
            return
        temp = self.stack2[::-1] + self.stack1
        print("Queue:", temp)
queue = QueueUsingStacks()
while True:
    print("\n1. Enqueue")
    print("2. Dequeue")
    print("3. Display")
    print("4. Exit")

    ch = int(input("Enter your choice: "))
    match ch:
        case 1:
            item = input("Enter element to enqueue: ")
            queue.enqueue(item)
        case 2:
            print("Dequeued:", queue.dequeue())
        case 3:
            queue.display()
        case 4:
            exit()
