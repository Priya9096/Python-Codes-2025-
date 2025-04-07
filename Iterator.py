li = [10,20,30] #iterable

iterator = iter(li)
print(iterator.__next__())
print(iterator.__next__())
print(iterator.__next__())
print(iterator.__next__()) #StopIteration

