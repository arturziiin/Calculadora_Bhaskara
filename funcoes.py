def verifica_equacao (a):
    if a == 0:
        print("Valor inválido para a, a equação não é de segundo grau!")
        return False
    else:
        return True
        
def delta(a, b, c):
    D = (b**2) - (4*a*c)
    print(f"Δ = {D}")
    return D

def valor_x (D, a, b):
    x1 = (((-b)+D**0.5) / 2*a)
    if x1 <= 0:
        x1 = ("Não existe raiz")
    x2 = (((-b)-D**0.5) / 2*a)
    if x2 <= 0:
        x2 = ("Não existe raiz")
    return x1, x2
