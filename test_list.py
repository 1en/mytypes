from mytypes import LinkedList


mylist = LinkedList()
mylist.append(1)
mylist.append(2)

assert mylist[0] == 1
assert mylist[1] == 2

assert len(mylist) == 2

mylist.clear()
assert len(mylist) == 0

raised = False
try:
    mylist[1]
except IndexError:
    raised = True
assert raised

mylist = LinkedList(1)
mylist[0] = 2
assert mylist[0] == 2
del mylist[0]
assert len(mylist) == 0

mylist = LinkedList(1, 2, 3)
del mylist[1]
assert mylist[1] == 3
del mylist[1]
assert len(mylist) == 1

a = LinkedList(1, 2, 3)
b = LinkedList(4, 5)
a.extend(b)
assert a[0] == 1
assert a[1] == 2
assert a[2] == 3
assert a[3] == 4
assert a[4] == 5
assert len(a) == 5

b.append(6)

raised = False
try:
    a[5]
except IndexError:
    raised = True
assert raised
