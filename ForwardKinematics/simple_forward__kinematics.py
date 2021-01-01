#シンプルに簡単な三角関数から手先位置を求めるシミュレーション

import matplotlib.pyplot as plt
import numpy as np
import sys

fig, ax = plt.subplots(figsize=(8,8))

#点と線の描画、スケールの設定
def plotPoint_Line(link,xscl,yscl,*deg):
    x1=0
    y1=0
    degs=[]
    N=len(deg)
    # if N>len(deg):
        # print("Error")
        # sys.exit()
    for link_num in range(0,N):
        degs.append(deg[link_num])
        #xとyの位置を計算
        x=link*np.cos(np.radians(sum(degs)))
        y=link*np.sin(np.radians(sum(degs)))
        #点と線の描画
        plt.plot([x1,x1+x],[y1,y1+y],marker='.',markersize=20)
        #リンクの名前
        plt.text((2*x1+x)/2+0.5,(2*y1+y)/2-0.2,'Link{N}, Deg:{deg}'.format(N=link_num+1,deg=deg[link_num]))
        x1=x+x1
        y1=y+y1
    plt.text(x1-0.1,y1+0.5,'(X:{x},Y:{y})'.format(x=round(x1,1),y=round(y1,1)))
    plt.text(0.5,yscal-2,'Link Length:{link}'.format(link=link))
    #グラフのx軸とy軸のスケールをそれぞれ0から10に
    plt.xlim(0,xscl)
    plt.ylim(0,yscl)

#原点
# origin=[0,0]
#リンクの長さ
link=2
#回転角度
deg=[60,-40,40]
xscal=yscal=link*len(deg)  #scale
plotPoint_Line(link,xscal,yscal,*deg)
plt.grid(True)
plt.show()