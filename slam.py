#slam.py
#This file will handle all slam related tasks
import pyrealsense2 as rs
import numpy as np
import time
import math
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import visualization
import os
class realsense():
    def __init__(self):
        self.pipelinedepth = rs.pipeline()
        cfg = rs.config()
        cfg.enable_stream(rs.stream.depth)
        self.pipelinedepth.start(cfg)
        
        self.pipelinepose = rs.pipeline()
        cfg = rs.config()
        cfg.enable_stream(rs.stream.pose)
        self.pipelinepose.start(cfg)

    def getcameradata(self):
        '''Returns trackingdata,depthcordinates'''
        depthframes = self.pipelinedepth.wait_for_frames()
        poseframes = self.pipelinepose.wait_for_frames()
        depth_frame = depthframes.get_depth_frame()
        pose_frame = poseframes.get_pose_frame()
        posedata = pose_frame.get_pose_data()
        
        #trackingdata
        transx = round(posedata.translation.x,5)
        transy = round(posedata.translation.y,5)
        roty = round(posedata.rotation.y,5)
        
        trackingdict = {"Translation":{"x":transx,"y":transy},"Rotation":{"y":roty}}
        
        theta = 0.138
        npobj2 = np.asanyarray(depth_frame.get_data())
        #get average of columns excluding 0
        slimframe = npobj2[200:280]
        columnaverage = visualization.depth_frametodarray(slimframe,80)
        cords = visualization.darraytogrid(columnaverage,theta)
        
        return trackingdict,cords
    
    def stop():
        self.pipeline.stop()

class mastermap():
    def __init__(self,mapinst=None):
        self.map={}
    def updatemap(self,newmap):
        self.map.update(newmap)
        
class slam():
    def __init__(self):
        self.mastermap = mastermap()
        self.realsense = realsense()
    def restoremastermap():
        pass
    
    def currentmaptomastermap(self,datafromcamera):
        transx,transy = datafromcamera[0]['Translation']['x'],datafromcamera[0]['Translation']['y']
        rot = datafromcamera[0]['Rotation']['y']
        rotdeg = 180*rot
        translateddict = {}
        os.system('cls' if os.name == 'nt' else "printf '\033c'")
        print('Mapping Object')
        theta = math.radians(rotdeg)
        cs = math.cos(theta)
        sn = math.sin(theta)
        print(theta,rotdeg,cs,sn)
        
        for key,value in datafromcamera[1].items():
            
            x,y = key[0],key[1]
            
            px = ((x * cs) - (y * sn))+transx
            py = ((x * sn) + (y * cs))+transy
            
            translateddict.update({(round(px,1),round(py,1)):value})
        
        
        self.mastermap.updatemap(translateddict)
        
        
        
    
if __name__ == '__main__':
    slamobj = slam()
    slamobj.currentmaptomastermap(slamobj.realsense.getcameradata())
    
    def run_depthframes(i):
        print('starting. dont move')
        slamobj.currentmaptomastermap(slamobj.realsense.getcameradata())
        print('done processing item. Now move')
        x,y,col=[],[],[]
        cords = slamobj.mastermap.map
        for keys,value in cords.items():
            if value==0:
                continue
            x.append(keys[0])
            y.append(keys[1])
    
    
    
        plt.cla()
        plt.scatter(x, y)

    ani = FuncAnimation(plt.gcf(),run_depthframes,interval = 100)
    plt.tight_layout()
    plt.show()
    
