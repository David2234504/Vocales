print("-------------------------------------")
print("----------Contador Vocales-----------")
print("-------------------------------------")

frase = input("Digite una frase: ")
vocales = "aeiouAEIOU"
a = 0
e = 0
i = 0
o = 0
u = 0

for k in frase:
    if k in vocales:
        if k == "a" or k == "A":
            a = a + 1
        elif k == "e" or k == "E":
            e = e + 1
        elif k == "i" or k == "I":
            i = i + 1
        elif k == "o" or k == "O":
            o = o + 1
        elif k == "u" or k == "U":
            u = u + 1

print(f"En la frase hay {a} veces la 'a'")
print(f"En la frase hay {e} veces la 'e'")
print(f"En la frase hay {i} veces la 'i'")
print(f"En la frase hay {o} veces la 'o'")
print(f"En la frase hay {u} veces la 'u'")
