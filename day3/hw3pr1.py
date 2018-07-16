#
# hw3pr1.py
#
#  lab problem - matplotlib tutorial (and a bit of numpy besides...)
#
# this asks you to work through the first part of the tutorial at
#     www.labri.fr/perso/nrougier/teaching/matplotlib/
#   + then try the scatter plot, bar plot, and one other kind of "Other plot"
#     from that tutorial -- and create a distinctive variation of each
#
# include screenshots or saved graphics of your variations of those plots with the names
#   + plot_scatter.png, plot_bar.png, and plot_choice.png
#
# Remember to run  %matplotlib  at your ipython prompt!
#

#
# in-class examples...
#

def inclass1():
    """
    Simple demo of a scatter plot.
    """
    import numpy as np
    import matplotlib.pyplot as plt


    N = 50
    x = np.random.rand(N)
    y = np.random.rand(N)
    colors = np.random.rand(N)
    area = np.pi * (15 * np.random.rand(N))**2  # 0 to 15 point radiuses

    plt.scatter(x, y, s=area, c=colors, alpha=0.5)
    plt.show()



#
# First example from the tutorial/walkthrough
#


#
# Feel free to replace this code as you go -- or to comment/uncomment portions of it...
#

def example1():
    import numpy as np
    import matplotlib.pyplot as plt
    import matplotlib.cm as cm

    X = np.linspace(-np.pi, np.pi, 256, endpoint=True)
    C,S = np.cos(X), np.sin(X)

    plt.plot(X,C)
    plt.plot(X,S)

    plt.show()






#
# Here is a larger example with many parameters made explicit
#

def example2():
    import numpy as np
    import matplotlib.pyplot as plt
    import matplotlib.cm as cm

    # Create a new figure of size 8x6 points, using 100 dots per inch
    plt.figure(figsize=(8,6), dpi=80)

    # Create a new subplot from a grid of 1x1
    plt.subplot(111)

    X = np.linspace(-np.pi, np.pi, 256,endpoint=True)
    C,S = np.cos(X), np.sin(X)

    # Plot cosine using blue color with a continuous line of width 1 (pixels)
    plt.plot(X, C, color="blue", linewidth=1.0, linestyle="-")

    # Plot sine using green color with a continuous line of width 1 (pixels)
    plt.plot(X, S, color="green", linewidth=1.0, linestyle="-")

    # Set x limits
    plt.xlim(-4.0,4.0)

    # Set x ticks
    plt.xticks(np.linspace(-4,4,9,endpoint=True))

    # Set y limits
    plt.ylim(-1.0,1.0)

    # Set y ticks
    plt.yticks(np.linspace(-1,1,5,endpoint=True))

    # Save figure using 72 dots per inch
    # savefig("../figures/exercice_2.png",dpi=72)

    # Show result on screen
    plt.show()

def import_things():
    """This just imports useful libraries"""
    import numpy as np
    import matplotlib.pyplot as plt
    import matplotlib.cm as cm

def scatter_plot():
    import numpy as np
    import matplotlib.pyplot as plt
    import matplotlib.cm as cm
    # New figure with white background
    fig = plt.figure(figsize=(6,6), facecolor='white')

    # New axis over the whole figure, no frame and a 1:1 aspect ratio
    ax = fig.add_axes([0,0,1,1], frameon=False, aspect=1)

    # Number of ring
    n = 50
    size_min = 50
    size_max = 50*50

    # Ring position
    P = np.random.uniform(0,1,(n,2))

    # Ring colors
    C = np.ones((n,4)) * (0,0,0,1)
    # Alpha color channel goes from 0 (transparent) to 1 (opaque)
    C[:,3] = np.linspace(0,1,n)

    # Ring sizes
    S = np.linspace(size_min, size_max, n)

    # Scatter plot
    scat = ax.scatter(P[:,0], P[:,1], s=S, lw = 0.5,
                      edgecolors = C, facecolors='None')

    # Ensure limits are [0,1] and remove ticks
    ax.set_xlim(0,1), ax.set_xticks([])
    ax.set_ylim(0,1), ax.set_yticks([])

    plt.show()

def scatter_challenge():
    """This is the code for making the complex scatter starting with the starter code"""
    import numpy as np
    import matplotlib.pyplot as plt
    import matplotlib.cm as cm

    n = 1024
    X = np.random.normal(-1,1,n)
    Y = np.random.normal(-1,1,n)

    color = np.arctan2(Y,X)

    # plt.scatter(X,Y,color = C,cmap = 'jet')
    ax = plt.subplot(111)
    the_plot = ax.scatter(X,Y,c = color, cmap = 'hsv', alpha = 0.5)

    plt.show()

def bar_challenge():
    """This is the code for making the complex bar plot starting with the starter code"""
    import numpy as np
    import matplotlib.pyplot as plt

    n = 12
    X = np.arange(n)
    Y1 = (1-X/float(n)) * np.random.uniform(0.5,1.0,n)
    Y2 = (1-X/float(n)) * np.random.uniform(0.5,1.0,n)

    plt.bar(X, +Y1, facecolor='#9999ff', edgecolor='white')
    plt.bar(X, -Y2, facecolor='#ff9999', edgecolor='white')

    for x,y in zip(X,Y1):
        plt.text(x, y+0.05, '%.2f' % y, ha='center', va= 'bottom')

    for x,y in zip(X,-Y2):
        plt.text(x, y-0.05, '%.2f' % y, ha = 'center', va = 'top')

    plt.ylim(-1.25,+1.25)
    plt.show()

def contour_challenge():
    """This is the code for making the contour plot work properly"""
    import numpy as np
    import matplotlib.pyplot as plt
    def f(x,y): return (1-x/2+x**5+y**3)*np.exp(-x**2-y**2)

    n = 256
    x = np.linspace(-3,3,n)
    y = np.linspace(-3,3,n)
    X,Y = np.meshgrid(x,y)

    plt.contourf(X, Y, f(X,Y), 8, alpha=.75, cmap='hot')
    C = plt.contour(X, Y, f(X,Y), 8, colors='black', linewidths=.5)
    plt.clabel(C)
    plt.show()

def neat_scatter():
    import numpy as np
    import matplotlib.pyplot as plt


    # Compute areas and colors
    N = 1024
    r = np.linspace(0,1,N)
    theta = np.linspace(0,360,N)
    area = 200 * r**2

    ax = plt.subplot(111, projection='polar')
    c = ax.scatter(theta, r, c=theta, s=50, cmap='hsv', alpha=0.75)

    plt.show()

def main():
    """This is just where all the code goes"""
    neat_scatter()
    scatter_challenge()
    bar_challenge()
    contour_challenge()

if __name__ == "__main__":
    main()
#
# using style sheets:
#   # be sure to               import matplotlib
#   # list of all of them:     matplotlib.style.available
#   # example of using one:    matplotlib.style.use( 'seaborn-paper' )
#
