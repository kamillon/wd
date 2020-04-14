def Parzyste(data):
    for i in range(0, len(data), 2):
        yield data[i]

list = [1, 2, 3, 4, 5]
p = Parzyste(list)
print(p.__next__())
print(p.__next__())
print(p.__next__())