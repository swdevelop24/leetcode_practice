# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1, list2) :
        head = ListNode(-1)
        tail = head
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2

        return head.next
        
        
        
'''
    def stringify_list(node):
        result = []
        current = node
        while current:
            result.append(str(current.val))  # 현재 노드의 값을 문자열로 변환하여 리스트에 추가
            current = current.next  # 다음 노드로 이동
        return " -> ".join(result)  # '->'로 각 노드를 이어붙여서 반환

list1 = ListNode(1, ListNode(2, ListNode(4)))
list2 = ListNode(1, ListNode(3, ListNode(4)))
sol = Solution()
print(stringify_list(sol.mergeTwoLists(list1, list2)))
'''