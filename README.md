# Algoritmos de busca em espaço de estados

Trabalho de Inteligência Artificial: modelar um espaço de estados com mais de 100 estados (os municípios do estado do Rio de Janeiro ligados por estradas) e resolvê-lo com cinco algoritmos de busca, comparando o tempo de resolução e o número de passos.

![Espaço de estados](https://user-images.githubusercontent.com/57930222/129944370-fa7f530f-2634-4bd3-a61e-362da79b8356.jpg)

| Arquivo | Algoritmo |
|---|---|
| `BFS.py` | Busca em largura (breadth-first) |
| `DSP.py` | Busca de custo uniforme (Dijkstra, menor caminho com distâncias) |
| `DFS.py` | Busca em profundidade (depth-first) |
| `LDFS.py` | Busca em profundidade limitada |
| `ILDFS.py` | Busca de aprofundamento iterativo |
| `citys.py` | Lista dos municípios usados como estados |

## Como rodar

```bash
python BFS.py
```

O programa lista os municípios numerados e pede o ponto de partida. Os outros arquivos funcionam do mesmo jeito.

## Aplicações pesquisadas

Representar um problema como espaço de estados e buscar nele aparece em sistemas de GPS (rota entre cidades), no planejamento de rotas de limpeza em empresas e na distribuição de bebidas (rotas de entrega).
