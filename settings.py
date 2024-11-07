#settings

# velocity: m*s^-1
# position: m
# acceleration: ms^-2
# energy: joule
# temperature: K

import numpy as np

def init():
    global n
    n = 8
    global N
    N = n**3                 # total number of particles
    global nsteps            # number of time step to analyze
    nsteps = 2000
    global mass              # mass of the LJ particles (kg)
    mass = 105.5206e-27
    global kb                # boltzmann's constant (m^2*kg*s^-2*K^-1)
    kb =1.3806503e-23
    global Tdesired          # temperature of the experiment in K
    Tdesired = 300.
    global eps               # eps in LJ (kg*m^2*s^-2)
    eps = 0.5*kb*Tdesired
    
    
    global sigma             # sigma in LJ (m)
    sigma = 2.55e-10
    global cutoff            # cutoff arbitrary at 15 angstrom
    cutoff = 2.5*sigma
    global deltat            # time step (s)
    deltat = 1.e-15
    global faktor_rho
    faktor_rho = 0.5
    global rho
    rho = faktor_rho / sigma**3                 #in m^-3
    global p_L
    p_L = n / (sigma * rho**(1/3))              #dimensionless
    global Vol
    Vol = N / rho
    global L
    L = p_L * sigma                             #in m
    global a_lat
    a_lat = L / n                               #in m       


    global box

    class box:

        def __init__(self, xlo, xhi, ylo, yhi, zlo, zhi, lx, ly, lz):
            self.xlo = xlo
            self.xhi = xhi
            self.ylo = ylo
            self.yhi = yhi
            self.zlo = zlo
            self.zhi = zhi   

    # initialize box dimension in angstrom     
    box.xlo = 0.
    box.xhi = L
    box.ylo = 0.
    box.yhi = L
    box.zlo = 0.
    box.zhi = L
    box.lx = box.xhi - box.xlo
    box.ly = box.yhi - box.ylo
    box.lz = box.zhi - box.zlo
    
    

    global Energy    # class for energy (potential, kinetic)

    class Energy:
        def __init__(self, ep, ek, ekx, eky, ekz):
            self.ep = ep
            self.ek = ek
            self.ekx = ekx
            self.eky = eky
            self.ekz = ekz
    
    global debug
    debug = 0  # 1 == debug; 0 == no debug
    global Trescale
    Trescale = 1  # 1 == rescale velocity at desired temperature every xth step; 0 == no rescaling
    
    
# for vectorization

    global xi
    xi = np.zeros(shape=N)
    global yi
    yi = np.zeros(shape=N)
    global zi
    zi = np.zeros(shape=N)
    global vix
    vix = np.zeros(shape=N)
    global viy
    viy = np.zeros(shape=N)
    global viz
    viz = np.zeros(shape=N)
    global sumfix
    sumfix = np.zeros(shape=N)
    global sumfiy
    sumfiy = np.zeros(shape=N)
    global sumfiz
    sumfiz = np.zeros(shape=N)
    

    
