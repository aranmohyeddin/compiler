def get_main_st():
    return {"name": "main", "children": [], "parent": False, "symbols": {}}


def append_st(st, name):
    st["children"] += [{"name": name, "children": [], "parent": st, "symbols": {}}]


def local_lookup(st, name):
    if name in st["symbols"]:
        return st["symbols"][name]
    else:
        return False


def global_lookup(st, name):
    res = local_lookup(st, name)
    if res:
        return res, st
    elif st["parent"]:
        return global_lookup(st["parnet"], name)
    else:
        return False


# if a var can be redefined use a list and lookup in reversed order
def add_symbol(st, name, sd=None):
    if local_lookup(st, name):
        return False
    else:
        st["symbols"][name] = {
            "type": None,
            "addr": None,
            "ret_type": None,
            "params": [],
            "line": None,
            "ret_addr": None,
        }
        if sd:
            st["symbols"][name].update(sd)
