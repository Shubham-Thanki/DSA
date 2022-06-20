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

    def rever(self):
        cur = self.head
        prev = None
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp

        self.head = prev
        LinkedList.print(self)


ll = LinkedList()
ll.insert_at_begining(5)
ll.insert_at_begining(9)
ll.insert_at_begining(12)
ll.print()
# ll.insert_at_begining(15)
ll.rever()
