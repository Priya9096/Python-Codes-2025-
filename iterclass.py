class Counter:
    def __init__(self, limit):
        self.count = 0
        self.limit = limit
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.count < self.limit:
            self.count += 1
            return self.count
        else:
            raise StopIteration
c1 = Counter(5)
print(c1.__iter__())
print(c1.__next__())
print(c1.__next__())


    
