class BinarySearchTreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        
    def add_child(self, data):
        if data == self.data:
            return # if the node already exist
        
        # If data is less than the value of current node --goes to left subtree
        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        # If data is greater than the value of current node --goes to right subtree
        else:
            if self.right:
                self.right.add_child(data) 
            else:
                self.right = BinarySearchTreeNode(data)
                
    def in_order_traversal(self):
        elements = []

        #Visit the left tree
        if self.left:
            elements += self.left.in_order_traversal()

        #Visit base node
        elements.append(self.data)

        #Visit the right tree
        if self.right:
            elements += self.right.in_order_traversal()
            
        return elements

    def search (self, val):
        if self.data == val:
            return True
        
        if val < self.data:
            #value should be in left subtree
            if self.left:
                return self.left.search(val)
            else:
                return False #means the value does not exist in the elements
        if val > self.data:
            #value should be in right subtree
            if self.right:
                return self.right.search(val)
            else:
                return False #means the value does not exist in the elements
            
    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()
        
def build_tree(elements):
    print("Building tree with these elements:",elements)
    root = BinarySearchTreeNode(elements[0])

    for i in range(1,len(elements)):
        root.add_child(elements[i])

    return root
        
if __name__ == '__main__':
    numbers = [17, 4, 1, 20, 9, 23, 18, 34]