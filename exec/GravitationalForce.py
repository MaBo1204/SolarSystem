import numpy as np


def F_Force_On_2(m1,r1,m2,r2,G):
    r_12 = r2 - r1
    F_21 = -G * m1 * m2 / np.linalg.norm(r_12)**3. * r_12
    return F_21
    
    
G=6.674*10**-11

m1=1.
r1=np.asarray([0,0,0])

m2=2.
r2=np.asarray([0,0,10])

print F_Force_On_2(m1,r1,m2,r2,G)
