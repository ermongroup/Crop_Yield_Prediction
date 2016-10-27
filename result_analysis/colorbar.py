from matplotlib import pyplot
import matplotlib as mpl

# Make a figure and axes with dimensions as desired.
fig = pyplot.figure()
ax2 = fig.add_axes([0.1, 0.1, 0.02, 0.8])



# The second example illustrates the use of a ListedColormap, a
# BoundaryNorm, and extended ends to show the "over" and "under"
# value colors.
cmap = mpl.colors.ListedColormap(["#d6604d", "#f4a582", "#fddbc7", "#d1e5f0", "#92c5de", "#4393c3"])
cmap.set_over("#2166ac")
cmap.set_under("#b2182b")

# If a ListedColormap is used, the length of the bounds array must be
# one greater than the length of the color list.  The bounds must be
# monotonically increasing.
bounds = [-15,-10, -5, 0, 5, 10,15]
norm = mpl.colors.BoundaryNorm(bounds, cmap.N)
cb2 = mpl.colorbar.ColorbarBase(ax2, cmap=cmap,
                                norm=norm,
                                # to use 'extend', you must
                                # specify two extra boundaries:
                                boundaries=[-20] + bounds + [20],
                                extend='both',
                                ticks=bounds,  # optional
                                spacing='proportional',
                                orientation='vertical')



pyplot.show()