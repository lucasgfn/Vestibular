# Trabalho desenvolvido na Matéria de Algoritmo e Estrutura de Dados

O vestibular de verão da Udesc está se aproximando. O processo seletivo será realizado por meio de
provas presenciais. Para evitar cópias, a universidade prepara diferentes versões da prova, de modo
que candidatos sentados próximos a outros não tenham as mesmas provas. Neste ano, a universidade
padronizou o layout das salas e deseja automatizar a distribuição de provas nas mesas. Sua tarefa é
implementar e avaliar um conjunto de algoritmos para resolver esse problema, conforme os detalhes a
seguir.
A sala de aula é modelada por um grafo não-dirigido G = (V, E), onde os vértices V = {1, 2, . . .}
representam as mesas da sala, e as arestas E conectam pares de mesas vizinhas (i.e. vértices vizinhos).
Ou seja, se as mesas u e v são vizinhas na sala de aula, então {u, v} ∈ E. A universidade possui
vários tipos de prova {1, 2, . . .}, mas deseja usar a menor quantidade de tipos possível, para facilitar os
procedimentos de correção. O algoritmo deverá garantir que nenhuma mesa receba uma prova do mesmo
tipo alocado a uma mesa vizinha, ao mesmo tempo que use a menor quantidade possível de tipos de
prova.
