def group_by(function, args):
    """
    (function, list) -> dictionary of lists
    This function get a function and a list of arguments and return a dictionary of lists
    """

    dictionary = {}
    for arg in args:
        dictionary.setdefault(function(arg), []).append(arg)
    return dictionary


def main():
    """ test the function group_by"""
    print(group_by(len, ["hi", "bye", "yo", "try"]))


if __name__ == '__main__':
    main()

