import numpy as np
import matplotlib.pyplot as plt
from celluloid import Camera
from matplotlib import animation

class system:
    Particles=[]
    time=0
    dt=1e-1
    def __init__(self,name,posx,posy,velx,vely,mass):
        if name in system.Particles:
            return NameError
        system.Particles.append(name)
        self.mass=mass
        self.pos=np.array([posx,posy])
        self.velocity=np.array([velx,vely])
  
    def position_vector(x,y):
        pass
    def force(x):
        forcee=-40*x.mass/np.linalg.norm(x.pos)**3*x.pos
        return forcee
    def attraction_force(self):
        attraction_force=0
        for x in system.Particles:
            if x!=id(self):
                new_attraction_force=-4*self.mass*x.mass/np.linalg.norm(x.pos-self.pos)**3*(self.pos-x.pos)
            attraction_force+=new_attraction_force
            print(self.pos)
        return attraction_force
    def updater(self):
        self.velocity=self.velocity+(system.force(self)+self.attraction_force())*system.dt/self.mass
        self.pos=self.pos+self.velocity*system.dt
    def runner(x,t):
        duration=int(t)
        positionx=[]
        positiony=[]
        time=[]
        for i in range (int(duration)):
            x.updater()
            positionx+=[x.pos[0]]
            positiony+=[x.pos[1]]
            time+=[i]
        return positionx,positiony,time

body1=system(10,10,1,0,1,name='vinuu')
body2=system(19,2,0,0.1,0.4,name='vinu')
x1,y1,t1=system.runner(body1,40)
x2,y2,t2=system.runner(body2,40)


plt.plot(x1,y1,'blue')
plt.plot(x2,y2,'red')
plt.show()


'''
camera=Camera(plt.figure())
for x,y in zip(x_range,y_range):
    plt.scatter(0,0,c='orange',s=40)
    plt.plot(x_range,y_range,lw=0.5,c='black')
    plt.scatter(x,y,c='black',s=20)
    camera.snap()

anime=camera.animate(interval=1e-6)
plt.show()

plt.scatter(x_range,y_range)
plt.show()

fig,ax=plt.subplots()

scatter1=ax.scatter(0,0,c='r')
scatter=ax.scatter(x_range,y_range,c='b')
def update(i,x_range,y_range,scatter):
    scatter.set_data(x_range[i],y_range[i])
    return scatter,
ani = animation.FuncAnimation(fig, update, len(x_range), interval=1, 
                              fargs=[x_range, y_range, scatter], blit=True)
plt.show()
'''