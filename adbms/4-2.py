from bplustree import BPlusTree
import time

tree = BPlusTree("C:\\Users\\hphem\\OneDrive\\Documents\\Desktop\\pracss\\adbms\\4-2.txt", order=50)

start = time.time()
for i in range(100):
    tree.insert(i, (2*i).to_bytes(10, 'big'))
end = time.time()
print((end - start)*1000)

start = time.time()
print(int.from_bytes(tree.get(43), 'big'))
end = time.time()
print((end - start)*1000)