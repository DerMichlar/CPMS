import settings
import force
import numpy as np



def VelocityVerletVec():
    
    
    

    # update the position at t+dt
    settings.xi += settings.vix * settings.deltat + settings.sumfix * settings.deltat * settings.deltat *0.5 / settings.mass
    settings.yi += settings.viy * settings.deltat + settings.sumfiy * settings.deltat * settings.deltat *0.5 / settings.mass
    settings.zi += settings.viz * settings.deltat + settings.sumfiz * settings.deltat * settings.deltat *0.5 / settings.mass
    
    # save the force at t
    sumfixati = settings.sumfix
    sumfiyati = settings.sumfiy
    sumfizati = settings.sumfiz
    
    # update acceleration at t+dt
    force.forceLJvec()
    
    # update the velocity
    settings.vix += 0.5*settings.deltat *(settings.sumfix + sumfixati) / settings.mass
    settings.viy += 0.5*settings.deltat *(settings.sumfiy + sumfiyati) / settings.mass
    settings.viz += 0.5*settings.deltat *(settings.sumfiz + sumfizati) / settings.mass
    


def KineticEneryVec():
    
    
    mass = settings.mass
    
    settings.Energy.ekx = 0.5*mass * np.sum(np.multiply(settings.vix, settings.vix) )
    settings.Energy.eky = 0.5*mass * np.sum(np.multiply(settings.viy, settings.viy) )
    settings.Energy.ekz = 0.5*mass * np.sum(np.multiply(settings.viz, settings.viz) )
    
    settings.Energy.ek = settings.Energy.ekx + settings.Energy.eky + settings.Energy.ekz
    