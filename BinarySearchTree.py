from Node import Node

class BinarySearchTree(object):
    'Generic Binary Search Tree class'

    """
    @param t_root: the node to be placed at root of the tree
    """
    def __init__(self, t_root=Node()):
        self.root = t_root

    """
    @param t_current_node: the node currently being looked at in the tree
    """
    def findMinimum(self, t_current_node):
        if t_current_node.left != None:
            return self.findMinimum(t_current_node.left)
        else:
            return t_current_node

    """
    @param t_current_node: the node currently being looked at in the tree
    """
    def findMaximum(self, t_current_node):
        if t_current_node.right != None:
            return self.findMaximum(t_current_node.right)
        else:
            return t_current_node

    """
    @param t_node: the node to be placed in the tree
    """
    def addNode(self, t_node):
        if self.root.value == None:
            self.root = t_node
        else:
            insertionPoint = self.searchForInsertionPoint(t_node, self.root)
            if insertionPoint.value < t_node.value:
                insertionPoint.right = t_node
            elif insertionPoint.value > t_node.value:
                insertionPoint.left = t_node

    """
    @param t_node: the node value to be deleted from the tree
    """
    def deleteNode(self, t_value):
        print("in delete node")
        found_node = self.searchForNodeByValue(t_value, self.root)
        if found_node == "Node not found.":
            print("Node not found.")
        else:
            if found_node.left != None and found_node.right != None:
                print("node has two children")
                successor = self.findMinimum(found_node.right)
                found_node.value = successor.value
                if successor.right != None:
                    found_node.right.left = successor.right
            elif found_node.left != None:
                print("node only has left child")
                found_node = found_node.left
            elif found_node.right != None:
                print("node only has right child")
                found_node = found_node.right
            else:
                print("found node doesn't have children")
                found_node = None

    """
    @param t_value: the value to search for in the tree
    @param t_current_node: the node currently being looked at in the tree
    """
    def searchForNodeByValue(self, t_value, t_current_node):
        if t_value == t_current_node.value:
            return t_current_node
        elif t_value < t_current_node.value:
            if t_current_node.left == None:
                return "Node not found."
            else:
                return self.searchForNodeByValue(t_value, t_current_node.left)
        else:
            if t_current_node.right == None:
                return "Node not found."
            else:
                return self.searchForNodeByValue(t_value, t_current_node.right)

    """
    @param t_new_node: the node to be placed in the tree
    @param t_current_node: the node currently being looked at in the tree
    """
    def searchForInsertionPoint(self, t_new_node, t_current_node):
        if t_current_node == None:
            return t_current_node
        if t_new_node.value <= t_current_node.value:
            if t_current_node.left == None:
                return t_current_node
            else:
                return self.searchForInsertionPoint(t_new_node, t_current_node.left)
        else:
            if t_current_node.right == None:
                return t_current_node
            else:
                return self.searchForInsertionPoint(t_new_node, t_current_node.right)

    """
    @param t_current_node: the node currently being looked at in the tree
    """
    def traverseTree(self, t_current_node):
        if self.root.value == None:
            print('Tree is empty.')
            return
        if t_current_node == None:
            return
        self.traverseTree(t_current_node.left)
        self.callback(t_current_node)
        self.traverseTree(t_current_node.right)

    """
    @param t_node: the node to callback on
    """
    def callback(self, t_node):
        print(t_node.value)
