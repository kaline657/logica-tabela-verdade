import re
import itertools

print("Gerador de Tabela Verdade")
print("Projeto de Lógica e Matemática Discreta - UFMA")

expressao = input("Digite uma expressão lógica (ex: (p ∧ q) → r): ")

# identificar proposições
proposicoes = sorted(set(re.findall(r"[a-z]", expressao)))

# conectivos aceitos
conectivos = {
    "¬": " not ",
    "∧": " and ",
    "∨": " or ",
    "→": " <= ",
    "↔": " == "
}

# converter expressão para python
expressao_python = expressao
for simbolo, operador in conectivos.items():
    expressao_python = expressao_python.replace(simbolo, operador)

print("\nExpressão digitada:", expressao)
print("Proposições encontradas:", proposicoes)

print("\nTabela Verdade:\n")

# cabeçalho
for p in proposicoes:
    print(p, end=" ")
print("| Resultado")

# gerar combinações da tabela verdade
for valores in itertools.product([0,1], repeat=len(proposicoes)):

    ambiente = dict(zip(proposicoes, valores))

    exp = expressao_python

    for var, val in ambiente.items():
        exp = re.sub(rf"\b{var}\b", str(bool(val)), exp)

    try:
        resultado = eval(exp)
    except:
        resultado = False

    for v in valores:
        print(v, end=" ")

    print("|", int(resultado))