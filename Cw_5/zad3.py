class Kwadrat:
    def __init__(self, x):
        self.x = x
    def __ge__(self,kw):
        if(self.x >= kw.x):
            return "Pierwszy kwadrat jest większy lub równy drugiemu"
        else:
            return "Pierwszy kwadrat jest mniejszy niż drugi"
    def __gt__(self,kw):
        if(self.x > kw.x):
           return "Pierwszy kwadrat jest większy niż drugi"
        else:
            return "Pierwszy kwadrat nie jest większy niż drugi"
    def __le__(self,kw):
        if(self.x <= kw.x):
            return "Pierwszy kwadrat jest mniejszy lub równy drugiemu"
        else:
            return "Pierwszy kwadrat jest większy niż drugi"
    def __lt__(self,kw):
        if(self.x < kw.x):
            return "Pierwszy kwadrat jest mniejszy niż drugi"
        else:
            return "Pierwszy kwadrat nie jest mniejszy niż drugi"

kwadrat1 = Kwadrat(4)
kwadrat2 = Kwadrat(3)
print(kwadrat1 >= kwadrat2)
print(kwadrat1 > kwadrat2)
print(kwadrat1 <= kwadrat2)
print(kwadrat1 < kwadrat2)