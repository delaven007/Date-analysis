
#线框图

import numpy as np
import matplotlib.pyplot as mp
from mpl_toolkits.mplot3d import axes3d
n=500
#生成网格化坐标矩阵
x,y=np.meshgrid(np.linspace(-3,3,n),np.linspace(-3,3,n))
# 根据每个网格点坐标，通过某个公式计算z高度坐标
z=(1 - x/2 + x**5 + y**3) * np.exp(-x**2 - y**2)            #(1+x/2+x**5+y**3)* e**-x**2-y**2

mp.figure("3D Contour",facecolor='orange')
ax3d=mp.gca(projection='3d')
ax3d.plot_wireframe(x,y,z,cstride=10,rstride=10,cmap='jet')

#设置紧凑布局
# mp.tight_layout()
mp.show()


