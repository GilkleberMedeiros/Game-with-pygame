msgs = {"stop": False, "instance": None}

def get_msg(key):
    return msgs[key]

def set_msg(key, value):
    msgs[key] = value