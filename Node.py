class Node(object):
    'Generic Node class, designed for data structures such as Linked Lists, Stacks, Queues, and Binary Trees.'

    """
    @param t_value: the value to be placed inside the node
    @param t_next: the next node this node is connected to
    @param t_left: the node to the left
    @param t_right: the node to the right
    """
    def __init__(self, t_value=None, t_next=None, t_left=None, t_right=None):
        self.value = t_value
        self.next = t_next
        self.left = t_left
        self.right = t_right
