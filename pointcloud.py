## License: Apache 2.0. See LICENSE file in root directory.
## Copyright(c) 2015-2017 Intel Corporation. All Rights Reserved.

#####################################################
## librealsense tutorial #1 - Accessing depth data ##
#####################################################

# First import the library
import pyrealsense2 as rs
import numpy as np
import time
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import visualization

# Create a context object. This object owns the handles to all connected realsense devices
pipeline = rs.pipeline()
pipeline.start()
#pipeline.start()
ls = []
def run_depthframes(i):
    
    # This call waits until a new coherent set of frames is available on a device
    # Calls to get_frame_data(...) and get_frame_timestamp(...) on a device will return stable values until wait_for_frames(...) is called
    frames = pipeline.wait_for_frames()
    depth_frame = frames.get_depth_frame()
    
    theta = 0.138
    npobj2 = np.asanyarray(depth_frame.get_data())
    
    #get average of columns excluding 0
    slimframe = npobj2[200:280]
    
    columnaverage = visualization.depth_frametodarray(slimframe,80)
    
    cords = visualization.darraytogrid(columnaverage,theta)
    
    x,y=[],[]
    for item in cords:
        x.append(item[0])
        y.append(item[1])
    
    
    plt.cla()
    plt.scatter(x, y)

ani = FuncAnimation(plt.gcf(),run_depthframes,interval = 100)
plt.tight_layout()
plt.show()
    
    
pipeline.stop()


    
    
    
        
