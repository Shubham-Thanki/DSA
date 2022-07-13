class MyQueue:

    # constructor
    def __init__(self):
        self.queue = list()
        self.maxSize = 100005
        self.head = 0
        self.tail = 0

    # Function to push an element x in a queue.
    def push(self, data):

        # checking if the queue is full and returning proper message.
        if self.size() >= self.maxSize:
            return ("Queue Full")

        # inserting data in the queue at tail.
        self.queue.append(data)
        self.tail += 1
        return

    # Function to pop an element from queue and return that element.
    def pop(self):

        # checking if the queue is empty and returning -1 if it is already empty.
        if self.size() <= 0:
            self.resetQueue()
            return -1

        data = self.queue[self.head]
        self.head += 1

        # else we return the element at front.
        return data

    def size(self):
        return self.tail - self.head

    def resetQueue(self):
        self.tail = 0
        self.head = 0
        self.queue = list()
