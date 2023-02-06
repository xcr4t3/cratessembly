import lib.variable as VAR
from random import randint, uniform

def _add(alpha, bravo, var: str):
    if (type(alpha) == float or type(alpha) == int) and (type(bravo) == float or type(bravo) == int):
        VAR._def(var, (alpha+bravo))
def _sub(alpha, bravo, var: str):
    if (type(alpha) == float or type(alpha) == int) and (type(bravo) == float or type(bravo) == int):
        VAR._def(var, (alpha-bravo))
def _mul(alpha, bravo, var: str):
    if (type(alpha) == float or type(alpha) == int) and (type(bravo) == float or type(bravo) == int):
        VAR._def(var, (alpha*bravo))
def _div(alpha, bravo, var: str):
    if (type(alpha) == float or type(alpha) == int) and (type(bravo) == float or type(bravo) == int):
        if bravo == 0 or alpha == 0:
            VAR._def(var, 0)
        else:
            VAR._def(var, (alpha/bravo))
def _ele(alpha, bravo, var: str):
    if (type(alpha) == float or type(alpha) == int) and (type(bravo) == float or type(bravo) == int):
        VAR._def(var, (alpha**bravo))
def _rin(alpha, bravo, charlie: str):
    VAR._def(charlie, randint(alpha, bravo))
def _rfl(alpha, bravo, charlie: str):
    VAR._def(charlie, uniform(alpha, bravo))
