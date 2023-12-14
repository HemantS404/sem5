import BTrees._IIBTree as IIBTree
import time

tree = IIBTree.BTree(order = 5)

start = time.time()
for i in range(100000):
    tree.insert(i, 2*i)
end = time.time()
print((end - start)*1000)

start = time.time()
print(tree.get(4327))
end = time.time()
print((end - start)*1000)