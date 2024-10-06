from setwithqueue import SetWithQueue

q = SetWithQueue()

print(q.size())

q.add(10)


print(q.size())

# q.list()

print(q.contains(10))
print(q.contains(11))
print(q.contains(10))

q.add(11)

q.add(12)

q.add(11)
