
##################################################
# treescanner
##################################################
def treescanner(tree):
    """
    enumerate all leaves in a tree
    """
    # a typical example where
    # the 'yield from' statement 
    # is the only way to go
    if isinstance(tree, list):
        for subtree in tree:
            yield from treescanner(subtree)
    else:
        yield tree

