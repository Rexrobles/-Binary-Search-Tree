#Create a demo using the letters in your fullname as the content of the binary tree.class BinarySearchTreeNode:
    
class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def add_child (self, data):
        if data == self.data:
            return  # if the node already exist

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
        
    def in_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.in_order_traversal()
        elements.append(self.data)
        if self.right:
            elements += self.right.in_order_traversal()
        return elements
    
    def post_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.post_order_traversal()
        if self.right:
            elements += self.right.post_order_traversal()
        elements.append(self.data)
        return elements
    
    def pre_order_traversal(self):
        elements = [self.data]
        if self.left:
            elements += self.left.pre_order_traversal()
        if self.right:
            elements += self.right.pre_order_traversal()
        return elements
    
    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()

    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()
    
    def calculate_sum(self):
        left_sum = self.left.calculate_sum() if self.left else 0
        right_sum = self.right.calculate_sum() if self.right else 0
        return self.data + left_sum + right_sum
    
    def delete (self, val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)
        else:
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.left

            max_val = self.left.find_max()
            self.data = max_val
            self.left = self.left.delete(max_val)

        return self
    
def build_tree(elements):
    print("Building tree with these elements:",elements)
    root = BinarySearchTreeNode(elements[0])

    for i in range(1,len(elements)):
        root.add_child(elements[i])

    return root

if __name__ == '__main__':
    my_name = (["R", "E", "X", "-", "I", "M", "M", "A", "N", "H", "R", "O","B", "L", "E", "S"])
    my_name_tree = build_tree(my_name)
    
    print("\nIn order traversal:",my_name_tree.in_order_traversal())
    print("\nPost order traversal:",my_name_tree.post_order_traversal())
    print("\nPre order traversal:",my_name_tree.pre_order_traversal())
    print("\nIs there letter E?",my_name_tree.search("E")) 
    print("\nIs there letter C?",my_name_tree.search("C")) 
    print("\nMinimum:",my_name_tree.find_min())
    print("\nMaximum:",my_name_tree.find_max())
    
    my_name = (["R", "E", "X", "-", "I", "M", "M", "A", "N", "H", "R", "O","B", "L", "E", "S"])
    my_name_tree = build_tree(my_name)
    my_name_tree.delete("O")
    print("\nAfter deleting O:", my_name_tree.in_order_traversal())