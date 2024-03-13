def existe_em_fib(n):
    f1, f2 = 0, 1

    if n == f1 or n == f2:
        return True

    while f2 < n:
        temp = f2
        f2 = f2 + f1
        f1 = temp

        if f2 == n:
            return True

    return False

n = int(input("Digite o número que deseja verificar: "))
textoExistencia = "existe" if existe_em_fib(n) else "não existe"
print(f"{n} {textoExistencia} na sequência de Fibonacci.")
