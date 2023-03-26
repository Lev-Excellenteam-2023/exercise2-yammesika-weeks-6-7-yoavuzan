def group_by(l, args):
    dic = {}
    for arg in args:
        dic.setdefault(l(arg), []).append(arg)
    return dic


print(group_by(len, ["hi", "bye", "yo", "try"]))