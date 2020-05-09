#slam.py
#This file will handle all slam related tasks
import pyrealsense2 as rs
import numpy as np
import time
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import visualization

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
        pass
    
class slam():
    def __init__(self):
        self.mastermap = mastermap()
        self.realsense = realsense()
    
if __main__ == 'main':
    slamobj = slam()
    print(slamobj.realsense.getcameradata())
