li = [50]
# Adding Element into List(at the end of the list using append():
li.append(100) 
print(li) # [50, 100]

#insert(index, element) inserts an element at specific index
li.insert(0,500)
print(li) #[500, 50, 100]

# pop ():pop method without any argument removes and returns last element from the list.
ele = li.pop()
print(ele) #100
print(li) #[500, 50]

# pop(index): pop can remove specific index element from list.
print(li.pop(0)) #500
print(li) # [50]

li.append(700) 
print(li) # [50, 700]

# remove(element):Removes element from list.
li.remove(700)
print(li) # [50]

li.append(900) 
print(li) # [50,900]

# del keyword: 
del li[1]
print("After del: ",li) # [50]

del li # Deletes whole object from the memory.
# print(li) #Error



