from matplotlib import pyplot

# (c) Tom Wiesing 2015
# licensed under MIT license

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
