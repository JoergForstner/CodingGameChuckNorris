
# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
def string2bits(s=''):
    return [bin(ord(x))[2:].zfill(7) for x in s]

def firstseries(argument):
    switcher = {
        '0': "00 ",
        '1': "0 "   
    }
    return switcher.get(argument, "Invalid string")

def space(argument):
    switcher = {
        '': "",
    }
    return switcher.get(argument," ")

message = input()

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)
bitstring = string2bits(message);
encodedstring  = '';
lastbitstring = '';

for i in range( len(bitstring) ):
    for j in range( len(bitstring[i]) ):
        if(lastbitstring != bitstring[i][j]):
          encodedstring = encodedstring + space(encodedstring) + firstseries(bitstring[i][j]);  
        encodedstring = encodedstring + '0';
        lastbitstring = bitstring[i][j];

print(encodedstring);
