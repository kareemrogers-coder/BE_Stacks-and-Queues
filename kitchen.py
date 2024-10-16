from helper import default_message

class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

class Kitchen:

    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, order):
        new_node = Node(order)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def traverse(self):
        current = self.head
        while current:
            print(current.data)
            current =current.next

    def dequeue(self):
        if self.head == None:
            return "No order found"
        else:
            removed = self.head
            self.head =removed.next
            print(f"{removed.data} is being cook")

    
orders = Kitchen()

default_message()
orders.enqueue("Hotdog")
orders.enqueue("Fish and Chips")   
orders.enqueue("Hamburger")
orders.enqueue("12pc wings")

orders.traverse()

print("*"*60)


orders.dequeue()


print("*"*60)

default_message()
orders.traverse()



