class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

class LinkedList:
    def __init__(self):
       self.head = None
       self.size = 0

    def insert(self, value):
        if self.head is None:
            self.head = Node(value)
            self.tail = self.head
        else:
            new_node = Node(value)
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def insert_after(self, new_data, node_data):
        curr = self.head
        prev = None
        new_node = Node(new_data)
        while curr:
            if curr.data == node_data:
                prev = curr.next
                curr.next = new_node
                new_node.next = prev
                return
            prev = curr
            curr = curr.next
        if not curr:
            prev.next = new_node
        self.size += 1

    def delete(self, data):
        temp = self.head
        prev = None
        while temp:
            if temp.data == data:
                self.size -= 1
                if prev:
                    prev.next = temp.next
                else:
                    self.head = temp.next
                return
            prev = temp
            temp = temp.next

    def print(self):
        temp = self.head
        while temp is not None:
            print(temp.data, end=" => ")
            temp = temp.next
        print('END')


list = LinkedList()
list.insert(1)
list.insert(2)
list.insert(3)
list.print() # Output: 1 => 2 => 3 => END
list.delete(2)
list.print() # Output: 1 => 3 => END

list = LinkedList()
list.insert(1)
list.insert(2)
list.insert(3)
print("Size of the linked list after insertions: ", list.size)  # Expected output: Size of the linked list after insertions: 3
list.delete(2)
print("Size of the linked list after deletion: ", list.size)  # Expected output: Size of the linked list after deletion: 2

llist = LinkedList()

# Add nodes to the alien communication network
llist.insert("Zog")
# TODO: Insert a new node "Zak" after "Zog" in the alien communication network.
llist.insert_after("Zak", "Zog")

# Print the Alien Communication Network
llist.print()