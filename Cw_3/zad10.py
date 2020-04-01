def zakupy(** lista):
    return sum(int(values) for values in lista.values())

print(zakupy(banany="4", jablka="5", pomarancze="2"))