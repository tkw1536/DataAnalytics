import networkx as nx
import numpy as np
from matplotlib import pyplot, collections

def from_ajacency_map(amap, directed = False):
    """
        Turns a map of adjacencies into a graph.

        amap: Adjacency Dict
        direct: If set to true, an undirected graph will be created.
    """
    return nx.from_dict_of_lists(amap, nx.DiGraph() if directed else nx.Graph())

def plot_graph(G, title=None, pos=None, show=True, interactive=True, interaction_node=None, interactions={}, **kwargs):
    # get the current figure and axis
    fig = pyplot.figure()
    ax = pyplot.gca()

    # if there is no layout, make a spring layout.
    if pos == None:
        pos = nx.spring_layout(G)

    # get a list of nodes of G
    nodes = list(G)

    keys = interactions.keys()

    def reset_graph():
        ax.clear()

        nx.draw(G, pos=pos, ax=ax, **kwargs)
        ax.collections[0].set_picker(True)

        ytexts = np.linspace(ax.get_ylim()[0], ax.get_ylim()[1], len(keys) + 2)[1:-1]

        for k, y in zip(keys, ytexts):
            pyplot.text(ax.get_xlim()[0], y, k, picker=True)

        return G


    if interaction_node == None:
        def interaction_node(G, node, event):
            if event.mouseevent.button == 3:
                reachable = nx.algorithms.dag.ancestors(G, node)
                reachable.add(node)
            else:
                reachable = nx.algorithms.dag.descendants(G, node)
                reachable.add(node)
            return G.subgraph(reachable)

    #  make the graph interactive if wanted
    if interactive:
        picked_node = [-1]
        picked_text = [-1]

        def onpick(event):
            if isinstance(event.artist, collections.PathCollection):
                onpick_node(event)
            else:
                onpick_text(event)

            # update the draw
            pyplot.draw()
        def onpick_text(event):
            # clear figure and things
            G = reset_graph()

            label = event.artist.get_text()

            if picked_text[0] == label:
                picked_text[0] = -1
            else:
                picked_text[0] = label
                subgraph = interactions[label](G)
                nx.draw_networkx(subgraph, ax=ax, with_labels=False, pos=pos, edge_color='g', node_color='g', **kwargs)

        def onpick_node(event):
            # clear figure and things
            G = reset_graph()

            if picked_node[0] == event.ind[0]:
                picked_node[0] = -1
            else:
                picked_node[0] = event.ind[0]
                node = nodes[event.ind[0]]

                # draw
                subgraph = interaction_node(G, node, event)
                nx.draw_networkx(subgraph, ax=ax, with_labels=False, pos=pos, edge_color='b', node_color='b', **kwargs)

        reset_graph()


        fig.canvas.mpl_connect('pick_event', onpick)



    # show if wanted
    if show:
        pyplot.show()

    return fig
