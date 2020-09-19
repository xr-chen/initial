import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
import matplotlib.animation as animation

fun=lambda x,y:np.exp(-((x-3)**2+y**2)/2)+np.exp(-((x+3)**2+y**2)/2)#概率密度函数

x,y=sp.symbols('x,y')
prob=sp.exp(-((x-3)**2+y**2)/2)+sp.exp(-((x+3)**2+y**2)/2)
U=-sp.log(prob)
Ux=sp.diff(U,x)
Uy=sp.diff(U,y)
gradU=np.vectorize(sp.lambdify([x,y],[Ux,Uy],'numpy'))#把求导结果转化为匿名函数
U=sp.lambdify([x,y],U,'numpy')

Mass=1
iterations=5000
stepsize=0.1
p=np.zeros([iterations,2])
q=np.zeros([iterations,2])
q[0,:]=[-1.5,0.75]

def HMC(U1,grad_U,epsilon,L,current_q):
    q = current_q
    p = np.random.normal(0,1,q.shape)
    current_p = p
    p = p - (epsilon/2) * grad_U(q[0],q[1])

    for i in range(1,L):
        q = q + epsilon * p
        if i!=L-1:
            p = p - epsilon * grad_U(q[0],q[1])
    
    p = p - (epsilon/2) * grad_U(q[0],q[1])
    p = -p
    current_U=U1(current_q[0],current_q[1])
    current_K=np.sum(current_p**2)/2
    proposed_U=U1(q[0],q[1])
    proposed_K=np.sum(p**2)/2

    if np.random.uniform(0,1)<np.min([1,np.exp(current_U-proposed_U+current_K-proposed_K)]):
        return q
    else:
        return current_q


for i in range(1,iterations):
    q[i,:]=HMC(U,gradU,stepsize,20,q[i-1,:])

accept_rate=len(set(q[:,1]))/q.shape[0]
    
x1=np.linspace(-6,6,1000)
y1=np.linspace(-4,4,1000)
[X,Y]=np.meshgrid(x1,y1)

fig, ax = plt.subplots()
xdata, ydata = [], []
ln, = plt.plot([], [], '+',markersize=3,animated=True)
#plt.plot(q[:,0],q[:,1],'+',markersize=1)

def init():
    ax.set_xlim(-6,6)
    ax.set_ylim(-4,4)
    return ln,

def update(frame):
    xdata.append(q[frame:frame+99,0])
    ydata.append(q[frame:frame+99,1])
    ln.set_data(xdata, ydata)
    return ln,

plt.title('accept rate'+str(accept_rate))
plt.contour(X,Y,fun(X,Y))
anim = animation.FuncAnimation(fig, update, frames=range(0,iterations,100),interval=30,
                   init_func=init,blit=True)

#anim.save('hmcguass3.gif',writer='imagemagick')
plt.show()
