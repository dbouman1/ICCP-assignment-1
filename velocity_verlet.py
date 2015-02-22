# Import libraries
import numpy as np
# Import functions
from acceleration import acceleration
# Define velocity verlet function
def velocity_verlet(N, h, pos, v_0, a_0, L):
    v_half_h = np.add(v_0,0.5*a_0*h)
    # print v_half_h[1,2]
    pos_h = np.add(pos,v_half_h*h)
    # print pos_h[1,2]
    # Impose periodic boundary condition
    pos_h = np.where(pos_h<0,L+pos_h,pos_h)
    pos_h = np.where(pos_h>L, pos_h-L, pos_h) 
    # print pos_h[1,2]
    a_h,potential = acceleration(N, pos_h, L)
    #print a_h[1,2]
    # print a_h[1,2]
    v_h = np.add(v_half_h,(0.5*a_h*h))
    # print v_h[1,2]
    a_0 = a_h
    pos = pos_h
    v_0 = v_h
    # Impose periodic boundary condition
    pos = np.where(pos<0, L+pos, pos)
    pos = np.where(pos>L, pos-L, pos) 
    return [pos,v_0,a_0,potential];