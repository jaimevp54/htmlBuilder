def flatten_params(params):
    result = []
    for item in params:
        if isinstance(item, (list, tuple)):
            for element in flatten_params(item):
                result.append(element)
        else:
            result.append(item)
    return result
