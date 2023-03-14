class MaxHeap():
    def __init__(self):
        self.data = [None]
        
    def insert(self, item):
        pass
    
    def maxHeapify(self, i):
        pass
    
    def remove(self):
        if len(self.data) > 1:
            self.data[1], self.data[-1] = self.data[1], self.data[-1]
            data = self.data.pop(-1)
            self.maxHeapify(1)
        else:
            data = None
        return data