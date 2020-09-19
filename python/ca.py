import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.animation import FuncAnimation, PillowWriter
from mpl_toolkits.mplot3d import Axes3D

z=lambda x,y:np.exp(-((x-3)**2+y**2)/2)+np.exp(-((x+3)**2+y**2)/2)

def mh(T,gamma,func):
    t=0
    pi=np.zeros(shape=(T,2))
    pi[0,0]=1.5
    pi[0,1]=-0.75    #设置起始点
    while t < T-1:
        t = t + 1
        a=pi[t-1,0]
        b=pi[t-1,1]
        mean = np.array([a,b])              # 均值
        conv = np.array([[gamma**2, 0.0],        # 协方差矩阵
                    [0.0, gamma**2]])
        pi_star = np.random.multivariate_normal(mean=mean, cov=conv, size=1)
        alpha = min(1, (func(pi_star[0,0],pi_star[0,1]) / func(pi[t - 1,0],pi[t-1,1])))
        u = np.random.uniform(0, 1)
        if u < alpha:
            pi[t,0] = pi_star[0,0]
            pi[t,1] = pi_star[0,1]
            
        else:
            pi[t,0] = pi[t - 1,0]
            pi[t,1] = pi[t - 1,1]
    print(len(set(pi[:,0])),len(pi[:,0]))
    rate=len(set(pi[:,0]))/(pi[:,0].size)
    return pi,rate

[pi,rate]=mh(5000,0.3,z)

def makefigure(pi,gamma,rate,func):
    x=np.linspace(-10,10,1000)
    y=np.linspace(-4,4,1000)
    x1,y1=np.meshgrid(x,y)

    fig, ax = plt.subplots()
    xdata, ydata = [], []
    ln, = plt.plot([], [], '+',markersize=3,animated=True)
    #plt.plot(q[:,0],q[:,1],'+',markersize=1)

    def init():
        ax.set_xlim(-10,10)
        ax.set_ylim(-4, 4)
        return ln,

    def update(frame):
        xdata.append(pi[frame:frame+99,0])
        ydata.append(pi[frame:frame+99,1])
        ln.set_data(xdata, ydata)
        return ln,

    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('accept rate:'+str(round(rate*100,2))+'%')
    plt.contour(x1,y1,func(x1,y1))
    anim = animation.FuncAnimation(fig, update, frames=range(0,5000,100),interval=30,
                    init_func=init,blit=True)

    #anim.save('mhgauss5.gif',writer='imagemagick')
    plt.show()

makefigure(pi,1,rate,z)