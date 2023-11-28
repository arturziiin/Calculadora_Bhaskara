import funcoes
validar_equacao = verifica_equacao(a)
if validar_equacao == True:
    D = delta(a, b, c)
    x1, x2 = valor_x(D, a, b)
    if D > 0:
        valor_x(D, a, b)
        print(f"X1 = {x1}")
        print(f"X2 = {x2}")
    elif D < 0:
        if x1 == 0:
            print(x2)
        elif x2 == 0:
            print(x1)
