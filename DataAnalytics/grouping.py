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
