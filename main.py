import re
import itertools

print("======================================")
print("Gerador de Tabela Verdade")
print("Disciplina: Lógica e Matemática Discreta")
print("======================================")

expressao = input("Digite uma expressão lógica (ex: (p ∧ q) → r): ")

# -----------------------------
# 1. Validar entrada restrita
# -----------------------------
padrao = r"^[p-z¬∧∨→↔()\s]+$"

if not re.match(padrao, expressao):
    print("\nErro: expressão contém símbolos inválidos.")
    print("Use apenas: p q r ... ¬ ∧ ∨ → ↔ ( )")
    exit()

# -----------------------------
# 2. Identificar proposições
# -----------------------------
proposicoes = sorted(set(re.findall(r"[p-z]", expressao)))

print("\nExpressão digitada:", expressao)
print("Proposições encontradas:", proposicoes)

# -----------------------------
# 3. Mapear conectivos lógicos
# -----------------------------
conectivos = {
    "¬": " not ",
    "∧": " and ",
    "∨": " or ",
    "→": " <= ",
    "↔": " == "
}

expressao_python = expressao

for simbolo, operador in conectivos.items():
    expressao_python = expressao_python.replace(simbolo, operador)

# -----------------------------
# 4. Gerar tabela verdade
# -----------------------------
print("\nTabela Verdade\n")

# Cabeçalho
for p in proposicoes:
    print(p, end=" ")

print("|", expressao)

# Combinações possíveis
for valores in itertools.product([0,1], repeat=len(proposicoes)):

    ambiente = dict(zip(proposicoes, valores))
    exp = expressao_python

    # substituir variáveis pelos valores
    for var, val in ambiente.items():
        exp = re.sub(rf"\b{var}\b", str(bool(val)), exp)

    try:
        resultado = eval(exp)
    except:
        resultado = False

    for v in valores:
        print(v, end=" ")

    print("|", int(resultado))