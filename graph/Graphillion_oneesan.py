# 『フカシギの数え方』 おねえさんといっしょ！ みんなで数えてみよう！
# https://youtu.be/Q4gTV4r0zRs
# https://github.com/takemaru/graphillion/wiki

from graphillion import GraphSet
import graphillion.tutorial as tl  # チュートリアルのためのヘルパー・モジュール
import time

def oneesan(n=1, draw=False):
    universe = tl.grid(n, n)
    GraphSet.set_universe(universe)

    start = 1
    goal = (n + 1) * (n + 1)
    start_time = time.time()
    paths = GraphSet.paths(start, goal)
    elapsed_time = time.time() - start_time
    print("処理に{:,.6f}".format(elapsed_time) + "秒かかりました。")
    print("{} x {} の通り方は、{:,}通りあります。".format(n,n,paths.len()))  # 結果が大規模のときは paths.len() を使う

    if draw:
        tl.draw(universe)

if __name__ == '__main__':
    n = 12
    # oneesan(n)
    for i in range(1, n+1):
        if i < 9 or i%2 == 0:   # 9以上の奇数はなぜかメモリ不足になって実行できない
            oneesan(n=i, draw=False)
