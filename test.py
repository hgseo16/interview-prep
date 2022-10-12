# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        length = 0
        end = head

        # finds length of ll
        while end:
            end = end.next
            length += 1

        # edge cases
        if length == 0 or length == 1:
            return True

        # finds mid index of ll
        mid = length // 2

        rev_mid_pointer = head

        # rev_mid_pointer points to mid of the ll
        for i in range(mid):
            rev_mid_pointer = rev_mid_pointer.next

        print(rev_mid_pointer.val)
        def reverse_ll(mid):
            reved = None
            while mid:
                nx = mid.next
                mid.next = reved
                reved = mid
                mid = nx
            return reved

        ptr1 = head
        ptr2 = reverse_ll(rev_mid_pointer)

        while ptr1 and ptr2:
            if ptr1.val != ptr2.val:
                return False
            ptr1 = ptr1.next
            ptr2 = ptr2.next

        return True

node1 = ListNode()
node2 = ListNode()
node3 = ListNode()
node4 = ListNode()
node1.val = 1
node2.val = 1
node3.val = 2
node4.val = 1

node1.next = node2
node1.next.next = node3
node1.next.next.next = node4

while node1:
    print(node1.val)
    node1 = node1.next

# solution = Solution()
# print(solution.isPalindrome(node1))