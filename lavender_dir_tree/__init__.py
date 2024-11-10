from os import path, listdir


def _name(p):
    return path.basename(path.normpath(p))


def DirTree(cp):

    if path.isfile(cp):
        try:
            return _name(cp)
        except Exception as e:
            return str(f"{type(e).__name__}: {e}")
    else:
        try:
            tree = {}
            for item in listdir(cp):
                tree[item] = DirTree(path.join(cp, item))
            return tree
        except Exception as e:
            return str(f"{type(e).__name__}: {e}")

__all__ = ['DirTree']