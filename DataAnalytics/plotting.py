from matplotlib import pyplot, ticker, cm
import numpy as np

# (c) Tom Wiesing 2015
# licensed under MIT license


def colormesh(M, title="", xlabels=None, ylabels=None, cmap="YlOrBr", show=True):
    """
        Makes a colormesh plot of a matrix

        M: Matrix to visualise.
        title: Title of plot. Optional.
        xlabels: Labels for values along the 0th axis of the matrix. Optional.
        ylabels: Labels for values along the 1st axis of the matrix. Optional.
        cmap: Colormap to use. Defaults to "YlOrBr"
        show: Should the figure be shown immediatly. Defaults to True.
    """

    # generate the axis
    x = range(M.shape[0])
    y = range(M.shape[1])

    # make a meshgrid
    x, y = np.meshgrid(x, y)

    # make a figure
    fig = pyplot.figure()
    fig.suptitle(title)

    # add a color grid and a colorbar
    ax = fig.add_subplot(1, 1, 1)
    ax.set_xlim([0, M.shape[0] - 1])
    ax.set_ylim([0, M.shape[1] - 1])


    cm = ax.pcolormesh(x, y, M, cmap=pyplot.get_cmap(cmap))
    fig.colorbar(cm)

    # labels for x
    if xlabels:
        pyplot.xticks(list(range(M.shape[0])), xlabels, rotation='vertical')

    # labels for y
    if ylabels:
        pyplot.yticks(list(range(M.shape[1])), ylabels)

    # show the figure if asked to
    if show:
        pyplot.show()

    # return the figure
    return fig

def paralellLines(M,axis=1,labels=(), interactive=True, title="",show=True):
    """
        Makes an optionally interactive paralell Lines plot.

        M: Matrix to visualise.
        axis: Axis of data values to plot. Needs to be either 1 or 0. Defaults to 1.
        labels: Labels of the axes to plot.
        interactive: Determines if the plot is interactive. Defaults to True.
        title: Title of the Plot to make. Defaults to "".
        show: Should the figure be shown immediatly. Defaults to True.
    """

    # ensure axis is of the right type.
    if axis != 1 and axis != 0:
        raise ValueError("Axis must be 0 or 1")

    if axis == 0:
        return paralellLines(M.T,axis=1,components=components,labels=labels,title=title,show=show)

    # do we have enough components?
    if M.shape[0] != len(labels):
        raise ValueError("Not enough labels for all components. ")

    # make a figure with a title.
    fig = pyplot.figure()
    fig.suptitle(title)

    # and an axis
    ax = fig.add_subplot(111)

    xs = range(M.shape[0])
    ys = range(M.shape[1])

    # plot all the lines.
    for y in ys:
        ax.plot(xs, M[:,y], 'k-', picker=5)

    xlim = ax.get_xlim()
    ylim = ax.get_ylim()

    zorder = ax.get_zorder()

    # add a bunch of new axes
    for (x, l) in zip(xs, labels):

        # add another axis.
        newaxis = ax.twinx()
        zorder = max(zorder, newaxis.get_zorder())

        # set its x and y limits
        newaxis.set_xlim(xlim)
        newaxis.set_ylim(ylim)

        # set the color
        newaxis.spines['left'].set_color('none')
        newaxis.spines['right'].set_position(('data',x))

        # hide the x axis
        newaxis.get_xaxis().set_visible(False)

        # and add a label
        newaxis.text(x, ylim[1],l, horizontalalignment='right',verticalalignment='top',rotation='horizontal')

    # Hide all the other axes.
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    # clear that plot
    ax.lines = []

    # add a new plot on top
    finalaxis = ax.twinx()

    # set the xaxis and yaxis
    finalaxis.set_xlim(xlim)
    finalaxis.set_ylim(ylim)

    # hide the splines
    finalaxis.get_xaxis().set_visible(False)
    finalaxis.get_yaxis().set_visible(False)

    # add all the lines (again)
    for y in ys:
        finalaxis.plot(xs, M[:,y], 'k-', picker=5 if interactive else False,zorder=1)

    # add interactivity
    def onclick(event):
        thisline = event.artist

        if thisline.get_color() == 'red':
            for l in finalaxis.lines:
                l.set_color('k')
                l.set_zorder(1)
        else:
            for l in finalaxis.lines:
                l.set_color('gray')
                l.set_zorder(1)
            thisline.set_color('red')
            thisline.set_zorder(2)
        pyplot.draw()

    if interactive:
        fig.canvas.mpl_connect('pick_event', onclick)

    # show it if we want to.
    if show:
        pyplot.show()

    # return the figure.
    return fig

def scatter(M,axis=1,components=(0, 1), labels=("", ""), title="",show=True):
    """
        Return a figure of a Scatterplot of the matrix M.

        M: Matrix to visualise.
        axis: Axis of data values to plot. Needs to be either 1 or 0. Defaults to 1.
        components: Components to make a scatter plot of. Defaults to (0, 1).
        title: Title of the Plot to make. Defaults to "".
        labels: Labels of the axes to plot.
        show: Should the figure be shown immediatly. Defaults to True.
    """

    # ensure axis is of the right type.
    if axis != 1 and axis != 0:
        raise ValueError("Axis must be 0 or 1")

    if axis == 0:
        return scatter(M.T,axis=1,components=components,labels=labels,title=title,show=show)

    # make a figure with a title.
    fig = pyplot.figure()
    fig.suptitle(title)

    # make a scatter plot.
    pyplot.scatter(M[components[0],:], M[components[1],:])

    # set a few labels
    pyplot.xlabel(labels[0])
    pyplot.ylabel(labels[1])

    # show it if we want to.
    if show:
        pyplot.show()

    # return the figure.
    return fig


def SPLOM(M,axis=1,title="",show=True):
    """
        Return a figure of a SPLOM of a matrix M.

        M: Matrix to visualise.
        axis: Axis of data values to plot. Needs to be either 1 or 0. Defaults to 1.
        title: Title of the Plot to make. Defaults to "".
        show: Should the figure be shown immediatly. Defaults to show.
    """

    # ensure axis is of the right type.
    if axis != 1 and axis != 0:
        raise ValueError("Axis must be 0 or 1")

    # Create a new figure.
    fig = pyplot.figure()
    fig.suptitle(title)

    # a counter
    c = 1

    if axis == 0:
        # for axis 0, work on the transpose.
        return SPLOM(M.T,axis=1,title=title)

    # make a list of columns
    count = M.shape[0]
    columns = range(count)

    # iterate over them and do a plot.
    for x in columns:
        for y in columns:
            fig.add_subplot(count, count, c).scatter(M[x,:], M[y,:])
            c += 1

    # show it if we want to.
    if show:
        pyplot.show()

    # return the figure.
    return fig
