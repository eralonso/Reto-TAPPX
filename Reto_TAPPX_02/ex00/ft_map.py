def ft_map(function_to_apply, iterable):
    """Map the function to all elements of the iterable. Args:
    function_to_apply: a function taking an iterable.
    iterable: an iterable object (list, tuple, iterator). Return:
    An iterable.
    None if the iterable can not be used by the function. """
    res = list()
    for elem in iterable:
        res.append(function_to_apply(elem))
    if (type(iterable) == tuple):
        res = tuple(res)
    return (res)

