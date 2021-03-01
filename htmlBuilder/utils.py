import collections.abc

def flatten_params(params):
    result = []
    for item in params:
        if issubclass(item.__class__, collections.abc.Iterable) and not issubclass(item.__class__, str):
            for element in flatten_params(item):
                result.append(element)
        else:
            result.append(item)
    return result
