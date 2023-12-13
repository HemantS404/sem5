count_memory = int(input("Enter no. of memory blocks : "))
seq = list(map(int,input("Enter the sequence : ").split(' ')))

block = [None for _ in range(count_memory)]

hits = 0
faults = 0
head = 0

print()
for j in seq:
    if j not in block:
        block[head] = j
        head = (head + 1)%count_memory
        faults += 1
    else:
        hits += 1
    print(j," : \t",block)

print(f"\nNo. of hits : {hits}\t\tHit ratio : {hits/len(seq)}")
print(f"No. of faults : {faults}\tFault ratio : {faults/len(seq)}")    
    
    