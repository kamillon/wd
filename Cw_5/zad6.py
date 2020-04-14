class Wspak:
    """Iterator zwracający wartości w odwróconym porządku"""
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]

w1 = Wspak("iterator")
it = iter(w1)
print(w1.__next__())
print(w1.__next__())
print(w1.__next__())
print(w1.__next__())
print(w1.__next__())
print(w1.__next__())
print(w1.__next__())
print(w1.__next__())
print("\n")

lista = [1, 2, 3, 4, 5]
w2 = Wspak(lista)
it = iter(w2)
print(w2.__next__())
print(w2.__next__())
print(w2.__next__())
print(w2.__next__())
print(w2.__next__())