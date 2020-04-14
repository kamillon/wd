class Kwadrat():

    def __init__(self, x):
        self.x = x

    def __add__(self, bok):
        return Kwadrat(self.x + bok.x)

    def __str__(self):
        return f'Bok = {self.x}'

b1 = Kwadrat(4)
b2 = Kwadrat(5)
b3 = b1 + b2
print(b3)