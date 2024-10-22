class ListNode:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None


class MyLinkedList:

    def __init__(self):
        self.head = ListNode(0)
        self.tail = ListNode(0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, index: int) -> int:
        cur = self.head.next
        while cur and index > 0:
            cur = cur.next
            index -= 1

        if cur and cur != self.tail and index == 0:
            return cur.val
        return -1

    def addAtHead(self, val: int) -> None:
        node, prev, next = ListNode(val), self.head, self.head.next
        node.next, node.prev = next, prev
        next.prev = node
        prev.next = node

    def addAtTail(self, val: int) -> None:
        node, prev, next = ListNode(val), self.tail.prev, self.tail
        node.next, node.prev = next, prev
        next.prev = node
        prev.next = node

    def addAtIndex(self, index: int, val: int) -> None:
        next = self.head.next
        while next and index > 0:
            next = next.next
            index -= 1

        if next and index == 0:
            node, prev = ListNode(val), next.prev
            node.next, node.prev = next, prev
            next.prev = node
            prev.next = node

    def deleteAtIndex(self, index: int) -> None:
        node = self.head.next
        while node and index > 0:
            node = node.next
            index -= 1

        if node and node != self.tail and index == 0:
            node.prev.next = node.next
            node.next.prev = node.prev

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)