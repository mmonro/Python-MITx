class Queue(object):
    def __init__(self):
        self.myqueue = []
        
    def insert(self, e):
        self.myqueue.append(e)
        
    def remove(self):
        try:
            return self.myqueue.pop(0)
        except:
            raise ValueError()
            
    def __str__(self):
        return '{' + ','.join([str(e) for i in self.myqueue]) + '}'
        
queue = Queue()
queue.insert(5)
queue.insert(6)
print queue.remove() #should return 5

queue.insert(7)
print queue.remove() #should return 6

print queue.remove() #should return 7

print queue.remove() #now empty, should raise ValueError exception
        
