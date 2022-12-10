# S C I E N T I F I C   C A L C U L A T O R


#import math library

import math
print("S C I E N T I F I C   C A L C U L A T O R")
print("")
print("")
print("Select from the given operations you want to perform (i.e 1, 2, 3, 4 or 5)")
print("")
print("1.Algebraic: ")
print("2.root and exponent: ")
print("3.trigno: ")
print("4.angle: ")
print("5.EXIT")
print("")
    
#defining algebraic function

#1
def algebra():
    print("\n")
    print("1.Addition:" )
    print("2.Subtraction: ")
    print("3.Multiplication: ")
    print("4.Division: ")
    print("5.Mod: ")
    n=int(input("Select Operation: "))
    
    def add(a,b):
        print("Addition of",a,'and',b,'=',a+b)
        
    def sub(a,b):
        print("Subtraction of",a,'and',b,'=',a-b)
             
    def mul(a,b):
        print('Multiplication of',a,'and',b,'=',a*b)
             
    def div(a,b):
        print('Division of',a,'and',b,'=',a/b)
        
    def mod(a,b):
        print('Mod of',a,'and',b,'=',a%b)
        
    if n>5:
        print("Invalid ,please select from the given options !")
        print('\n')
             
    else:
        a=float(input("no.1: "))
        b=float(input("no.2: "))
        if n==1:
            add(a,b)
        if n==2:
            sub(a,b)
        if n==3:
            mul(a,b)
        if n==4:
            div(a,b)
        if n==5:
            mod(a,b)
            
#defining exponent and sqrt function
            
#2
def rt():
    print("1.Exponent: ")
    print("2.Square root: ")
    n=int(input("Select Operation: "))
    
    def exp(a,b):
        print(a**b)
    def root(a):
        print("Square Root of",a,'=',a**(1/2))
        
    if n>2:
        print('Invalid ,please select from the given options !')
        print('\n')
             
    else:
        if n==1:
            a=int(input("Value of a: "))
            b=int(input("Value of b: "))
            exp(a,b)
        if n==2:
            a=int(input("Value of A: "))
            root(a)

# defining trigonometric function

#3            
def trig():
    print("1.sine")
    print("2.cosine")
    print("3.tan")
    n=int(input("Select Operation: "))
    
    if n>3:
        print('Invalid ,please try from the given options !')
        print("\n")
             
    else:
        a=int(input())
        if n==1:
            print("{:.6f}".format(math.sin(a)),"rad")
        if n==2:
            print("{:.6f}".format(math.cos(a)),"rad")
        if n==3:
            print("{:.6f}".format(math.tan(a)),"rad")

# defining angular function

#4                 
def ang():
    print("1.deg to rad")
    print("2.rad to deg")
    n=int(input("Select Operation: "))
    
    if n >2:
        print('Invalid ,please try from the given options !')
        print('\n')
             
    else:
        a=float(input())
        if n==1:
            print(math.radians(a))
        if n==2:
            print(math.degrees(a))
            
while True:
    n=int(input("Select Operation: "))
    if n>5:
        print('Invalid ,please try from the given options !')
    else:
        if n==1:
            algebra()
        if n==2:
            rt()
        if n==3:
            trig()
        if n==4:
            ang()
        if n==5:
            print("")
#5
            print("_____EXIT_____")
            break
