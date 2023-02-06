# Imports (Own)
import lib._math as MATH
import lib.variable as VAR
import lib.console as CON
import lib.IF as IF
# Imports (Not created by me)
from sys import argv
import string
chars = list(string.punctuation)
chars.pop(13)
# Vars intializations
largs = []

# Checking if file has been given by the user
if len(argv) != 2:
    exit()

# File spliter
lines = open(argv[1], "r").read().rsplit("\n")
for line in lines:
    args = line.split(" ")
    largs.append(args)
lines = largs
del largs

for line in lines:
    if (line[0].startswith("#")) or (line[0].startswith("//")):
        None
    else:
        for arg in line:
            for char in chars:
                if arg.__contains__(char) or arg.endswith(".") or arg.startswith("."):
                    print("Error: Argument contains punctuation or starts/ends with dot!!")
                    exit()

# Looking for functions calls
for line in lines:
    if line[0].startswith("#") or line[0].startswith("//"):
        None
    elif line[0] == "inp" and len(line) == 2:
        try:
            float(line[1])
            print("A Number was given as a var name!")
            exit()
        except:
            err = CON._inp(line[1])
            if err == "INP_ERR":
                print("Error at input!")
                exit()
    elif line[0] == "prt" and len(line) == 2:
        prt_txt = None
        try:
            prt_txt = float(line[1])
        except:
            try:
                prt_txt = VAR.get(line[1])
            except:
                print("Error: Print error! Var '" + line[1] + "' not found!")
                exit()
        err = CON._prt(prt_txt)
        if err == "PRT_ERR":
            print("Error at print!")
            exit()
    elif line[0] == "def" and len(line) == 3:
        contain = 0
        try:
            float(line[1])
            print("A Number was given as a var name!")
            exit()
        except:
            try:
                contain = float(line[2])
                s = str(contain).endswith(".0")
                x = 0
                if s:
                    x = int(contain)
                else:
                    x = contain
            except:
                try:
                    x = VAR.get(line[2])
                except:
                    print("Given var result is not a var or a number!")
                    exit()
            err = VAR._def(line[1], x)
            if err == "DEF_ERR":
                print("Error at define!")
                exit()
    elif line[0] == "add" and len(line) == 4:
        alpha = 0
        bravo = 0
        try:
            alpha = float(line[1])
        except:
            try:
                alpha = VAR.get(line[1])
            except:
                print("Alpha not founded!")
                exit()
        try:
            bravo = int(line[2])
        except:
            try:
                bravo = VAR.get(line[2])
            except:
                print("Bravo not founded!")
                exit()
        try:
            float(line[3])
            print("A Number was given as a var name!")
            exit()
        except:
            MATH._add(alpha, bravo, line[3])
    elif line[0] == "sub" and len(line) == 4:
        alpha = 0
        bravo = 0
        try:
            alpha = float(line[1])
        except:
            try:
                alpha = VAR.get(line[1])
            except:
                print("Alpha not founded!")
                exit()
        try:
            bravo = float(line[2])
        except:
            try:
                bravo = VAR.get(line[2])
            except:
                print("Bravo not founded!")
                exit()
        try:
            float(line[3])
            print("A Number was given as a var name!")
            exit()
        except:
            MATH._sub(alpha, bravo, line[3])
    elif line[0] == "mul" and len(line) == 4:
        alpha = 0
        bravo = 0
        try:
            alpha = float(line[1])
        except:
            try:
                alpha = VAR.get(line[1])
            except:
                print("Alpha not founded!")
                exit()
        try:
            bravo = int(line[2])
        except:
            try:
                bravo = VAR.get(line[2])
            except:
                print("Bravo not founded!")
                exit()
        try:
            float(line[3])
            print("A Number was given as a var name!")
            exit()
        except:
            MATH._mul(alpha, bravo, line[3])
    elif line[0] == "div" and len(line) == 4:
        alpha = 0
        bravo = 0
        try:
            alpha = float(line[1])
        except:
            try:
                alpha = VAR.get(line[1])
            except:
                print("Alpha not founded!")
                exit()
        try:
            bravo = int(line[2])
        except:
            try:
                bravo = VAR.get(line[2])
            except:
                print("Bravo not founded!")
                exit()
        try:
            float(line[3])
            print("A Number was given as a var name!")
            exit()
        except:
            MATH._div(alpha, bravo, line[3])
    elif line[0] == "ele" and len(line) == 4:
        alpha = 0
        bravo = 0
        try:
            alpha = float(line[1])
        except:
            try:
                alpha = VAR.get(line[1])
            except:
                print("Alpha not founded!")
                exit()
        try:
            bravo = int(line[2])
        except:
            try:
                bravo = VAR.get(line[2])
            except:
                print("Bravo not founded!")
                exit()
        try:
            float(line[3])
            print("A Number was given as a var name!")
            exit()
        except:
            MATH._ele(alpha, bravo, line[3])
    elif line[0] == "equ" and len(line) == 5:
        alpha = 0
        bravo = 0
        charlie = 0
        delta = 0
        try:
            try:
                alpha = float(line[1])
            except:
                try:
                    alpha = VAR.get(line[1])
                except:
                    print("Alpha not found!")
                    exit()
            try:
                bravo = float(line[2])
            except:
                try:
                    bravo = VAR.get(line[2])
                except:
                    print("Bravo not found!")
                    exit()
            try:
                charlie = float(line[4])
            except:
                try:
                    charlie = VAR.get(line[4])
                except:
                    print("Charlie not found!")
                    exit()
            delta = line[3]
            IF._equ(alpha, bravo, charlie, delta)
        except:
            print("Error at EQU")
            exit()
    elif line[0] == "not" and len(line) == 5:
        alpha = 0
        bravo = 0
        charlie = 0
        delta = 0
        try:
            try:
                alpha = float(line[1])
            except:
                try:
                    alpha = VAR.get(line[1])
                except:
                    print("Alpha not found!")
                    exit()
            try:
                bravo = float(line[2])
            except:
                try:
                    bravo = VAR.get(line[2])
                except:
                    print("Bravo not found!")
                    exit()
            try:
                charlie = float(line[4])
            except:
                try:
                    charlie = VAR.get(line[4])
                except:
                    print("Charlie not found!")
                    exit()
            delta = line[3]
            IF._not(alpha, bravo, charlie, delta)
        except:
            print("Error at NOT")
            exit()
    elif line[0] == "moe" and len(line) == 5:
        alpha = 0
        bravo = 0
        charlie = 0
        delta = 0
        try:
            try:
                alpha = float(line[1])
            except:
                try:
                    alpha = VAR.get(line[1])
                except:
                    print("Alpha not found!")
                    exit()
            try:
                bravo = float(line[2])
            except:
                try:
                    bravo = VAR.get(line[2])
                except:
                    print("Bravo not found!")
                    exit()
            try:
                charlie = float(line[4])
            except:
                try:
                    charlie = VAR.get(line[4])
                except:
                    print("Charlie not found!")
                    exit()
            delta = line[3]
            IF._moe(alpha, bravo, charlie, delta)
        except:
            print("Error at MOE")
            exit()
    elif line[0] == "soe" and len(line) == 5:
        alpha = 0
        bravo = 0
        charlie = 0
        delta = 0
        try:
            try:
                alpha = float(line[1])
            except:
                try:
                    alpha = VAR.get(line[1])
                except:
                    print("Alpha not found!")
                    exit()
            try:
                bravo = float(line[2])
            except:
                try:
                    bravo = VAR.get(line[2])
                except:
                    print("Bravo not found!")
                    exit()
            try:
                charlie = float(line[4])
            except:
                try:
                    charlie = VAR.get(line[4])
                except:
                    print("Charlie not found!")
                    exit()
            delta = line[3]
            IF._soe(alpha, bravo, charlie, delta)
        except:
            print("Error at SOE")
            exit()
    elif line[0] == "mre" and len(line) == 5:
        alpha = 0
        bravo = 0
        charlie = 0
        delta = 0
        try:
            try:
                alpha = float(line[1])
            except:
                try:
                    alpha = VAR.get(line[1])
                except:
                    print("Alpha not found!")
                    exit()
            try:
                bravo = float(line[2])
            except:
                try:
                    bravo = VAR.get(line[2])
                except:
                    print("Bravo not found!")
                    exit()
            try:
                charlie = float(line[4])
            except:
                try:
                    charlie = VAR.get(line[4])
                except:
                    print("Charlie not found!")
                    exit()
            delta = line[3]
            IF._mre(alpha, bravo, charlie, delta)
        except:
            print("Error at MRE")
            exit()
    elif line[0] == "sma" and len(line) == 5:
        alpha = 0
        bravo = 0
        charlie = 0
        delta = 0
        try:
            try:
                alpha = float(line[1])
            except:
                try:
                    alpha = VAR.get(line[1])
                except:
                    print("Alpha not found!")
                    exit()
            try:
                bravo = float(line[2])
            except:
                try:
                    bravo = VAR.get(line[2])
                except:
                    print("Bravo not found!")
                    exit()
            try:
                charlie = float(line[4])
            except:
                try:
                    charlie = VAR.get(line[4])
                except:
                    print("Charlie not found!")
                    exit()
            delta = line[3]
            IF._sma(alpha, bravo, charlie, delta)
        except:
            print("Error at SMA")
            exit()
    elif line[0] == "rin" and len(line) == 4:
        alpha = 0
        bravo = 0
        try:
            alpha = float(line[1])
        except:
            try:
                alpha = VAR.get(line[1])
            except:
                print("Alpha not founded!")
                exit()
        try:
            bravo = int(line[2])
        except:
            try:
                bravo = VAR.get(line[2])
            except:
                print("Bravo not founded!")
                exit()
        try:
            float(line[3])
            print("A Number was given as a var name!")
            exit()
        except:
            MATH._rin(alpha, bravo, line[3])
    elif line[0] == "rfl" and len(line) == 4:
        alpha = 0
        bravo = 0
        try:
            alpha = float(line[1])
        except:
            try:
                alpha = VAR.get(line[1])
            except:
                print("Alpha not founded!")
                exit()
        try:
            bravo = int(line[2])
        except:
            try:
                bravo = VAR.get(line[2])
            except:
                print("Bravo not founded!")
                exit()
        try:
            float(line[3])
            print("A Number was given as a var name!")
            exit()
        except:
            MATH._rfl(alpha, bravo, line[3])
    elif line[0] == "del" and len(line) == 2:
        if VAR._del(line[1]) != "DEL_ERR":
            try:
                float(line[1])
                print("A Number was given as a var name!")
                exit()
            except:
                VAR._del(line[1])
        else:
            print("ERROR AT DEL")
            exit()
    elif line[0]:
        print("Error! Function '" + line[0] + "' not found, need arguments o has more than what it needs!")
        exit()
