class Node:
    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.left = None
        self.right = None
    
    def inorder(self):
        traversal = []
        if self.left:
            traversal += self.left.inorder()
        traversal.append(self)
        if self.right:
            traversal += self.right.inorder()
    
    def min(self):
        if self.left: # 제일 왼쪽 끝에 있는 노드가 제일 작은 노드
            return self.left.min()
        else:
            return self # 그렇지 않다면 자기 자신을 리턴
        
    def max(self):
        if self.right:
            return self.right.max()
        else:
            return self
    
    def lookup(self, key, parent=None):
        if key < self.key:
            if self.left:
                return self.left.lookup(key, self) # self = parent node
            else:
                return None, None
        elif key > self.key:
            if self.right:
                return self.right.lookup(key, self)
            else:
                return None, None
        else:
            return self, parent
    
    def insert(self, key, data):
        if key < self.key:
            pass
        elif key > self.key:
            pass
        else:
            raise KeyError('...')
    
    def count(self):
        count = 0
        if self.left:
            count += 1
        if self.right:
            count += 1
        return count

class BinSearchTree:
    def __init__(self):
        self.root = None

    def inorder(self):
        if self.root:
            return self.root.inorder()
        else:
            return []
        
    def min(self):
        if self.root:
            return self.root.min()
        else:
            return None
    
    def max(self):
        if self.root:
            return self.root.max()
        else:
            return None
    
    def lookup(self, key):
        if self.root:
            return self.root.lookup(key)
        else:
            return None, None
        
    def insert(self, key, data):
        if self.root:
            self.root.insert(key, data)
        else:
            self.root = Node(key, data)