import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.animation import FuncAnimation, PillowWriter
from mpl_toolkits.mplot3d import Axes3D

class mesh3D:
    def __init__(self,expression,xrange,yrange):
        self.expression=expression
        self.xlow=xrange[0]
        self.xsub=xrange[1]
        self.ylow=yrange[0]
        self.ysub=yrange[1]
        self.detail=1000
    
    def mesh(self):
        ax3 = plt.axes(projection='3d')
        xx = np.linspace(self.xlow,self.xsub,self.detail)
        yy = np.linspace(self.ylow,self.ysub,self.detail)
        X, Y = np.meshgrid(xx, yy)
        Z = self.expression(X,Y)
        ax3.plot_surface(X,Y,Z,cmap='rainbow')
        plt.show()
        
    def set(self,detail):
        self.detail=detail

if __name__=='__main__':
    f1=mesh3D(lambda x,y:x*y,[-10,10],[-10,10])
    f1.mesh()