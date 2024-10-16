## Restaurant Order Management 

**Objective:**  The aim of this assignment is to implement an order management system for a restaurant using stacks and queues.

**Problem Statement:** You have been tasked with developing an order management system for a busy restaurant to streamline the ordering process and improve customer satisfaction. The restaurant receives orders for food and drinks from customers, and the orders need to be processed and delivered efficiently. Your objective is to design and implement a system that uses a queue to address each of the orders, in order that they were placed.

**Task 1**

- Create an "Order" class which should include:

```py
class Order:

    def __init__(self, meals, table_number):
        self.meals = meals
        self.table_number= table_number
        self.next = None
    
```

**Task 2**

- Create a "Kitchen" class which should include the following methods:

1. add_order() - adds order to kitchen queue

```py
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



orders = Kitchen()

default_message()
orders.enqueue("Hotdog")
orders.enqueue("Red snapper fish and Rice")   
orders.enqueue("Hamburger")
orders.enqueue("12pc wings")



```

2. cook_order() - removes order from the queue

```py
class Kitchen:

    def __init__(self):
        self.head = None
        self.tail = None

    def dequeue(self):
        if self.head == None:
            return "No order found"
        else:
            removed = self.head
            self.head =removed.next
            print(f"{removed.data} is being cook")

orders = Kitchen()

orders.dequeue()
```

3. view_orders() - should print out all the orders

```py
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

    

orders = Kitchen()

orders.enqueue("Hotdog")
orders.enqueue("Red snapper fish and Rice")   
orders.enqueue("Hamburger")
orders.enqueue("12pc wings")

orders.traverse()

```