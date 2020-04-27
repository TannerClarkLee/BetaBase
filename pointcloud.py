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
import visualization




#Testing

a2 = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])
print(a2[0:1])
#raise Exception



# Create a context object. This object owns the handles to all connected realsense devices
pipeline = rs.pipeline()
pipeline.start()
#pipeline.start()
ls = []
for i in range(0,1):
    print(i)
    
    # This call waits until a new coherent set of frames is available on a device
    # Calls to get_frame_data(...) and get_frame_timestamp(...) on a device will return stable values until wait_for_frames(...) is called
    frames = pipeline.wait_for_frames()
    depth_frame = frames.get_depth_frame()
    
    theta = 0.138
    npobj2 = np.asanyarray(depth_frame.get_data())
    st = time.time()
    #get average of columns excluding 0
    
    slimframe = npobj2[200:280]
    start_avg = time.time()
    columnaverage = visualization.depth_frametodarray(slimframe,80)
    print(len(columnaverage))
    end_avg_start_cords = time.time()
    cords = visualization.darraytogrid(columnaverage,theta)
    
    print('Time Column Average: ', end_avg_start_cords-start_avg)
    print('Time Cords : ', time.time()-end_avg_start_cords)
    
    end = time.time()
    print(end-st)
    #print(columnaverage)
    x,y=[],[]
    for item in cords:
        x.append(item[0])
        y.append(item[1])
    
    plt.matshow(npobj2[0:640], cmap='Blues')
    plt.show()





plt.scatter(x, y)
plt.show()


    
    
def init():
    line.set_data([], [])
    return line,
    
    
    
pipeline.stop()
    
    #import numpy as np
    #import matplotlib.pyplot as plt

    #x = np.array([[1,0],[0,1]])
    #plt.matshow(npobj, cmap='Blues')
    #plt.show()
    
    #fig = plt.figure()
    #ax = fig.add_subplot(111, projection='3d')
    #ax.scatter(x, y, z, c='r', marker='o')
    #plt.show()

    
    
    
        
