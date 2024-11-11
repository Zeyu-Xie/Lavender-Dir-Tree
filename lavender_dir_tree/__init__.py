from os import path, listdir

def _relpath(p, bp):
    return path.relpath(p, bp)


def _abspath(p):
    return path.abspath(p)


def _name(p):
    return path.basename(path.normpath(p))


def _DirTree(cp, _type, _rp):
    """
    cp: current path
    _type: type of the output
    _rp: root path
    """

    # cp is a file
    if path.isfile(cp):
        try:
            if _type == 'relpath':
                return _relpath(cp, _rp)
            elif _type == 'abspath':
                return _abspath(cp)
            elif _type == 'name':
                return _name(cp)
            else:
                return _relpath(cp, _rp)
        except Exception as e:
            return str(f"{_type(e).__name__}: {e}")
    # cp is a directory
    else:
        try:
            tree = {}
            for item in listdir(cp):
                tree[item] = _DirTree(path.join(cp, item), _type, _rp)
            return tree
        except Exception as e:
            return str(f"{type(e).__name__}: {e}")


def DirTree(cp, type='relpath'):
    """
    cp: current path
    type: type of the output, default is 'relpath'
    """

    # Check if the type is legal
    legal_types = ['relpath', 'abspath', 'name']
    if type not in legal_types:
        raise ValueError(
            f"Invalid type: {type}. Legal types are {legal_types}")

    # Return the tree
    return _DirTree(cp, type, cp)

__all__ = ['DirTree']