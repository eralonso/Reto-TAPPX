def ft_reduce(function_to_apply, iterable):
    """Apply function of two arguments cumulatively.
    Args:
    function_to_apply: a function taking an iterable.
    iterable: an iterable object (list, tuple, iterator).
    Return:
    A value, of same type of elements in the iterable parameter.
    None"""
    res = iterable[0]
    iterator = iterable
    iterator.pop(0)
    for elem in iterator:
        res = function_to_apply(res, elem)
    return (res)

