with open("6.txt", "w") as f:
    f.writelines('meow\nme\nmuh\nwow\nmemeh')

with open("6.txt", "r") as f:
    data = f.readlines()
    for i in data:
        print(i.strip())

with open("6.txt", "a") as f:
    f.write("\nnigga")

with open("6.txt", "r") as f:
    data = f.readlines()
    for i in data:
        print(i.strip())