class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

def find_sum(head):
    stack = []
    while head:
        # implement this
        stack.append(head)
        head = head.next

    sum_, index = 0, 1
    while stack:
        # implement this
        node = stack.pop()
        if index == 3:
            sum_ += node.data
        index += 1
    return sum_

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
print(find_sum(head))
head.next.next.next = Node(4)
print(find_sum(head))
head.next.next.next.next = Node(5)
print(find_sum(head))
