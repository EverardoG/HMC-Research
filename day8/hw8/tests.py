from hw8pr1 import *


raw_image1 = cv2.imread('g_dawg.jpeg',cv2.IMREAD_COLOR)
image1 = cv2.cvtColor(raw_image1,cv2.COLOR_RGB2BGR)

raw_image2 = cv2.imread('yoda.jpeg',cv2.IMREAD_COLOR)
image2 = cv2.cvtColor(raw_image2,cv2.COLOR_RGB2BGR)

try_two_image_filter(image2,image1)
