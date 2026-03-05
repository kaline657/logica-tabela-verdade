import re

print("Gerador de Tabela Verdade")
print("Projeto de Lógica e Matemática Discreta - UFMA")

expressao = input("Digite uma expressão lógica (ex: p ∧ q): ")

# identificar proposições
proposicoes = sorted(set(re.findall(r"[a-z]", expressao)))

# conectivos aceitos
conectivos = {
    "¬": "NAO",
    "∧": "E",
    "∨": "OU",
    "→": "IMPLICA",
    "↔": "BICONDICIONAL"
}

# identificar conectivos usados
conectivos_encontrados = []

for simbolo in conectivos:
    if simbolo in expressao:
        conectivos_encontrados.append(simbolo)

print("\nExpressão digitada:", expressao)
print("Proposições encontradas:", proposicoes)
print("Conectivos encontrados:", conectivos_encontrados)