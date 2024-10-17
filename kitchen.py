from helper import default_message

class Order:

    def __init__(self, meals, table_number):
        self.meals = meals
        self.table_number= table_number
        self.next = None

class Kitchen:

    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, meals, table_number):
        new_node = Order(meals, table_number)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def traverse(self):
        current = self.head
        while current:
            print(f"{current.meals} for {current.table_number}")
            current =current.next

    def dequeue(self):
        if self.head == None:
            return "No order found"
        else:
            removed = self.head
            self.head =removed.next
            print(f"{removed.meals} for {removed.table_number} is being cook")

    
orders = Kitchen()

default_message()
orders.enqueue("Hotdog","Table: 1")
orders.enqueue("Red snapper fish and Rice","Table: 2")   
orders.enqueue("Hamburger","Table: 3")
orders.enqueue("12pc wings","Table: 4")

orders.traverse()

print("*"*60)


orders.dequeue()


print("*"*60)

default_message()
orders.traverse()



