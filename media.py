print("digite 5 notas")

# ao invés de ser 5 notas predefinidas, agora é possível adicionar 5 notas que desejar 

var1 = int(input(""))
var2 = int(input(""))
var3 = int(input(""))
var4 = int(input(""))
var5 = int(input(""))

y = [var1, var2, var3, var4, var5]

x = 0

for i in range(len(y)):
    x = x + y[i]

M = x / len(y)

print("Média final:", M)
