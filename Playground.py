# Implement a linked list
class Node:
    def __init__(self, value, next=None) -> None:
        self.val = value
        self.next = next


n1 = Node(11)
n2 = Node(23)
n3 = Node(341)


n1.next = n2
n2.next = n3

curr = n1
while curr:
    print(curr.val)
    curr = curr.next
