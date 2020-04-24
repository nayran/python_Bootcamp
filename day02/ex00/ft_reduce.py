def error(x):
    raise TypeError(x)


def ft_reduce(function_to_apply, list_of_inputs):
    if (list_of_inputs is None or function_to_apply is None):
        error("Input error")
    final = list_of_inputs[0]
    for i in list_of_inputs[1:]:
        final = function_to_apply(final, i)
    return final
    pass
