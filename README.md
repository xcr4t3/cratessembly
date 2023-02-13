# Cratessembly
Cratessembly is a open-source coding language. Created by me, as a challenge for myself. It's sytaxis looks like Assembly, and I wanted it to have my name.

## How to use
First of all, download all the repo as a zip file, uncompress in anyfolder you want, then, you will need only python (3.11 or new versions), then, you can try making a cratessembly file by yourself, or use this as an try code:
<code>
def alpha 1
prt alpha
def alpha 2
prt alpha
</code>
Then, save it with whatever name you want, and then run cly.py and with the filename.cly as the arg.
This should show 1 and 2 in 2 lines, if that's not the case, report it.
## Types
At the moment, the only types are int and floats. Strings will be added in a future. But booleans wont! (This becuase there is not usage for them at all)

## What should you report at "Issues" tab?
What I will suggest you, is to report python crashes (any crash that is made using cly.py) and cratessembly bugs. Will read it!

## Functions

def -
The "def" function is for declaring variables, all variables are declared globally and are not constant
Usage:
def name value
example:
def alpha 10

inp -
The "inp" function is for asking the user a input, at the moment it uses DDIT (Default Display Input Text), but is planned to add the CDIT (Custom Display Input Text). This, and other functions, ask you a var to save the input or output.
usage:
inp name_var
example:
inp bravo

prt -
The "prt" functions is the only function that can print chars into the screen.
usage:
prt float/int/var
example:
prt alpha

rin -
The "rin" function save a random number between the alpha and bravo given.
usage:
rin alpha bravo var
example:
rin alpha bravo charlie

rfl -
The "rfl" function save a random number between the alpha and bravo given, but in float.
usage:
rfl alpha bravo var
example:
rfl alpha bravo charlie

del -
The "del" function deletes a variable.
usage:
del alpha
example:
del alpha

add/sub/mul/div/ele -
This are the math operators. This is a list of which is X operator.
Func - Operator
|--------|
|add   + |
|sub   - |
|mul   * | 
|div   / |
|ele   **|
usage:
func alpha bravo var
example:
add 7 bravo result

