pessoas = ("Ana" , "Bia", "Celi", "Diana", "Eva", "Fabia")
comb = []
for p1 in pessoas:
    for p2 in range(len(pessoas)):
        if f"{pessoas[p2]} e {p1}" in comb or pessoas[p2] == p1:
            continue
        comb.append(f"{p1} e {pessoas[p2]}")
print(comb)