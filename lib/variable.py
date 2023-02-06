vars = {}

def _def(name: str, value):
    try:
        vars[name] = value
    except:
        return "DEF_ERR"
def get(name: str):
    return vars[name]
def _del(name: str):
    try:
        del vars[name]
    except:
        return "DEL_ERR"