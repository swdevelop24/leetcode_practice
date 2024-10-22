# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow, fast = head, head
        prev = None

        # 중간 지점을 찾고 첫 번째 반을 반전
        while fast and fast.next:
            fast = fast.next.next
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp


        # prev는 첫 번째 반의 끝을 가리키고, slow는 두 번째 반의 시작을 가리킴
        maxi = 0

        # 두 개의 반을 비교하여 최대 쌍 합을 계산합니다.
        while slow:  # None이 아닐 때까지 반복합니다.
            maxi = max(maxi, slow.val + prev.val)
            slow = slow.next
            prev = prev.next

        return maxi