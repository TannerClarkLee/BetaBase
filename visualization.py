#visualization packages
import math
import numpy as np

rounditemconfig = 1
def darraytogrid(A,theta):
    '''
    This function will create a set of coordinates from a list A centered around 0.
    theta is the distance between each pixel
    '''
    returnlist = {}
    
    def sas(s1,a,s2):
        '''
        This function will take in SAS from law of cosines and return the side b.
        '''
        b = math.sqrt((s1**2 + s2**2)-(2*s1*s2*math.cos(math.radians(a))))
        
        return b
    
    def saa(s,a1,a2):
        '''
        This function will take in SAA from law of cosines and return the side b.
        '''
        b =     (s/math.sin(math.radians(a1)))*math.sin(math.radians(a2))
        
        return b
        
    centerpixel = len(A)//2
    centerdistance = (A[centerpixel]+A[centerpixel-1]+A[centerpixel+1]+A[centerpixel+2]+A[centerpixel-2])/5
    if centerdistance == 0:
        return
    for i in range(0,len(A)):
        distfromcenter = centerpixel-i #y coordinate before applying theta
        
        abstheta = (distfromcenter*theta)
        
        dist = A[i]
        if dist==0:
            continue
        
        #Add occupancy item of 1 (something there)
        y = round(saa(dist,90,abstheta)/1000,rounditemconfig)
        if np.isnan(y):
            continue
        x = round(math.sqrt(dist**2 - y**2)/1000,rounditemconfig)
        returnlist.update({(x,y):1})
        #Add occupancy item of 0 (nothing there)
        unocciter = math.floor((dist/1000)/0.1)
        for j in range(unocciter):
            dist_unocc = dist-((j+1)*100)
            y = round(saa(dist_unocc,90,abstheta)/1000,rounditemconfig)
            if np.isnan(y):
                continue
            x = round(math.sqrt(dist_unocc**2 - y**2)/1000,rounditemconfig)
            returnlist.update({(x,y):0})
    return returnlist
            
        
        
        
def depth_frametodarray(depthframe,numofrows):
    columnaverage = np.true_divide(depthframe.sum(0),(depthframe!=0).sum(0))
    return columnaverage


        
        
        