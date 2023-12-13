count_memory = int(input("Enter no. of memory blocks : "))
seq = list(map(int,input("Enter the sequence : ").split(' ')))

block = [None for _ in range(count_memory)]
timestapm = [-1 for _ in range(count_memory)]

hits = 0
faults = 0

print()
for i, j in enumerate(seq):
    if j not in block:
        minimum = min(timestapm)
        index = timestapm.index(minimum)
        block[index] = j
        timestapm[index] = i
        faults +=1
    else:
        index = block.index(j)
        timestapm[index] = i
        hits += 1
    print(j," : \t",block)

print(f"\nNo. of hits : {hits}\t\tHit ratio : {hits/len(seq)}")
print(f"No. of faults : {faults}\tFault ratio : {faults/len(seq)}")    
    
    