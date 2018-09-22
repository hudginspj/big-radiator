from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
from matplotlib import style
import dummystep as dt
import time
import matplotlib.animation as ani
style.use('ggplot')

fig = plt.figure()
ax1 = fig.add_subplot(111, projection='3d')
def animate(a):
    xs = []
    ys = []
    zs = []
    data = dt.step()
    for i in data:
        values = data[i]
        x = values['x']
        y = values['y']
        z = values['z']
        xs.append(x)
        ys.append(y)
        zs.append(z)
        ax1.set_xlabel('x axis')
        ax1.set_ylabel('y axis')
        ax1.set_zlabel('z axis')
    ax1.scatter(x, y, z, c='g', marker='o')
    print(xs[0])
    #ax1.clear()
   # ax1.scatter(xs, ys, zs, c='g', marker='o')

gr = ani.FuncAnimation(fig, animate, interval=1000)
ax1.set_xlabel('x axis')
ax1.set_ylabel('y axis')
ax1.set_zlabel('z axis')
plt.show()

'''

while 1:
    data = dt.step()
    for i in data:
        values = data[i]
    x = values['x']
    y = values['y']
    z = values['z']
    print(x)
    print(y)
    print(z)
    ax1.scatter(x, y, z, c='g', marker='o')
    ax1.set_xlabel('x axis')
    ax1.set_ylabel('y axis')
    ax1.set_zlabel('z axis')
    plt.show()
    time.sleep(1)
'''