import numpy as np


def F_Force_On_2(m1,r1,m2,r2,G):
    r_12 = r2 - r1
    F_21 = -G * m1 * m2 / np.linalg.norm(r_12)**3. * r_12
    return F_21
    
def F_Acceleration(F,m):
    return F/m

def F_Velocity(a,v0,dt):
    v = a*dt + v0
    return v


###############
G=6.674*10**-11
dt=1.
#
m1 =1.98892*10**30
r1 = np.asarray([0,0,0])
v0_1 = np.asarray([0,0,0])
#
m2=5.9722*10**24
r2=np.asarray([149600000000,0,0])
v0_2 = np.asarray([1,0,0])
###############################
# Determine force
F = F_Force_On_2(m1,r1,m2,r2,G)
print F
# Determine acceleration    
a1 = F_Acceleration(F,m1)
a2 = F_Acceleration(F,m2)
print a1
print a2

# Determine velocity    
v1 = F_Velocity(a1,v0_1,dt)
v2 = F_Velocity(a2,v0_2,dt)

print v1
print v2
