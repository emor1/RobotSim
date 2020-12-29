#シンプルに簡単な三角関数から手先位置を求めるシミュレーション

import matplotlib.pyplot as plt
import numpy as np
import sys

#点と線の描画、スケールの設定
def plotPoint_Line(link,xscl,yscl,*deg,N=1):
    x1=0
    y1=0
    degs=[]
    if N!=len(deg):
        print("Error\nDoes not match number of links and degrees")
        sys.exit()
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
    plt.text(0.5,y1+2,'Link Length:{link}'.format(link=link))
    #グラフのx軸とy軸のスケールをそれぞれ0から10に
    plt.xlim(0,xscl)
    plt.ylim(0,yscl)
    plt.show()

#原点
# origin=[0,0]
#リンクの長さ
link=3
#リンクの数
N=4
#回転角度
deg=[10,30,-20]


xscal=yscal=10  #scale
plotPoint_Line(link,xscal,yscal,*deg,N=N)


