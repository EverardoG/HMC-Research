# ## Problem 2:  green-screening!
#
# This question asks you to write one function that takes in two images:
#  + orig_image  (the green-screened image)
#  + new_bg_image (the new background image)
#
# It also takes in a 2-tuple (corner = (0,0)) to indicate where to place the upper-left
#   corner of orig_image relative to new_bg_image
#
# The challenge is to overlay the images -- but only the non-green pixels of
#   orig_image...
#

#
# Again, you'll want to borrow from hw7pr1 for
#  + opening the files
#  + reading the pixels
#  + create some helper functions
#    + defining whether a pixel is green is the key helper function to write!
#  + then, creating an output image (start with a copy of new_bg_image!)
#
# Happy green-screening, everyone! Include at least TWO examples of a background!
#
import numpy as np
from matplotlib import pyplot as plt
import cv2

# Here is a signature for the green-screening...
# remember - you will want helper functions!
def change_location( orig_image, new_bg_image, corner=(0,0) ):
    """This takes in two images and splices them together really poorly"""

    height1, width1, channels = orig_image.shape
    height2, width2, channels = new_bg_image.shape
    heights = [height1,height2]
    widths = [width1,width2]

    new_image = new_bg_image.copy()
    num_rows, num_cols, num_chans = new_image.shape
    for row in range(min(heights)):
        for col in range(min(widths)):
            r1, g1, b1 = orig_image[row,col]
            r2, g2, b2 = new_bg_image[row,col]
            if r1 < 80 and g1 >150 and b1 < 80:
                new_image[row,col] = [r2 , g2, b2 ]
            else:
                new_image[row,col] = [r1,g1,b1]

    return new_image

raw_background = cv2.imread('weird.jpg',cv2.IMREAD_COLOR)
background = cv2.cvtColor(raw_background, cv2.COLOR_BGR2RGB)

raw_foreground = cv2.imread('useful_thing.jpg',cv2.IMREAD_COLOR)
foreground = cv2.cvtColor(raw_foreground, cv2.COLOR_BGR2RGB)

new_image = change_location(foreground,background)
plt.imshow(new_image)
plt.show()
