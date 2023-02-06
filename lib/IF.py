import bin.variable as VAR

def _equ(alpha, bravo, charlie, delta):
    if alpha == bravo:
        VAR._def(delta, charlie)
def _not(alpha, bravo, charlie, delta):
    if alpha != bravo:
        VAR._def(delta, charlie)
def _moe(alpha, bravo, charlie, delta):
    if alpha >= bravo:
        VAR._def(delta, charlie)
def _soe(alpha, bravo, charlie, delta):
    if alpha <= bravo:
        VAR._def(delta, charlie)
def _mre(alpha, bravo, charlie, delta):
    if alpha > bravo:
        VAR._def(delta, charlie)
def _sma(alpha, bravo, charlie, delta):
    if alpha < bravo:
        VAR._def(delta, charlie)