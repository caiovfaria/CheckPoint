# CheckPoint — Exercícios de Treino em Python

Repositório com 20 exercícios práticos de lógica de programação em Python, cobrindo desde estruturas condicionais básicas (`if/elif/else`) até a sintaxe mais moderna de correspondência de padrões (`match/case`, disponível a partir do Python 3.10).

## Como executar

Cada exercício é um script independente. Basta rodar:

```bash
python "Exercicio N.py"
```

e responder às entradas solicitadas no terminal.

## Índice

| # | Exercício | Conceito principal |
|---|-----------|---------------------|
| 1 | [Calculadora de IMC](#1-calculadora-de-imc-detalhada) | `if/elif/else` |
| 2 | [Conversor de Temperaturas](#2-conversor-de-temperaturas-inteligente) | `if/elif/else` + strings |
| 3 | [Desconto por Forma de Pagamento](#3-calculadora-de-desconto-por-forma-de-pagamento) | `if/elif/else` |
| 4 | [Conversor de Segundos](#4-conversor-de-segundos) | Aritmética inteira (`//`, `%`) |
| 5 | [Ano Bissexto](#5-verificador-de-ano-bissexto) | Operadores lógicos |
| 6 | [Classificador de Triângulos](#6-validador-e-classificador-de-triângulos) | Condicionais aninhadas |
| 7 | [Regras de Aposentadoria](#7-verificador-de-aposentadoria) | `if/elif/else` |
| 8 | [Imposto de Renda](#8-calculadora-de-imposto-de-renda) | `if/elif/else` (com bugs) |
| 9 | [Calculadora de 4 Operações](#9-calculadora-de-operações-básicas) | `if/elif/else` + tratamento de erro |
| 10 | [Identificador de Quadrante](#10-identificador-de-quadrante-cartesiano) | Condicionais múltiplas |
| 11 | [Pedra, Papel e Tesoura](#11-pedra-papel-e-tesoura) | Condicionais aninhadas |
| 12 | [Situação do Aluno](#12-situação-do-aluno-notas-e-faltas) | Condicionais aninhadas |
| 13 | [Equação de 2º Grau (Bhaskara)](#13-equação-de-2º-grau-bhaskara) | `math`, `if/elif/else` |
| 14 | [Validador de Data](#14-validador-de-data) | `match/case` |
| 15 | [Caixa Eletrônico](#15-caixa-eletrônico-decomposição-em-notas) | Aritmética inteira |
| 16 | [Signo do Zodíaco](#16-identificador-de-signo-do-zodíaco) | `if/elif/else` extenso |
| 17 | [Códigos de Status HTTP](#17-identificador-de-código-http) | `match/case` |
| 18 | [Conversor de Moedas](#18-conversor-de-moedas) | `match/case` |
| 19 | [Nome do Mês e Dias](#19-nome-do-mês-e-quantidade-de-dias) | `match/case` aninhado |
| 20 | [Pedágio por Veículo](#20-calculadora-de-pedágio) | `match/case` |

---

## 1. Calculadora de IMC Detalhada

**Contexto:** calcular o Índice de Massa Corporal (IMC) do usuário a partir de peso e altura, e classificar o resultado em uma das seis faixas usadas pela OMS.

**Como foi resolvido:**
- Lê `peso` (kg) e `altura` (m) como `float`.
- Calcula `imc = peso / (altura ** 2)`.
- Uma cadeia de `if/elif/else` compara o IMC contra os limites de cada faixa (abaixo do peso, peso normal, sobrepeso, obesidade graus I a III) e define a string `classificacao`.
- Imprime a classificação e o IMC formatado com 2 casas decimais (`{imc:.2f}`).

**Observação:** o `print("Classificação:", classificacao)` aparece duplicado no arquivo (uma vez antes de imprimir o IMC e outra depois) — é redundante, mas não quebra a execução.

---

## 2. Conversor de Temperaturas Inteligente

**Contexto:** converter uma temperatura entre Celsius e Fahrenheit, com base na escolha do usuário.

**Como foi resolvido:**
- Pergunta se o usuário quer converter de `'C'` para Fahrenheit ou de `'F'` para Celsius, normalizando a entrada com `.upper()` para aceitar minúsculas.
- Aplica as fórmulas padrão: `F = C * 9/5 + 32` e `C = (F - 32) * 5/9`.
- Trata entrada inválida (diferente de C/F) com uma mensagem de erro no `else`.

---

## 3. Calculadora de Desconto por Forma de Pagamento

**Contexto:** simular a política de preços de uma loja que varia conforme a forma de pagamento escolhida.

**Como foi resolvido:**
- O usuário escolhe entre 3 opções: PIX à vista, cartão de crédito 1x ou cartão parcelado.
- PIX aplica 10% de desconto (`preco * 0.9`), crédito à vista mantém o preço original, e o parcelado aplica 5% de juros (`preco * 1.05`).
- Um `if/elif/else` trata a opção escolhida e calcula o preço final correspondente.

---

## 4. Conversor de Segundos

**Contexto:** converter uma quantidade de segundos em horas, minutos e segundos.

**Como foi resolvido:**
- Usa divisão inteira (`//`) e módulo (`%`) sucessivamente:
  - `horas = tempo // 3600`
  - o resto vira `tempo % 3600`, do qual se extrai `minutos = tempo // 60`
  - o resto final é o total de segundos restantes.
- Imprime os três valores em uma única linha formatada.

---

## 5. Verificador de Ano Bissexto

**Contexto:** determinar se um ano é bissexto, seguindo a regra do calendário gregoriano.

**Como foi resolvido:**
- Aplica diretamente a regra matemática: um ano é bissexto se é divisível por 4 **e** não é divisível por 100, **ou** se é divisível por 400.
- Implementado como uma única expressão booleana: `(ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)`.

---

## 6. Validador e Classificador de Triângulos

**Contexto:** verificar se três medidas de lados formam um triângulo válido e, em caso positivo, classificá-lo (equilátero, isósceles ou escaleno).

**Como foi resolvido:**
- Aplica a desigualdade triangular: a soma de dois lados quaisquer deve ser maior que o terceiro lado, para os três pares possíveis.
- Se a condição é satisfeita, classifica com `if/elif/else` aninhado: todos os lados iguais → equilátero; dois lados iguais → isósceles; caso contrário → escaleno.

> ⚠️ **Ponto de atenção:** o script não possui um `else` para o caso em que os lados **não** formam um triângulo válido — nesse cenário, o programa simplesmente não imprime nada.

---

## 7. Verificador de Aposentadoria

**Contexto:** simular regras simplificadas de aposentadoria com base em idade e tempo de contribuição.

**Como foi resolvido:**
- Lê idade e anos de contribuição.
- `if/elif/else` com três faixas: aposentadoria plena (idade ≥ 65 ou contribuição ≥ 30 anos), regra especial (idade ≥ 60 e contribuição ≥ 25 anos), ou ainda não pode se aposentar.

---

## 8. Calculadora de Imposto de Renda

**Contexto:** calcular o Imposto de Renda devido com base no salário informado, usando faixas simplificadas.

**Como foi resolvido:**
- Compara o salário contra dois limites de faixa (`<= 2.112` e `<= 2.826`) e aplica uma fórmula de alíquota efetiva na segunda faixa (`salario * 0.075 - 1713.58`).

> ⚠️ **Este exercício está com bugs reais e não funciona corretamente como está:**
> 1. Os limites `2.112` e `2.826` são números de ponto flutuante (2,112 e 2,826), quase certamente deveriam ser `2112.00` e `2826.65` — parece confusão entre o separador de milhar brasileiro e o ponto decimal do Python.
> 2. A fórmula `salario * 0.075 - 1713.58` produz um valor **negativo** para qualquer salário nessa faixa (ex.: R$ 2.500 × 0,075 = 187,50 − 1.713,58 = −1.526,08), o que não faz sentido para um imposto.
> 3. A variável `imposto` é calculada mas **nunca é impressa** na tela.
> 4. A tabela do IR real tem mais de duas faixas; o `else` deste script apenas informa "salário acima do limite" sem calcular nada para quem ganha mais.
>
> Recomenda-se revisar os valores oficiais da tabela do IR e reescrever a lógica antes de considerar este exercício "resolvido".

---

## 9. Calculadora de Operações Básicas

**Contexto:** uma calculadora simples com as quatro operações aritméticas.

**Como foi resolvido:**
- Lê dois números e a operação desejada (`1` a `4`) como texto.
- `if/elif/else` executa soma, subtração, multiplicação ou divisão.
- Na divisão, há uma checagem extra para `num2 == 0`, evitando `ZeroDivisionError` e informando "Operação inválida".

---

## 10. Identificador de Quadrante Cartesiano

**Contexto:** dado um ponto (x, y), identificar em qual quadrante do plano cartesiano ele está, ou se está sobre um dos eixos/origem.

**Como foi resolvido:**
- Uma cadeia de `if/elif` trata, nesta ordem: origem (x=0 e y=0), eixo Y (x=0), eixo X (y=0), e os quatro quadrantes (Q1 a Q4) combinando o sinal de x e y.

---

## 11. Pedra, Papel e Tesoura

**Contexto:** simular uma rodada do clássico jogo Pedra, Papel e Tesoura contra o computador.

**Como foi resolvido:**
- Lê a jogada do usuário (normalizada com `.lower()`).
- Compara com a jogada do computador usando a lógica clássica: pedra vence tesoura, tesoura vence papel, papel vence pedra.
- Trata empate e jogada inválida.

> ⚠️ **Limitação:** a variável `computador = "pedra"` está fixa no código — não há `import random`, então o computador sempre joga "pedra" em toda execução. Para virar um jogo de verdade, seria necessário usar `random.choice(["pedra", "papel", "tesoura"])`.

---

## 12. Situação do Aluno (Notas e Faltas)

**Contexto:** determinar a situação final de um aluno considerando duas notas e a porcentagem de faltas.

**Como foi resolvido:**
- Primeiro verifica se as faltas excedem 25% — nesse caso, reprovação automática por faltas, sem nem calcular a média.
- Caso contrário, calcula a média das duas notas e classifica em Aprovado (≥ 7,0), Recuperação (≥ 5,0) ou Reprovado por Nota, usando `if/elif/else` aninhado.

---

## 13. Equação de 2º Grau (Bhaskara)

**Contexto:** resolver uma equação do segundo grau (ax² + bx + c = 0) usando a fórmula de Bhaskara.

**Como foi resolvido:**
- Importa `math` para usar `math.sqrt`.
- Trata o caso especial `A == 0` (não seria uma equação de 2º grau).
- Calcula o discriminante (`delta = B**2 - 4*A*C`) e usa `if/elif/else` para os três cenários possíveis: delta negativo (sem raízes reais), delta zero (raiz única) e delta positivo (duas raízes reais, calculadas com a fórmula completa).

---

## 14. Validador de Data

**Contexto:** verificar se uma combinação de dia/mês/ano forma uma data válida no calendário, considerando anos bissextos.

**Como foi resolvido:**
- Calcula se o ano é bissexto com a mesma regra do Exercício 5.
- Usa `match/case` sobre o mês para definir o limite de dias: fevereiro (28 ou 29, dependendo do ano bissexto), meses com 30 dias (`4 | 6 | 9 | 11`), meses com 31 dias (`1 | 3 | 5 | 7 | 8 | 10 | 12`), e um `case _` de segurança para mês inválido.
- Valida o dia contra o limite calculado usando uma expressão condicional (`"Data válida!" if 1 <= dia <= limite else "Data inválida!"`).

---

## 15. Caixa Eletrônico (Decomposição em Notas)

**Contexto:** simular a lógica de um caixa eletrônico, decompondo um valor de saque no menor número de cédulas disponíveis (100, 50, 20, 10, 5 e 2 reais).

**Como foi resolvido:**
- Primeiro descarta valores que não podem ser formados com as notas disponíveis (valores menores que 2, ou iguais a 1 ou 3).
- Em seguida, aplica divisão inteira e módulo sucessivamente para cada cédula, do maior para o menor valor, "abatendo" o valor restante a cada passo — a mesma técnica usada no Exercício 4.
- Ao final, se sobrar algum valor não divisível pelas notas disponíveis, informa que o saque é inválido; caso contrário, imprime a quantidade de cada nota entregue.

---

## 16. Identificador de Signo do Zodíaco

**Contexto:** dado um dia e mês de nascimento, identificar o signo do zodíaco correspondente.

**Como foi resolvido:**
- Valida primeiro se mês e dia estão em intervalos plausíveis (mês 1–12, dia 1–31).
- Usa uma longa cadeia de `elif`, cada um cobrindo o intervalo de datas de um signo (ex.: Áries vai de 21/03 a 19/04, testado como duas condições unidas por `or`, já que o intervalo cruza a virada do mês).
- Como observação de melhoria: essa lógica repetitiva poderia ser simplificada com uma lista de tuplas `(mes_limite, dia_limite, nome_do_signo)` percorrida em um laço, mas como exercício de prática de `if/elif` a solução está correta.

---

## 17. Identificador de Código HTTP

**Contexto:** dado um código de status HTTP, exibir seu significado.

**Como foi resolvido:**
- Usa `match/case` para mapear diretamente os códigos mais comuns (200, 400, 401, 403, 404, 500) para sua descrição textual.
- O `case _` cobre qualquer código não cadastrado.

---

## 18. Conversor de Moedas

**Contexto:** converter um valor em Reais para Dólar, Euro, Libra ou Iene, usando taxas de câmbio fixas.

**Como foi resolvido:**
- Usa `match/case` sobre a opção escolhida (1 a 4) para selecionar a taxa de câmbio correspondente e dividir o valor em reais por ela.
- Formata a saída com o símbolo de cada moeda (`$`, `€`, `£`, `¥`) e duas casas decimais.

> **Observação:** as taxas de câmbio estão fixas (hardcoded) no código — o que é adequado para fins didáticos, mas exigiria integração com uma API de câmbio para valores reais e atualizados.

---

## 19. Nome do Mês e Quantidade de Dias

**Contexto:** dado o número de um mês (1 a 12), exibir seu nome por extenso e quantos dias ele tem.

**Como foi resolvido:**
- Usa `match/case` externo para agrupar os meses por quantidade de dias (31, 30, ou fevereiro à parte).
- Dentro de cada grupo, um segundo `match/case` aninhado traduz o número do mês para seu nome em português.
- Fevereiro é tratado separadamente, já que sua quantidade de dias varia (28 ou 29).

> **Observação:** a solução funciona, mas o aninhamento de dois `match` é mais verboso do que o necessário — o mesmo resultado poderia ser obtido com um único dicionário `{1: "Janeiro", 2: "Fevereiro", ...}` e uma lista separada de meses com 30/31 dias.

---

## 20. Calculadora de Pedágio

**Contexto:** calcular o valor do pedágio com base no tipo de veículo.

**Como foi resolvido:**
- Usa `match/case` para mapear o tipo de veículo (1 a 4: moto, carro, caminhonete, caminhão) ao valor correspondente (R$ 5, 10, 15 e 25).
- O `case _` trata tipos inválidos.

---

## Resumo de pontos de atenção

| Exercício | Problema identificado |
|---|---|
| 1 | `print` de classificação duplicado (cosmético, não afeta o resultado) |
| 6 | Falta tratar o caso em que os lados **não** formam um triângulo válido |
| 8 | Limites de faixa incorretos, fórmula gera imposto negativo, variável `imposto` nunca é impressa, faltam faixas da tabela real |
| 11 | Jogada do computador é fixa (`"pedra"`) — falta `import random` para tornar o jogo funcional |

Esses pontos não impedem o entendimento do conceito trabalhado em cada exercício, mas seriam os primeiros alvos de correção caso o repositório evolua para uma versão "produção".
