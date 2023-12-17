import random

def compute(genes):
    x = [int(i,2) for i in genes]
    fx = [i**2 for i in x]
    fx_sum = sum(fx)
    expected = [round(i/fx_sum,4) for i in fx]
    actual = [round(i*4,0) for i in expected]
    if sum(actual) < 4:
        index = actual.index(max(actual))
        actual[index] += 1
    if sum(actual) > 4:
        index = actual.index(max(actual))
        actual = actual[:4]
    return x, fx, expected, actual

def crossover(mating_pool):
    remaing = [i for i in range(len(mating_pool))]
    partners = {}
    while len(remaing)!=0:
        parent1 = remaing.pop()
        parent2 = random.choice(remaing)
        c_point = random.randint(1, 4)
        remaing.remove(parent2)
        partners[parent1] = {'partner':parent2,'c_point':c_point}
        partners[parent2] = {'partner':parent1,'c_point':c_point}
    new_popluation = []
    for i in partners:
        parent1 = i
        parent2 = partners[i]['partner']
        c_point = partners[i]['c_point']
        child = mating_pool[parent1][:c_point] + mating_pool[parent2][c_point:]
        new_popluation.append(child)
    return partners, new_popluation

def GA(genes, itr):
    print("--------------------------------------------------------------")
    print("Initial Population : ", [int(i,2) for i in genes])
    for j in range(itr):
        x, fx, expected, actual = compute(genes)
        print(f"----------------Genration {j}-----------------------------------")
        print(f"Gene\tValue\tFit\tExp\tActual")
        for i in range(4):
            print(f"{genes[i]}\t{x[i]}\t{fx[i]}\t{expected[i]}\t{actual[i]}")
        mating_pool = []
        for gene, rep in zip(genes, actual):
            for _ in range(int(rep)):
                mating_pool.append(gene)
        parteners, new_popluation = crossover(mating_pool)
        x = [int(i,2) for i in mating_pool]
        print(f"----------------New Population Genration {j}--------------------")
        print(f"Gene\tValue\tPartner\tC Point\tChild")
        for i in range(4):
            print(f"{mating_pool[i]}\t{x[i]}\t{parteners[i]['partner']}\t{parteners[i]['c_point']}\t{new_popluation[i]}")
        genes = new_popluation
    print("--------------------------------------------------------------")
    print("Final Population : ", [int(i,2) for i in genes])
    print("--------------------------------------------------------------")

genes = ['10010', '01010', '01101','01000']
GA(genes, 3)