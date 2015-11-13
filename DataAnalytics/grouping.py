import numpy as np

def group_indexes_by(data, group):
    """
        groups the indexes of an array.

        data: Array of which the indexes should be sorted
        group: Array of functions that should return if an item belongs to a group.
    """

    # create an array of groups
    groups = [[] for g in group]

    # iterate through the data
    for j, d in enumerate(data):
        # and through the groups
        for i, g in enumerate(group):
            if g(d):
                groups[i].append(j)

    return groups

def make_group_order(data, group):
    """
        Groups the indexes of an array and returns one array with indexes on a per-group basis.

        data: Array of which the indexes should be sorted
        group: Array of functions that should return if an item belongs to a group.
    """

    # make groups
    groups = group_indexes_by(data, group)

    # create a new array of groups
    go = []

    # add all of them
    for g in groups:
        go += g

    # return the list of groups
    return go

def make_labels(groups, group_labels=None):
    """
        Makes labels and new group mappings.

        groups: List of groups. 
        group_labels: Labels for the groups. Optional.
    """

    # we do not have group labels
    newgroups = sorted(list(set(groups)))

    # make new group identifiers
    pgroups = np.array(
        list(
            map(
                lambda g:newgroups.index(g),
                groups
            )
        )
    )

    if group_labels == None:
        # if we do not have labels, use the group id as a label
        plabels = list(map(str, newgroups))
    else:
        plabels = group_labels

    return (pgroups, plabels)
