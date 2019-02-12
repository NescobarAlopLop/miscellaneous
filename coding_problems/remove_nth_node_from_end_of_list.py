"""
Given a linked list, remove the n-th node from the end of list and return its head.

Example:

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.

Note:

Given n will always be valid.
"""
# Definition for singly-linked list.
import unittest
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        last_np = head
        last_ni = 0
        node_to_del_p = head
        node_to_del_idx = 0
        while last_np.next:
            last_np = last_np.next
            last_ni += 1
            if node_to_del_idx + n < last_ni:
                node_to_del_p = node_to_del_p.next
                node_to_del_idx += 1
        if node_to_del_p == head:
            head = head.next
        else:
            node_to_del_p.next = node_to_del_p.next.next
        return head


def create_linked_list_from_array(arr):
    head = ListNode(arr[0])
    node = head
    for val in arr[1:]:
        node.next = ListNode(val)
        node = node.next
    return head


class TestSolution(unittest.TestCase):
    def test_0(self):
        linked_list = create_linked_list_from_array(range(6))
        sol = Solution()
        linked_list = sol.removeNthFromEnd(linked_list, 2)
        test = []
        while linked_list:
            test.append(linked_list.val)
            linked_list = linked_list.next
        self.assertEqual(test, [0, 1, 2, 3, 5])

    def test_1(self):
        linked_list = create_linked_list_from_array(range(6))
        sol = Solution()
        linked_list = sol.removeNthFromEnd(linked_list, 6)
        test = []
        while linked_list:
            test.append(linked_list.val)
            linked_list = linked_list.next
        self.assertEqual(test, [1, 2, 3, 4, 5])

    def test_2(self):
        linked_list = create_linked_list_from_array(range(2))
        sol = Solution()
        linked_list = sol.removeNthFromEnd(linked_list, 1)
        test = []
        while linked_list:
            print(linked_list.val)
            test.append(linked_list.val)
            linked_list = linked_list.next
        self.assertEqual(test, [1])


if __name__ == '__main__':
    unittest.main()
