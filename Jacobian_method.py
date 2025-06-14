x,y,z,i=0,0,0,0
while True:
 i=i+1
 xn=(2.22+1.2*y-3.22*z)/4.63
 yn=(-3.17+3.07*x-2.11*z)/5.48
 zn=(5.11-1.26*x-3.11*y)/4.57
 print("x=",xn,'\ny=',yn,'\nz=',zn,'\ncount=',i,'\n\n')
 if abs(x-xn)<10**-4 and abs (y-yn)<10**-10 and (z-zn)<10**-4:
    exit()
 x=xn
 y=yn
 z=zn