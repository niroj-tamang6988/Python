collection = {1,2,3,4,5,5,6 }

print(collection)

#empty set
empty = set()

print(type(empty))

#add method to add element in set
empty.add(1)
empty.add(2)
empty.add(3)
empty.add(4)

#remove method to remove element in set
# empty.remove(2)

# empty.clear() #clear all element in set

print(empty.pop())#removes random values
# print(empty)


#union and intersection of sets
set1 = {1,2,3}
set2={3,4,5}

print(set1.union(set2)) #union of set1 and set2
print(set1.intersection(set2)) #intersection of set1 and set2