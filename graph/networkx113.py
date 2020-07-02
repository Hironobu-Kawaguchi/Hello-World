import networkx as nx
import matplotlib.pyplot as plt


#　一繋ぎの5個の点を持つグラフに初期化
G = nx.path_graph(5)

# 点5, 6を結ぶ線を追加
G.add_edge(5, 6)

# ここに(1, 5)を結ぶ線を追加してください
G.add_edge(1, 5)

# ノードを描画する位置を決める
pos = nx.spring_layout(G)

# 描画
nx.draw_networkx(G, pos)
plt.show()