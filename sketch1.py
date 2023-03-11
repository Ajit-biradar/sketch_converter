import numpy as np
import imageio
import scipy.ndimage
import cv2



img='samreen.jpg'


def ajit(rgb):
    return np.dot(rgb[...,:3],[0.2989,0.5879,0.1140])




def samreen(front,back):
    final_sketch = front*255/(255-back)
    final_sketch[back>255]=255
    return final_sketch.astype('uint8')



    

s=imageio.imread(img)
gray=ajit(s)

i=255-gray


blur=scipy.ndimage.filters.gaussian_filter(i,sigma=15)
r=samreen(blur,gray)



cv2.imwrite('sam-sketch.png',r)
