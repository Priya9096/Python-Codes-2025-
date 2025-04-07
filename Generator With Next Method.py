def disp():
    print("Start")
    yield 10
    print("Task 1")
    yield 20
    print("Task 2")
    yield 30

res = disp()

print(res.__next__())