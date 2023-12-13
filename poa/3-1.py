count_memory = int(input("Enter no. of memory location : "))
count_process = int(input("Enter no. of process : "))

memories = {}
for i in range(count_memory):
    print(f"\nFor memory m{i}")
    size = int(input("Enter size : "))
    memory = {"size":size, "free":True, "empty":0, "process":None}
    memories[f"m{i}"] = memory

processes = {}
for i in range(count_process):
    print(f"\nFor process p{i}")
    size = int(input("Enter size : "))
    process = {"size":size, "placed":False}
    processes[f"p{i}"] = process

for p in processes:
    diff = float('inf')
    optimal_memory = None
    for m in memories:
        if memories[m]["free"]:
            if diff > (memories[m]["size"] - processes[p]["size"] and (memories[m]["size"] - processes[p]["size"]))>= 0:
                optimal_memory = m
                diff = memories[m]["size"] - processes[p]["size"]
    if optimal_memory != None:
        memories[optimal_memory]["free"] = False
        memories[optimal_memory]["empty"] = diff
        memories[optimal_memory]["process"] = p
        processes[p]["placed"] = True

print("\nUsing Best fit : ")
for m in memories:
    print(f"Memory : {m}\tSize : {memories[m]['size']}\tOccupied : {not memories[m]['free']}\t\tEmpty : {memories[m]['empty']}\tOccupied By : {memories[m]['process']}")

for p in processes:
    if not processes[p]["placed"]:
        print(f"Process {p} is not Placed with size {processes[p]['size']}")

