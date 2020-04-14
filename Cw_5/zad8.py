class Samogloski:

    def __init__(self, data):
        if not isinstance(data, str):
            raise BaseException("Podano niepoprawny argument")
        self.data = data
        self.index = -1

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index + 1 > len(self.data) - 1:
            raise StopIteration
        for i in "AaEeIiOoUuYy":
            if self.data[self.index + 1] == i:
                self.index += 1
                return self.data[self.index]
        self.index += 1
        return self.__next__()

text = "Samogloski"
s = Samogloski(text)
print(s.__next__())
print(s.__next__())
print(s.__next__())
print(s.__next__())