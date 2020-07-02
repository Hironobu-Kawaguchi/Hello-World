import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

# 初期化
G = nx.DiGraph()

# エッジをまとめて追加する
G.add_edges_from([(0, 1), (1, 0), (2, 3), (2, 1), (3, 4)])

# ノードを描画する位置を決める
pos = nx.spring_layout(G)

# 描画
nx.draw_networkx(G, pos)
plt.show()