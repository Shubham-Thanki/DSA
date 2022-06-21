# list1 = [1,2,4]
# list2 = [1,3,4]


class Node:
    def __init__(self, data=None, next=None) -> None:
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def insert_at_begining(self, data):
        node = Node(data, self.head)
        self.head = node
        # print(self.head)

    def insert_at_end(self, data):
        if self.head is None:
            node = Node(data, None)
            self.head = node
            return

        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None)

    def print(self):
        if self.head is None:
            print("Linked List is empty")
            return

        itr = self.head
        llstr = ''

        while itr:
            llstr += str(itr.data)+' --> '
            itr = itr.next

        print(llstr)

    def mergeTwoLists(self, list1, list2):
        p1 = list1.head
        p2 = list2.head
        while p1 and p2:
            if p1.data > p2.data:
                self.insert_at_end(p2.data)
                p2 = p2.next
            else:
                self.insert_at_end(p1.data)
                p1 = p1.next

        itr = self.head
        while itr.next:
            itr = itr.next
        if p1:
            itr.next = p1
        elif p2:
            itr.next = p2


list1 = LinkedList()
list1.insert_at_begining(12)
list1.insert_at_begining(8)
list1.insert_at_begining(6)
list1.print()


list2 = LinkedList()
list2.insert_at_begining(9)
list2.insert_at_begining(7)
list2.insert_at_begining(5)
list2.print()


list3 = LinkedList()
# list3.insert_at_begining('x')
# list3.insert_at_end(25)
# list3.insert_at_end(56)
# list3.print()
list3.mergeTwoLists(list1, list2)
list3.print()


# -----------------------------------------------------------------------------------------------
# https://leetcode.com/problems/merge-two-sorted-lists/
# LEETCODE SOLUTION
# # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
#         dummy=ListNode()
#         tail=dummy

#         while list1 and list2:
#             if list1.val<list2.val:
#                 tail.next=list1
#                 list1=list1.next
#             else:
#                 tail.next=list2
#                 list2=list2.next
#             tail=tail.next

#         if list1:
#             tail.next=list1
#         elif list2:
#             tail.next=list2

#         return dummy.next
