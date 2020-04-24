def error(x):
    raise TypeError(x)


def ft_map(function_to_apply, list_of_inputs):
    if (list_of_inputs is None or function_to_apply is None):
        error("Input error")
    final = []
    for i in list_of_inputs:
        final.append(function_to_apply(i))
    return final
    pass
