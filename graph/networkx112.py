# Aidemy ネットワーク分析入門 1.1.2 グラフを描画してみよう
# https://aidemy.net/courses/6150/exercises/BJb27HnvdG

import networkx as nx
import matplotlib.pyplot as plt

# 一繋ぎの5個の点を持つグラフに初期化
G = nx.path_graph(5)

# 点5, 6を結ぶ線を追加
G.add_edge(5, 6)

nx.draw_networkx(G)
plt.show()