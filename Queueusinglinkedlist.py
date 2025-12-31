class Node:
    def __init__(self ,data=0,next=None):
        self.data = data
        self.next = next
        
class queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self):
        new_node = Node(int(input("Enter Element: ")))
        if self.front == None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        print("element Enqueue")

    def dequeue(self):
        if self.front == None:
            print("Queue is Empty")
        else:
            deque = self.front.data
            self.front = self.front.next
        print("element Dequeue")

    def display(self):
        if self.front == None:
            print("queue is Empty")
        else:
            t = self.front
            while t:
                print(t.data , end=' ->')
                t=t.next
            print('None')


Queue = queue()

while True:
    print("Menu: ")
    print("1.Enqueue")
    print("2.dequeue")
    print("3.Display")
    print("4.Exit")

    choice = int(input("Enter choice: "))
    match(choice):
        case 1:
            Queue.enqueue()
        case 2:
            Queue.dequeue()
        case 3:
            Queue.display()
        case 4:
            exit(0)
