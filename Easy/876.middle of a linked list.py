"""
🔗 Problem: Middle of the Linked List

Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.

Examples:
---------

Input: head = [1, 2, 3, 4, 5]
Output: [3, 4, 5]
Explanation: The middle node is node 3.

Input: head = [1, 2, 3, 4, 5, 6]
Output: [4, 5, 6]
Explanation: The list has two middle nodes (3 and 4), so the second one (node 4) is returned.

Constraints:
------------
- The number of nodes in the list is in the range [1, 100]
- 1 <= Node.val <= 100
"""
#Solution

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow=fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        return slow
        