
class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None
    def __repr__(self):
        return self.data.__repr__()

class BSTNode:
    def __init__(self, data, parent_node=None):
        self.data = data
        self.right_node = None
        self.left_node = None
        self.parent_node = parent_node
    def __repr__(self):
        return self.data.__repr__()

class BinarySearchTree:
    def __init__(self):
        self.root_node = None
    
    # the method finds the lowest point in the tree while recervivily calling (prints it) and then goes up the tree until it reaches the highest point so that as the stack clears it (when no lower points can be called) it prints lowest to highest. 
    def print_tree(self):
        if self.root_node is not None:
            self.print_in_order(self.root_node)

    def print_in_order(self, node):
        if node.left_node is not None:
            self.print_in_order(node.left_node)
        print(node)
        if node.right_node is not None:
            self.print_in_order(node.right_node)

    # def __repr__(self):
    #     output = ""
    #     if self.root_node is not None:
    #         self.print_in_order(self.root_node)
    #     return output

    # the methods finds where in the tree the inserted data is no longer smaller/bigger than the node to its left/right by recursively calling itself
    # once the spot it finds is none it is pointed to by the node above it 
    def insert(self, data):
        new_node = BSTNode(data)
        if self.root_node is None:
            self.root_node = new_node
        else:
            self.insert_node(data, self.root_node)

    def insert_node(self, data, node):
        if data.abbr < node.data.abbr:
            if node.left_node is not None:
                self.insert_node(data, node.left_node)
            else:
                node.left_node = BSTNode(data, node)
        else:
            if node.right_node is not None:
                self.insert_node(data, node.right_node)
            else:
                node.right_node = BSTNode(data, node)
    
    def get_min(self):
        temp_node = self.root_node
        while temp_node.left_node is not None:
            temp_node = temp_node.left_node
        return temp_node.data

    def get_max(self):
        temp_node = self.root_node
        while temp_node.right_node is not None:
            temp_node = temp_node.right_node
        return temp_node.data
    
    def get_max_node_from_data(self, node):
        temp_node = node
        while temp_node.right_node is not None:
            temp_node = temp_node.right_node
        return temp_node

    def get(self, data):
    # returns the object with that title
        return self.get_node(data, self.root_node)

    def get_node(self, data, node):
    # This is the helper method
        if node is None or data == node.data.abbr:
            return node
        if data < node.data.abbr:
            return self.get_node(data, node.left_node)
        else:
            return self.get_node(data, node.right_node)

     # i coded this myself and i feel like that explains how over complicated it is ;-;
     # this method will remove the node that has the same data as the data passed and replace it with the node that would come before it in the list
     # the passed data is marked as the node to be removed
     # the method finds the node that is suppose to replace the removed node by useing the get_max_node_from_data methods which finds the predicersor to the node trying to be removed.
     # all the pointers from the removed node is given to the new node depending on the case this is exucuted slightly differently but the resualts are similar
    def remove_node(self, data):
        remove_node = self.get(data)

        if remove_node is self.root_node:
                self.root_node = remove_node

        if remove_node.left_node is None and remove_node.right_node is None:
            if remove_node.parent_node.left_node is remove_node:
                remove_node.parent_node.left_node = None
                return remove_node
            if remove_node.parent_node.right_node is remove_node:
                remove_node.parent_node.right_node = None
                return remove_node
        else:
            if remove_node.left_node is None:
                if remove_node.parent_node.left_node is remove_node: remove_node.parent_node.left_node = remove_node.right_node
                elif remove_node.parent_node.right_node is remove_node: remove_node.parent_node.right_node = remove_node.right_node
                remove_node.right_node.parent_node = remove_node.parent_node
                return remove_node
            if remove_node.right_node is None:
                if remove_node.parent_node.left_node is remove_node: remove_node.parent_node.left_node = remove_node.left_node
                elif remove_node.parent_node.right_node is remove_node: remove_node.parent_node.right_node = remove_node.left_node
                remove_node.left_node.parent_node = remove_node.parent_node
                return remove_node
            if remove_node.left_node is not None and remove_node.right_node is not None:
                switch_node = self.get_max_node_from_data(remove_node.left_node)
                if remove_node.parent_node.left_node is remove_node: remove_node.parent_node.left_node = switch_node
                elif remove_node.parent_node.right_node is remove_node: remove_node.parent_node.right_node = switch_node
                if switch_node is not remove_node.left_node: switch_node.left_node = remove_node.left_node
                elif switch_node is not remove_node.right_node: switch_node.right_node = remove_node.right_node
                switch_node.parent_node = remove_node.parent_node
                return remove_node

        

class LinkedList:
    def __init__(self):
        self.head_node = None
        self.tail_node = None # optional
        self.num_of_nodes = 0 # optional
    
    def __iter__(self):
        temp_node = self.head_node
        while temp_node is not None:
            yield temp_node.data
            temp_node=temp_node.next_node

    def __repr__(self):
        output = "LinkedList: \n"
        temp_node = self.head_node 
        while temp_node is not None:
            output += f"{temp_node.__repr__()} \n"
            temp_node = temp_node.next_node
        return output

    def insert_at_start(self, data):
        new_node = Node(data)
        self.num_of_nodes += 1
        if self.head_node is None:
            self.head_node = new_node
            self.tail_node = new_node
        else:
            new_node.next_node = self.head_node
            self.head_node = new_node

    def append(self, data):
        new_node = Node(data)
        self.num_of_nodes += 1

        if self.head_node is None:
            self.head_node = new_node
            self.tail_node = new_node
        else:
            self.tail_node.next_node = new_node
            self.tail_node = new_node

    def insert_after(self, new_data, data):
        if self.head_node is None:
            self.head_node = new_node
            self.tail_node = new_node
        else:
            new_node = Node(new_data)
            old_node = self.head_node
            while old_node.next_node is not None and old_node.data != data:
                old_node = old_node.next_node
            if (old_node.next_node is None):
                self.tail_node = new_node
            new_node.next_node = old_node.next_node
            old_node.next_node = new_node
        
    def remove(self, data):
        if self.head_node is None:
            return
        if self.head_node.data == data:
            temp_node = self.head_node
            self.head_node = self.head_node.next_node
            del temp_node
            self.num_of_nodes -= 1
        else:
            remove_node = self.head_node
            while remove_node.next_node is not None and remove_node.data != data:
                previous_node = remove_node
                remove_node = remove_node.next_node

            if remove_node.data != data:
                return

            previous_node.next_node = remove_node.next_node

            del remove_node
            self.num_of_nodes -= 1
        
class Stack:
    def __init__(self):
        self.top_node = None
        self.num_of_nodes = 0

    def __iter__(self):
        temp_node = self.top_node
        while temp_node is not None:
            yield temp_node.data
            temp_node=temp_node.next_node

    def __repr__(self):
        output = "\n"
        temp_node = self.top_node 
        while temp_node is not None:
            output += f"{temp_node.__repr__()} \n"
            temp_node = temp_node.next_node
        return output

    def push(self, data):
        new_node = Node(data)
        self.num_of_nodes += 1

        if self.top_node is None:
            self.top_node = new_node
        else:
            new_node.next_node = self.top_node
            self.top_node = new_node

    # this method is used to remove the top node in the stack
    # the pop methods takes the top node and removes it making sure that the next node (the node thre top node is currently pointing at) knows it is now the top node    
    def pop(self):
        if self.top_node is None:
            return
        else:
            temp_node = self.top_node
            self.top_node = self.top_node.next_node
            self.num_of_nodes -= 1
            return temp_node.data

class Queue:
    def __init__(self):
        self.front_node = None
        self.rear_node = None
        self.num_of_nodes = 0
    
    def __iter__(self):
        temp_node = self.front_node
        while temp_node is not None:
            yield temp_node.data
            temp_node=temp_node.next_node

    def __repr__(self):
        output = "\n"
        temp_node = self.front_node 
        while temp_node is not None:
            output += f"{temp_node.__repr__()} \n"
            temp_node = temp_node.next_node
        return output

    # this method adds new data to the queue
    # this method takes the tail node of the queue which is saved as a instance variable removes it (and points it twords the new node) and makes the next node the new tail node 
    def push(self, data):
        new_node = Node(data)
        self.num_of_nodes += 1
        if self.front_node is None:
            self.front_node = new_node
            self.tail_node = new_node
        else:
            self.tail_node.next_node = new_node
            self.tail_node = new_node

    def pop(self):
        if self.front_node is None:
            return
        else:
            temp = self.front_node
            self.front_node = self.front_node.next_node
            self.num_of_nodes -= 1
            return temp.data

if __name__ == '__main__':
    my_list = BinarySearchTree()

    my_list.insert(60)
    my_list.insert(34)
    my_list.insert(45)
    my_list.insert(21)
    my_list.insert(46)
    my_list.insert(63)
    # print(my_list.get(45))
    print("removed:")
    print(my_list.remove_node(60))

    print("Tree:")
    my_list.print_tree()
    # print(my_list.get_min())
    # print(my_list.get_max())