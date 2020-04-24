def error(x):
    raise TypeError(x)


def ft_filter(function_to_apply, list_of_inputs):
    if (list_of_inputs is None or function_to_apply is None):
        error("Input error")
    final = []
    for i in list_of_inputs:
        if function_to_apply(i):
            final.append(i)
    return final
    pass
