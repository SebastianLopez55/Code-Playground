class ListNode:
    def __init__(self, val, next=None) -> None:
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def append(self, val) -> None:
        if self.head is None:
            self.head = ListNode(val)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = ListNode(val)

    def print_list(self) -> None:
        if self.head is None:
            print("Empty List")
        else:
            current = self.head
            while current:
                print(current.val)
                current = current.next
