# -*- coding: utf-8 -*-
"""
Created on Thu May  2 21:55:15 2019

@author: 30517
"""

import math

def Ant(G0,HPBW,HPBW_back,FS,FB,FB_rest,n_side,n_back,ANG,TILT):
    
    for i in range(1,5001):
        if (((math.sin(90-(HPBW/2)))**(1/2))**(i/10)) >= 0.5:
            N = i
    
    for i in range(1,5001):
        if (((math.sin(90-(HPBW_back/2)))**(1/2))**(i/10)) >= 0.5:
            N_back = i
    
    q_side = 10**(FS/10)
    q_back = 10**(FB/10)
    q_back_rest = 10**(FB_rest/10)
    G_cal =  10**(G0)

    ANG_new = ANG + TILT
    
    if ANG_new >= 360:
        ANG_new = ANG_NEW - 360
    
    if TILT <= ANG_new + LIFT < = TILT + 180:
        if ((math.sin(ANG_new))**(1/2))**(N) >= math.fabs(math.sin(n_side*ANG_new))/(q_side):
            a = ((math.sin(ANG_new))**(1/2)) ** (N)
        else:
            a = math.fabs(math.sin(n_side*ANG_new))/(q_side)
    else:
        ANG_new = ANG + TILT
        if ((math.sin(ANG_new))**(1/2))**(N) >= math.fabs(math.sin(n_side*ANG_new))/(q_side):
            a = ((math.sin(ANG_new))**(1/2)) ** (N_back)
        else:
            a = math.fabs(math.sin(n_side*ANG_new))/(q_side)
    
    return G_cal * a


    
        

    
