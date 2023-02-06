import bin.variable as VAR

def _prt(alpha):
    try:
        print(alpha)
    except:
        return "PRT_ERR"
def _inp(var: str):
    try:
        f = float(input("Input required: "))
        s = str(f).endswith(".0")
        x = 0
        if s:
            x = int(f)
        else:
            x = f
        VAR._def(var, x)
    except:
        return "INP_ERR"