class Node:
    def __init__(self , data = 0 , next =None):
        self.data = data
        self.next  = next

class stack:
    def __init__(self):
        self.top = None

    def Push(self):
        new_node = Node(int(input("Enter Push element: ")))
        if self.top == None :
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        print("element pushed successfully")

    def Pop(self):
        if self.top == None:
            print("stack is empty")
        else:
            popped = self.top.data
            self.top = self.top.next
        print("element pop successfully")

    def Peek(self):
        if self.top == None:
            print("Stack is Empty")
        else:
            print("peek of the Stack",self.top.data)
        
    def Display(self):
        if self.top == None:
            print("Stack is empty:")
        else:
            t = self.top
            while t:
                print(t.data , end=' ->')
                t = t.next
            print("None")

Stack = stack()

while True:
    print("Menu: ")
    print("1.Push the Element")
    print("2.pop the element")
    print("3.Peek of the stack")
    print("4.Display")
    print("5.Exit")

    choice = int(input("Enter Your Choice: "))
    match (choice):
        case 1:
            Stack.Push()
        case 2:
            Stack.Pop()
        case 3:
            Stack.Peek()
        case 4:
            Stack.Display()
        case 5:
            exit(0)
