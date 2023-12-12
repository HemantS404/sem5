# # A
# # list
# l = [1,2,3]
# l.append(4)
# l.remove(4)
# print(l.count(1))
# print(l.index(2))
# l.pop()
# print(l)
# # tuple
# t = (1,2,3)
# print(t.index(1))
# print(t.count(2))
# # set
# s = {1,2,3}
# s.add(4)
# print(s.pop())
# s.remove(4)
# print(s)
# print(s.intersection({2}))
# # dictionary
# d = {1:1, 2:2}
# print(d.keys())
# print(d.items())
# print(d.values())
# d[3] = 3
# print(d)

# # B
# def histogram(l):
#     dicty = {}
#     for i in l:
#         if dicty.get(i, None) == None:
#             dicty[i] = 1
#         else:
#             dicty[i] += 1
#     new = []
#     for i in dicty:
#         new.append((i, dicty[i]))
#     new.sort(key = lambda data: data[1])
#     return new
# print(histogram([1,2,2,3,3,4,4,4,1,1,6,7,6,5,1]))

# # C
# def perfect(n):
#     factors = []
#     for i in range(1, n):
#         if n%i == 0:
#             factors.append(i)
#     sumy = 0
#     for j in factors:
#         sumy += j
#     return True if sumy == n else False 
# print(perfect(28))

# # D
# def toh(fro, aux, to, n):
#     if n>0:
#         toh(fro, to, aux, n-1)
#         print(f"Move {n} from {fro} to {to} using {aux}")
#         toh(aux, fro, to, n-1)
#         return
#     else:
#         return

# toh("A","B","C",3)

# # E
# f = lambda a, b: b if a<b else a
# print(f(9,3))

# # F
# l1 = [1,2,3,4]
# l2 = [5,6,7,8]
# print(list(map(lambda a, b: a+b, l1, l2)))

# # G
# l1 = [1,2,3,4,5,6,7]
# print(list(map(lambda a: a**3, filter(lambda a: a%2!=0, l1))))