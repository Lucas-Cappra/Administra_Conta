import numpy as np
import matplotlib as plt


NLivros = int(input(("Quantos livros você comprou? \n")))

def GastoLivros(LivrosPrecos):
    LivrosPrecos = []
    TotalGasto = 0
    for i in range (0, NLivros):
        ele = float(input("Quanto custou respectivamente os livros? \n"))
        LivrosPrecos.append(ele)

    for i in range (0, NLivros):

        TotalGasto = LivrosPrecos[i] + TotalGasto
    return TotalGasto

print(f"Você gastou R${GastoLivros(NLivros)} em livros.")

NAlmoços = int(input(("Quantos dias você comprou almoço?")))