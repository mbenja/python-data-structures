from Node import Node

class Queue(object):
    'Generic Queue class'

    """
    @param t_front: node to become front of queue
    """
    def __init__(self, t_front=Node()):
        self.front = t_front
        self.size = 0

    """
    @param t_node: the node to be enqueued
    """
    def enqueue(self, t_node):
        if self.front.value == None:
            self.front = t_node
        else:
            current_node = self.front
            while current_node.next != None:
                current_node = current_node.next
            current_node.next = t_node
        self.size += 1

    """
    dequeues the node at the front of the queue
    """
    def dequeue(self):
        if self.front.value == None:
            print('Queue is already empty, front node not removed.')
        else:
            self.front = self.front.next
            self.size -= 1

    """
    returns node value at the front of the queue
    """
    def peek(self):
        return self.front.value

    """
    prints value of each node in queue
    """
    def printQueue(self):
        current_node = self.front
        while current_node.next != None:
            print(current_node.value)
            current_node = current_node.next
