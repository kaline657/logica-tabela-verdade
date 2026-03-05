import re

print("Gerador de Tabela Verdade")
print("Projeto de Lógica e Matemática Discreta - UFMA")

expressao = input("Digite uma expressão lógica (ex: p ∧ q): ")

# identificar proposições
proposicoes = sorted(set(re.findall(r"[a-z]", expressao)))

print("Expressão digitada:", expressao)
print("Proposições encontradas:", proposicoes)