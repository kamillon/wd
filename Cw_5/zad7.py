class Parzyste:

    def __init__(self, data):
        self.data = data
        self.index = -2

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index + 2 > len(self.data) - 1:
            raise StopIteration
        self.index += 2
        return self.data[self.index]

list = [1, 2, 3, 4, 5]
p = Parzyste(list)
print(p.__next__())
print(p.__next__())
print(p.__next__())