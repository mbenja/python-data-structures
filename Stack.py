from Node import Node

class Stack(object):
    'Generic Stack class'

    """
    @param t_top: base node for the stack
    """
    def __init__(self, t_top=Node()):
        self.top = t_top
        self.size = 0

    """
    @param t_node: node to push to top of stack
    """
    def push(self, t_node):
        if self.top.value == None:
            self.top = t_node
        else:
            t_node.next = self.top
            self.top = t_node
        self.size += 1

    """
    pops top node off of stack
    """
    def pop(self):
        if self.top.value == None:
            print('Stack is already empty, top node not popped.')
        else:
            self.top = self.top.next
            self.size -= 1

    """
    peeks at top node of stack
    """
    def peek(self):
        return self.top.value

    """
    prints value of each node in stack
    """
    def printStack(self):
        current_node = self.top
        while current_node.next != None:
            print(current_node.value)
            current_node = current_node.next
