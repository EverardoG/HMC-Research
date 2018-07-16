#
# coding: utf-8
#
# hw8pr1.py - the k-means algorithm -- with pixels...
#

# import everything we need...
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import utils
import cv2
import numpy as np

def fried_chicken_or_doggo():
    #Fried Chicken or Doggo?
    # choose an image...
    # IMAGE_NAME = "./jp.png"  # Jurassic Park
    # IMAGE_NAME = "./batman.png"
    # IMAGE_NAME = "./hmc.png"
    # IMAGE_NAME = "./thematrix.png"
    # IMAGE_NAME = "./fox.jpg"
    IMAGE_NAME = "./doggo.jpeg"
    image = cv2.imread(IMAGE_NAME, cv2.IMREAD_COLOR)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # reshape the image to be a list of pixels
    image_pixels = image.reshape((image.shape[0] * image.shape[1], 3))

    # # choose k (the number of means) in  NUM_MEANS
    # # and cluster the pixel intensities
    #
    # NUM_MEANS = 5
    # clusters = KMeans(n_clusters = NUM_MEANS)
    # clusters.fit(image_pixels)
    #
    # # After the call to fit, the key information is contained
    # # in  clusters.cluster_centers_ :
    # count = 0
    # for center in clusters.cluster_centers_:
    #     print("Center #", count, " == ", center)
    #     # note that the center's values are floats, not ints!
    #     center_integers = [int(p) for p in center]
    #     print("   and as ints:", center_integers)
    #     count += 1
    #
    # # build a histogram of clusters and then create a figure
    # # representing the number of pixels labeled to each color
    # hist = utils.centroid_histogram(clusters)
    # bar = utils.plot_colors(hist, clusters.cluster_centers_)
    #
    #
    # # in the first figure window, show our image
    plt.figure()
    plt.axis("off")
    plt.imshow(image)

    bars = []
    for i in range(4):
        NUM_MEANS = 3 + i
        clusters = KMeans(n_clusters = NUM_MEANS)
        clusters.fit(image_pixels)
        count = 0
        for center in clusters.cluster_centers_:
            center_integers = [int(p) for p in center]
            count += 1
        hist = utils.centroid_histogram(clusters)
        bar = utils.plot_colors(hist, clusters.cluster_centers_)
        bars.append(bar)
    # in the second figure window, show the pixel histograms
    #   this starter code has a single value of k for each
    #   your task is to vary k and show the resulting histograms
    # this also illustrates one way to display multiple images
    # in a 2d layout (fig == figure, ax == axes)
    #
    num_rows = 2
    num_cols = 4
    fig, ax = plt.subplots(nrows=num_rows, ncols=num_cols, sharex=False, sharey=False)
    titles = []
    i=0
    for bar in bars:
        title = str(i+3)+" means"
        titles.append(title)
        i+=1

    ax[0,0].imshow(bars[0]);    ax[0,0].set_title(titles[0])
    ax[0,1].imshow(bars[1]);    ax[0,1].set_title(titles[1])
    ax[1,0].imshow(bars[2]);    ax[1,0].set_title(titles[2])
    ax[1,1].imshow(bars[3]);    ax[1,1].set_title(titles[3])

    IMAGE_NAME = "./legs.jpg"
    image = cv2.imread(IMAGE_NAME, cv2.IMREAD_COLOR)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # reshape the image to be a list of pixels
    image_pixels = image.reshape((image.shape[0] * image.shape[1], 3))

    plt.figure()
    plt.axis("off")
    plt.imshow(image)

    bars = []
    for i in range(4):
        NUM_MEANS = 3 + i
        clusters = KMeans(n_clusters = NUM_MEANS)
        clusters.fit(image_pixels)
        count = 0
        for center in clusters.cluster_centers_:
            center_integers = [int(p) for p in center]
            count += 1
        hist = utils.centroid_histogram(clusters)
        bar = utils.plot_colors(hist, clusters.cluster_centers_)
        bars.append(bar)
    # in the second figure window, show the pixel histograms
    #   this starter code has a single value of k for each
    #   your task is to vary k and show the resulting histograms
    # this also illustrates one way to display multiple images
    # in a 2d layout (fig == figure, ax == axes)
    #

    titles = []
    i=0
    for bar in bars:
        title = str(i+3)+" means"
        titles.append(title)
        i+=1

    ax[0,2].imshow(bars[0]);    ax[0,2].set_title(titles[0])
    ax[0,3].imshow(bars[1]);    ax[0,3].set_title(titles[1])
    ax[1,2].imshow(bars[2]);    ax[1,2].set_title(titles[2])
    ax[1,3].imshow(bars[3]);    ax[1,3].set_title(titles[3])




    for row in range(num_rows):
        for col in range(num_cols):
            ax[row,col].axis('off')
    plt.show(fig)

def posterize():
    IMAGE_NAME = "./mffn.jpg"
    image = cv2.imread(IMAGE_NAME, cv2.IMREAD_COLOR)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # reshape the image to be a list of pixels
    image_pixels = image.reshape((image.shape[0] * image.shape[1], 3))

    NUM_MEANS = 5
    clusters = KMeans(n_clusters = NUM_MEANS)
    clusters.fit(image_pixels)
    count = 0
    for center in clusters.cluster_centers_:
        center_integers = [int(p) for p in center]
        count += 1
    hist = utils.centroid_histogram(clusters)
    bar = utils.plot_colors(hist, clusters.cluster_centers_)
    # print(clusters.cluster_centers_)
    plt.figure()
    plt.axis("off")
    plt.imshow(image)

    height,width,channels = image.shape
    poster = image.copy()
    for row in range(height):
        for col in range(width):
            distances = []
            for point in clusters.cluster_centers_:
                r,g,b = image[row,col]
                distances.append(np.sqrt( (point[0]-r)**2 + (point[1]-g)**2 + (point[2]-b)**2 ) )
            min_distance_ind = distances.index(min(distances))
            # print(distances)
            # print(min_distance_ind)
            poster[row,col] = clusters.cluster_centers_[min_distance_ind]
    plt.figure()
    plt.axis('off')
    plt.imshow(poster)
    plt.show()
posterize()

#
# comments and reflections on hw8pr1, k-means and pixels
"""
 + Which of the paths did you take:
    + posterizing or
    + algorithm-implementation

 + How did it go?  Which file(s) should we look at?
 + Which function(s) should we try...
"""
#
#
