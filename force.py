import settings
import numpy as np


def forceLJvec():
        
    # Position Matrix creation
    xi=np.transpose(np.multiply(np.ones(shape=(settings.N,settings.N)),settings.xi))
    xit=np.transpose(xi)
    yi=np.transpose(np.multiply(np.ones(shape=(settings.N,settings.N)),settings.yi))
    yit=np.transpose(yi)
    zi=np.transpose(np.multiply(np.ones(shape=(settings.N,settings.N)),settings.zi))
    zit=np.transpose(zi)
    
    # Position Matrix creation
    xij = xi - xit
    yij = yi - yit
    zij = zi - zit
    
    # Periodic Boundary Condition Adjustment    
    xijpbc = np.where(np.abs(xij) > 0.5*settings.box.lx, xij-np.sign(xij)*settings.box.lx, xij)
    yijpbc = np.where(np.abs(yij) > 0.5*settings.box.ly, yij-np.sign(yij)*settings.box.ly, yij)
    zijpbc = np.where(np.abs(zij) > 0.5*settings.box.lz, zij-np.sign(zij)*settings.box.lz, zij)
    
    # Squared Distance calculation
    R2 = np.multiply(xijpbc,xijpbc) + np.multiply(yijpbc,yijpbc) + np.multiply(zijpbc,zijpbc)
    
    # Account for the vanishing diagonal
    R2 += 1.0e10*np.identity(settings.N)
    
    oneoverR2 = np.reciprocal(R2)
    rc2overR2 = settings.sigma *settings.sigma * oneoverR2 # r_c^2 /rij^2
    
    rc6overR6 = np.multiply(np.multiply(rc2overR2, rc2overR2),rc2overR2)
    
    aa = rc6overR6 - np.ones(shape=(settings.N,settings.N))
    
    # Potential calculation
    fpot = 4.0*settings.eps*(np.multiply(rc6overR6, aa))
    
    # Force calculation
    fforce0 = 48.0*settings.eps * np.multiply(rc6overR6, rc6overR6 - 0.5*np.ones(shape=(settings.N, settings.N)))
    fforce = np.multiply(fforce0, oneoverR2)
    
    # Return vanishing Force above distance cutoff threshhold
    fforcecut = np.where(R2 > settings.cutoff*settings.cutoff, np.zeros(shape=(settings.N, settings.N)), fforce)
    
    # Return vanishing Potential above distance cutoff threshhold
    epotij = np.where(R2 > settings.cutoff*settings.cutoff, np.zeros(shape=(settings.N, settings.N)), fpot)
    eptiju = np.triu(epotij, 0)
    
    # Update potential energy
    settings.Energy.ep = np.sum(eptiju)
    
    
    # Calculate Force in each cartesian direction
    fijx = -np.multiply(fforcecut, xijpbc)
    fijy = -np.multiply(fforcecut, yijpbc)
    fijz = -np.multiply(fforcecut, zijpbc)
    
    
    # Force summation
    settings.sumfix = np.sum(fijx,axis=0)
    settings.sumfiy = np.sum(fijy,axis=0)
    settings.sumfiz = np.sum(fijz,axis=0)
    
