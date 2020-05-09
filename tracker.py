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
cfg = rs.config()
cfg.enable_stream(rs.stream.pose)
pipeline.start(cfg)
#pipeline.start()
ls = []
import os

    
# This call waits until a new coherent set of frames is available on a device
# Calls to get_frame_data(...) and get_frame_timestamp(...) on a device will return stable values until wait_for_frames(...) is called
for i in range(1):
    frames = pipeline.wait_for_frames()
    pose_frame = frames.get_pose_frame()

    npobj = np.asanyarray(pose_frame.get_pose_data())
    data = pose_frame.get_pose_data()
    print("Frame #{}".format(pose_frame.frame_number))
    print("Position: {}".format(data.translation))
    print("Rotation: {}".format(data.rotation))
    print("Acceleration: {}\n".format(data.acceleration))
    print(type(data.rotation.y))
    print(data.rotation.y)
    time.sleep(0.25)
    #os.system('cls' if os.name == 'nt' else "printf '\033c'")
    
pipeline.stop()


    
    
    
        
