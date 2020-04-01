def prosta(a1, a2):
    if(a1 == a2):
        return "Proste sa rownolegle"
    elif(a1 * a2 == -1):
        return "Proste sa prostopadle"
    else:
        return "Proste nie sa w relacji"

print(prosta(1, 1))
print(prosta(1, -1))