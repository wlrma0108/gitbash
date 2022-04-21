from Andgate import AND
from Orgate import OR
from Nandgate import NAND

def XOR(x1,x2):
    s1=NAND(x1,x2)
    s2=OR(x1,x2)
    y=AND(s1,s2)
    return y 

if __name__ =='__main__':
    for xs in ([0,0],(1,0),(0,1),(1,1)):
        y=XOR(xs[0],xs[1])
        print(str(xs)+ "->"+str(y))
        