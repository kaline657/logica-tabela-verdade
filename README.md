# logica-tabela-verdade
Projeto da disciplina de Lógica e Matemática Discreta - UFMA
# Gerador de Tabela Verdade
# Autor

Kaline Carvalho  
Universidade Federal do Maranhão – UFMA  
Disciplina: Lógica e Matemática Discreta

O objetivo deste programa é gerar automaticamente a **tabela-verdade de uma expressão da lógica proposicional**, a partir da entrada fornecida pelo usuário.

---

# 1. Introdução

Na lógica proposicional, as proposições podem assumir apenas dois valores lógicos:

- **Verdadeiro (1)**
- **Falso (0)**

A partir dessas proposições podemos construir **expressões lógicas** utilizando conectivos lógicos.

Os principais conectivos utilizados são:

| Símbolo | Operação | Significado |
|------|------|------|
| ¬ | Negação | NÃO |
| ∧ | Conjunção | E |
| ∨ | Disjunção | OU |
| → | Implicação | SE...ENTÃO |
| ↔ | Bicondicional | SE E SOMENTE SE |

A **tabela-verdade** apresenta o resultado lógico da expressão para **todas as combinações possíveis das proposições**.

Por exemplo, para a expressão:
(p ∧ q) → r

Existem **3 proposições**, portanto o número de linhas da tabela verdade será:

2³ = 8 combinações possíveis

O programa desenvolvido neste projeto automatiza esse processo.

---

# 2. Objetivo do Projeto

O objetivo deste programa é:

- Receber uma **expressão lógica digitada pelo usuário**
- Validar se a expressão possui apenas **símbolos permitidos**
- Identificar automaticamente as **proposições presentes**
- Gerar todas as **combinações possíveis de valores lógicos**
- Calcular o resultado da expressão
- Exibir a **tabela-verdade completa**

---

# 3. Tecnologias Utilizadas

O projeto foi desenvolvido utilizando:

- **Python 3**
- Biblioteca **re** (expressões regulares)
- Biblioteca **itertools** (geração de combinações)

---

# 4. Estrutura do Projeto

O projeto possui um arquivo principal:
main.py

Esse arquivo contém toda a lógica necessária para:

- validar a entrada do usuário
- identificar proposições
- interpretar conectivos lógicos
- gerar as combinações da tabela verdade
- calcular o resultado da expressão

---

# 5. Funcionamento do Programa

O funcionamento do sistema ocorre em algumas etapas principais.

---

## 5.1 Entrada da expressão lógica

O programa solicita ao usuário que digite uma expressão lógica.

Exemplo:
(p ∧ q) → r

Essa entrada é armazenada em uma variável dentro do programa.

---

## 5.2 Restrição e validação da entrada

Para evitar ambiguidades da linguagem natural, o programa permite apenas os seguintes símbolos:

- proposições: **p, q, r, s...**
- conectivos: **¬ ∧ ∨ → ↔**
- parênteses: **( )**

Essa validação é feita utilizando **expressões regulares**.

Caso o usuário digite símbolos inválidos, o programa exibe uma mensagem de erro e encerra a execução.

---

## 5.3 Identificação das proposições

O programa identifica automaticamente quais proposições aparecem na expressão lógica.

Exemplo:
(p ∧ q) → r

Proposições identificadas:
['p', 'q', 'r']

Isso permite que o programa saiba **quantas colunas a tabela verdade deve possuir**.

---

## 5.4 Conversão dos conectivos lógicos

Para que a expressão possa ser avaliada pelo Python, os conectivos lógicos são convertidos para operadores equivalentes da linguagem.

| Conectivo Lógico | Operador Python |
|------|------|
| ¬ | not |
| ∧ | and |
| ∨ | or |
| → | <= |
| ↔ | == |

Essa conversão permite que o Python interprete corretamente a expressão lógica.

---

## 5.5 Geração das combinações da tabela verdade

Para gerar todas as combinações possíveis de valores das proposições é utilizada a biblioteca:
itertools.product()

Por exemplo, para três proposições são geradas as seguintes combinações:
000
001
010
011
100
101
110
111

Cada linha representa uma possível atribuição de valores para as proposições.

---

## 5.6 Avaliação da expressão lógica

Para cada combinação de valores das proposições, a expressão lógica é avaliada.

O programa substitui cada proposição por **True ou False** e calcula o resultado da expressão.

O resultado é então exibido na tabela-verdade.

---

# 6. Exemplo de Execução

Entrada do usuário:
(p ∧ q) → r
Saída gerada pelo programa:
p q r | (p ∧ q) → r
0 0 0 | 1
0 0 1 | 1
0 1 0 | 1
0 1 1 | 1
1 0 0 | 1
1 0 1 | 1
1 1 0 | 0
1 1 1 | 1

---

# 7. Como Executar o Programa no VS Code

### 1. Abrir o projeto

Abra a pasta do projeto no **Visual Studio Code**.

---

### 2. Abrir o terminal

No VS Code pressione:
CTRL + `

ou vá em:
Terminal → New Terminal

---

### 3. Executar o programa

No terminal digite o comando:
python main.py

---

### 4. Digitar a expressão lógica

Quando solicitado, digite uma expressão lógica.

Exemplo:
(p ∧ q) → r

O programa irá gerar automaticamente a **tabela verdade correspondente**.

---

# 8. Exemplos de Expressões Aceitas

O programa aceita expressões como:
p ∧ q

¬p

(p ∧ q) → r

(p ∨ q) ↔ r

¬(p ∨ q)

---

# 9. Conclusão

O programa desenvolvido demonstra a aplicação prática dos conceitos de **Lógica Proposicional**, permitindo gerar automaticamente tabelas-verdade para diferentes expressões lógicas.

A solução utiliza recursos da linguagem Python para:

- validação de entradas
- manipulação de expressões
- geração de combinações
- avaliação lógica

Dessa forma, o sistema permite analisar rapidamente qualquer expressão dentro das regras da lógica proposicional estudadas em aula.
