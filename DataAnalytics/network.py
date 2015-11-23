import networkx as nx
from matplotlib import pyplot

def from_ajacency_map(amap, directed = False):
    """
        Turns a map of adjacencies into a graph.

        amap: Adjacency Dict
        direct: If set to true, an undirected graph will be created.
    """
    return nx.from_dict_of_lists(amap, nx.DiGraph() if directed else nx.Graph())

def plot_graph(G, title=None, pos=None, show=True, interactive=True, **kwargs):
    # get the current figure and axis
    fig = pyplot.figure()
    ax = pyplot.gca()

    # if there is no layout, make a spring layout.
    if pos == None:
        pos = nx.spring_layout(G)

    # get a list of nodes of G
    nodes = list(G)

    # Draw the graph
    nx.draw(G, pos=pos, ax=ax, **kwargs)

    #  make the graph interactive if wanted
    if interactive:
        picked = [-1]

        def onpick(event):
            if picked[0] == event.ind[0]:
                picked[0] = -1

                # remove the highlighted node
                scatter_nodes[0].remove()
                scatter_nodes[0] = None
            else:
                picked[0] = event.ind[0]
                node = nodes[event.ind[0]]

                # remove any older highlight if available
                if scatter_nodes[0]:
                    scatter_nodes[0].remove()

                reachable = nx.algorithms.dag.descendants(G, node)
                reachable.add(node)


                # draw our node
                scatter_nodes[0] = nx.draw_networkx_nodes(G, pos=pos, nodelist=reachable, node_color='b', **kwargs)

            # update the draw
            pyplot.draw()

        # Make the first element pickable
        ax.collections[0].set_picker(True)
        scatter_nodes = [None]

        fig.canvas.mpl_connect('pick_event', onpick)



    # show if wanted
    if show:
        pyplot.show()

    return fig
