#Project a point from 3D to 2D using a matrix operation

# Given: Point p in 3-space [x y z], and focal length f
#Return: Location of projected point on 2D image plane [u v]
import numpy as np


def project_point(p, f):
    #Homogeneous Matrix
    h=np.array([[f,0,0,0],
        [0,f,0,0],
        [0,0,1,0]])
    project = np.matmul(h,np.array(p))
    return project
p = [[20],[100],[200],[1]]
f = 50
ans = project_point(p,f)
u = ans[0]/ans[2]
v = ans[1]/ans[2]
print(u,v)
    
