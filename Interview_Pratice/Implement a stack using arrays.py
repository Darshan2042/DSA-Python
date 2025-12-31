#Implement a stack using arrays.

class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return "Stack is empty"
    
    def is_empty(self):
        return len(self.stack) == 0

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        return "Stack is empty"
    
    def display(self):
        print("Stack:", self.stack)

stack = Stack()

while True:
    print("1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Display")
    print("5. Exit")

    ch = int(input("Enter your choice: "))

    match ch:
        case 1:
            item = input("Enter element to push: ")
            stack.push(item)
            print("Pushed:", item)
        case 2:
            print("Popped:", stack.pop())
        case 3:
            print("Top element:", stack.peek())
        case 4:
            stack.display()
        case 5:
            print("Exiting...")
            break
        case _:
            print("Invalid choice! Try again.")




