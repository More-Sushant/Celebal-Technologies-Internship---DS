# Node class for creating an empty node and add data in it
# Adding data is done using parameters. If you have to do manually then you have to use INPUT function which was used in previous assignment.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Class for singly LL is created here 
class LinkedList:
    def __init__(self):
        self.head = None

    # Function for adding new node
    def add_node(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next

        current.next = new_node

    # function for printing LL
    def print_list(self):
        if self.head is None:
            print("\nEmpty LL")
            return

        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    # Deleting nth node in the list. 1-based index is used as mentioned.
    def delete_nth_node(self, n):
        if self.head is None:
            print("\nYou cannot delete empty LL")
            return

        if n <= 0:
            print("\nPlease provide a positive number/index")
            return

        
        if n == 1:
            deleted_value = self.head.data
            self.head = self.head.next
            print(f"\nDeleted node at position {n} with value: {deleted_value}")
            return

        current = self.head
        previous = None
        count = 1


        while current and count < n:
            previous = current
            current = current.next
            count += 1

        if current == None:
            print("\nNo node found to delete.")
            return
            

        delete_value = current.data
        previous.next = current.next
        print(f"\nDeleted node at position {n} having value: {delete_value}")


# Creating object 
my_list = LinkedList() 

# Adding elements
my_list.add_node(10)
my_list.add_node(20)
my_list.add_node(30)
my_list.add_node(40)

# Printing Linked list
print("\nInitial LL:")
my_list.print_list()

# Deleting 2nd node
try:
    my_list.delete_nth_node(3)
    print("\nAfter deleting the node 3:")
    my_list.print_list()
except Exception as e:
    print(e)

# Deleting from empty list
empty_list = LinkedList()
try:
    empty_list.delete_nth_node(1)
except Exception as e:
    print(e)

print("\n")