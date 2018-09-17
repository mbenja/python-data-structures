from Node import Node

class LinkedList(object):
    'Generic Linked List class'

    """
    @param t_head: the node to be set as head node in the linked list
    """
    def __init__(self, t_head=Node()):
        self.head = t_head
        self.size = 0

    """
    @param t_node: the node to be set as first node in the linked list
    """
    def addHead(self, t_node):
        if self.head.value == None:
            self.head = t_node
        else:
            t_node.next = self.head
            self.head = t_node
        self.size += 1

    """
    @param t_node: the node to be set as next node at the end of the linked list
    """
    def addTail(self, t_node):
        if self.head.value == None:
            self.head = t_node
        else:
            current_node = self.head
            while current_node.next != None:
                current_node = current_node.next
            current_node.next = t_node
        self.size += 1

    """
    @param t_node: the node to be set at the specified index of the linked list
    @param t_index: the index at which to set the node
    """
    def insertNode(self, t_node, t_index):
        if t_index == 0:
            addNodeStart(t_node)
        elif t_index == self.size:
            addNodeEnd(t_node)
        elif t_index < 0 or t_index > self.size:
            print('Specified index is out of bounds of linked list. Node not inserted.')
        else:
            current_index = 0
            current_node = self.head
            while current_index != t_index - 1:
                current_node = current_node.next
                current_index += 1
            t_node.next = current_node.next
            current_node.next = t_node
            self.size += 1

    """
    removes node from head of linked list
    """
    def removeHead(self):
        if self.head.value == None:
            print('Linked list is already empty, head node not removed.')
        else:
            self.head = self.head.next
            self.size -= 1

    """
    removes node from tail of linked list
    """
    def removeTail(self):
        if self.size == 0:
            print('Linked list is already empty, head node not removed.')
        else:
            current_index = 0
            current_node = self.head
            while current_index != self.size - 2:
                current_node = current_node.next
                current_index += 1
            current_node.next = None
            self.size -= 1

    """
    @param t_index: the index at which to remove a node
    """
    def removeNode(self, t_index):
        if t_index == 0:
            removeHead()
        elif t_index == self.size:
            removeTail()
        else:
            current_index = 0
            current_node = self.head
            while current_index != t_index - 1:
                current_node = current_node.next
                current_index += 1
            current_node.next = current_node.next.next
            self.size -= 1

    """
    prints value of each node in linked list
    """
    def printList(self):
        current_node = self.head
        while current_node.next != None:
            print(current_node.value)
            current_node = current_node.next
