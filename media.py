print("digite 5 notas")

# ao invés de ser 5 notas predefinidas, agora é possível adicionar 5 notas que desejar 

v1 = int(input(""))
v2 = int(input(""))
v3 = int(input(""))
v4 = int(input(""))
v5 = int(input(""))

y = [v1, v2, v3, v4, v5]

x = 0

for i in range(len(y)):
    x = x + y[i]

z = x / len(y)

print("Média final:", z)
