class BinarySearchTreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
    
    def add_child(self,data):
        if self.data == data:
            return
        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)
    
    def delete(self,val):
        if val < self.data and self.left:
            self.left = self.left.delete(val)
        elif val > self.data and self.right:
            self.right = self.right.delete(val)
        else:
            if val == self.data:
                if self.right is None and self.left is None:
                    return None
                if self.left is None:
                    return self.right
                if self.right is None:
                    return self.left
                min_val = self.right.minimum_finder()
                self.data = min_val
                self.right = self.right.delete(min_val)
            else:
                print("Given Number is not present in the tree")
        
        return self
        
    def in_order_traversal(self):
        elements = []
        if self.left:
            elements+=self.left.in_order_traversal()
        elements.append(self.data)
        if self.right:
            elements+=self.right.in_order_traversal()
        return elements
    
    def pre_order_traversal(self):
        elements = []
        elements.append(self.data)
        if self.left:
            elements+=self.left.pre_order_traversal()
        if self.right:
            elements+=self.right.pre_order_traversal()
        return elements
    
    def post_order_traversal(self):
        elements = []
        if self.left:
            elements+=self.left.pre_order_traversal()
        if self.right:
            elements+=self.right.pre_order_traversal()
        elements.append(self.data)
        return elements
    
    def minimum_finder(self):
        if self.left:
            return self.left.minimum_finder()
        return self.data
    
    def maximum_finder(self):
        if self.right:
            return self.right.maximum_finder()
        return self.data
    
def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])
    for i in range(1,len(elements)):
        root.add_child(elements[i])
    return root
    
if __name__=='__main__':
    numbers = [13,4,1,9,20,18,17,19,23,34]
    number_tree = build_tree(numbers)
    print(number_tree.in_order_traversal())
    print(number_tree.pre_order_traversal())
    print(number_tree.post_order_traversal())
    print(number_tree.minimum_finder())
    print(number_tree.maximum_finder())
    number_tree.delete(20)
    print(number_tree.in_order_traversal())